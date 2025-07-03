from django.contrib import admin
from myapp.models import *

# Register your models here.

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(UserAddress)
admin.site.register(UserOrder)
admin.site.register(OrderItems)

