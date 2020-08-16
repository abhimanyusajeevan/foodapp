from django.contrib import admin

from .models import regdata,fooditem,cartitem,address,state
# Register your models here.
admin.site.register(regdata)
admin.site.register(fooditem)
admin.site.register(cartitem)
admin.site.register(address)
admin.site.register(state)
