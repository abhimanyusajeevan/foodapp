from django.shortcuts import render
from .models import regdata,fooditem,cartitem,address,state,discount
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse,Http404,HttpResponseRedirect 
from django.urls import reverse
# Create your views here.
# Have set up a migration file which inputs data of states and populates state model

    
def index(request):
    name= None
    if request.user.is_authenticated:
        name=request.user.username

    
    return render(request, 'foodapp/index.html',{'name':name})
     
  


def loginpage(request):
    name= None
    if request.user.is_authenticated:
        name=request.user.username
        return render(request, 'foodapp/index.html',{'name':name})
    return render(request, 'foodapp/login.html',{'i':0})


def registration(request):
    name= None
    if request.user.is_authenticated:
        name=request.user.username
        return render(request, 'foodapp/index.html',{'name':name})
    return render(request, 'foodapp/registration.html',{'i':0})
    
def registered(request):
    name= None
    if request.user.is_authenticated:
        name=request.user.username
        return render(request, 'foodapp/index.html',{'name':name})
    reg=regdata()
    reg.name=request.POST.get('name')
    reg.email=request.POST.get('email')
    reg.pswrd=request.POST.get('password')
    pswrdcheck=request.POST.get('re_password')
    check=request.POST.get('agree-term')
    users = regdata.objects.filter(name=reg.name)
    if((len(reg.name)==0) or (len(reg.pswrd)==0) or (len(pswrdcheck)==0)):
        
        return render(request, 'foodapp/registration.html',{'i':1,'reg':reg,'pswrdcheck':pswrdcheck})
    elif (not(check)):

        return render(request, 'foodapp/registration.html',{'i':2,'reg':reg,'pswrdcheck':pswrdcheck})
    elif (pswrdcheck!=reg.pswrd):
        
        return render(request, 'foodapp/registration.html',{'i':3,'reg':reg,'pswrdcheck':pswrdcheck}) 

    elif users.exists():
        return render(request, 'foodapp/registration.html',{'i':4,'reg':reg,'pswrdcheck':pswrdcheck})
    user = User.objects.create_user(username=reg.name,email=reg.email,password=reg.pswrd)
    user.save()
    reg.save()

    return render(request, 'foodapp/registered.html',)

def logged(request):
    name= None
    if request.user.is_authenticated:
        name=request.user.username
        return render(request, 'foodapp/index.html',{'name':name})
    name=request.POST.get('name')
    pswrd=request.POST.get('pass')
    user = authenticate(request, username=name, password=pswrd)

    if (user is not None):
        login(request,user)
        return render(request, 'foodapp/logged.html')
        
    else:

       return render(request, 'foodapp/login.html',{'i':1})
    



def menu(request):
    food=fooditem.objects.all()
    
    if request.user.is_authenticated:
        activeuser=request.user
        name=activeuser.username
        
    else:
        return render(request, 'foodapp/login.html',{'i':0})
    foodid=request.POST.get('foodid')
    
    if foodid:
        
        if activeuser.cartitem_set.filter(id1=foodid):
            item=activeuser.cartitem_set.filter(id1=foodid)
            item.update(count=item[0].count+1)
            
        
        
            
        else:
            activeuser.cartitem_set.create(id1=foodid,count=1)
            
    
            
        return HttpResponseRedirect('/menu')
    
    return render(request, 'foodapp/menu.html',{'fooditem':food,'name':name,})

def loggedout(request):
    logout(request)
    return render(request, 'foodapp/loggedout.html')


def cart(request):
    
    
    name= None
    if request.user.is_authenticated:
        activeuser=request.user
        name=activeuser.username
    else:
        return render(request, 'foodapp/login.html',{'i':0})
    foodcart=activeuser.cartitem_set.all()
    food=fooditem.objects.all()

    foodid=request.POST.get('foodid')
    foodiddel=request.POST.get('foodiddel')
    if foodid:
        if activeuser.cartitem_set.filter(id1=foodid):
            item=activeuser.cartitem_set.filter(id1=foodid)
            item.update(count=item[0].count+1)
        
        
            
        else:
            activeuser.cartitem_set.create(id1=foodid,count=1)
    elif foodiddel:
        
        item=activeuser.cartitem_set.filter(id1=foodiddel)
        if (item[0].count>1):
            item.update(count=item[0].count-1)
            
        
            
        else:
            item.delete()  
            

            
        return HttpResponseRedirect('/cart')
    return render(request, 'foodapp/cart.html',{'fooditem':food,'name':name,'foodcart':foodcart})

def checkout(request):
    name= None
    m=0
    if request.user.is_authenticated:
        activeuser=request.user
        name=activeuser.username
    else:
        return render(request, 'foodapp/login.html',{'i':0})
    if request.POST.get('submit2'):
        if request.POST.get('choiceadr'):
            return HttpResponseRedirect('/payment')
        m=1 
        

        
    foodcart=activeuser.cartitem_set.all()
    food=fooditem.objects.all()
    price=0
    for i in food:
        for j in foodcart:
            if(i.id==j.id1):
                price+= (i.price*j.count)
    
    
    codecheck=request.POST.get('code')
    discounts=discount.objects.all()
    actualdisc=0
    if discounts:
        
        for i in discounts:
            if( codecheck == discounts.code):
                actualdisc=discounts.percentdisc
    pricediscounted=price-price*actualdisc/100
    existingaddress=activeuser.address_set.all()
    
    return render(request, 'foodapp/checkout.html',{'m':m,'name':name,'price':price,'discprice':pricediscounted,'existingaddress':existingaddress })




def createadr(request):
    name= None
    if request.user.is_authenticated:
        activeuser=request.user
        name=activeuser.username
    else:
        return render(request, 'foodapp/login.html',{'i':0})
    states=state.objects.all()
    
    statead=request.POST.get('state')
    city=request.POST.get('city')
    streetad=request.POST.get('streetad')
    pincode=request.POST.get('pincode')
    if statead and city and streetad and pincode:
        
        adr=activeuser.address_set.create(state=statead,city=city,streetad=streetad,pincode=pincode)
        adr.save()  
        return HttpResponseRedirect('/checkout')
    elif request.POST.get('submit'):
        i=1
    return render(request,'foodapp/createadr.html',{'name':name,'states':states,'i':i})
    
