from .models import state
def stateinit():    
    Totalstates="Andhra Pradesh,Arunachal Pradesh,Assam,Bihar,Chhattisgarh,Goa,Gujarat,Haryana,Himachal Pradesh,Jammu and Kashmir,Jharkhand,Karnataka,Kerala,Madhya Pradesh,Maharashtra,Manipur,Meghalaya,Mizoram,Nagaland,Odisha,Punjab,Rajasthan,Sikkim,Tamil Nadu,Telangana,Tripura,Uttar Pradesh,Uttarakhand,West Bengal,Andaman and Nicobar,Chandigarh,Dadra and Nagar Haveli,Daman and Diu,Lakshadweep,Delhi,Puducherry"
    statename=''
    istate=state()
    for i in Totalstates:
        if i != ',':
            statename+=i
        else:
            
            istate.state=statename
            istate.save()

    istate.state=statename
    istate.save()