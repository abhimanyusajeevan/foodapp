from django.contrib import admin

from .models import regdata,fooditem,cartitem,address,state,discount,order,indvdl_order
# Register your models here.
admin.site.register(regdata)
admin.site.register(fooditem)
admin.site.register(cartitem)
admin.site.register(address)
admin.site.register(state)
admin.site.register(discount)
admin.site.register(order)
admin.site.register(indvdl_order)

