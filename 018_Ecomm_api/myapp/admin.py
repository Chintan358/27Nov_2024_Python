from django.contrib import admin

# Register your models here.
from myapp.models import *
# Register your models here.

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(UserAddress)
admin.site.register(UserOrder)
admin.site.register(OrderItems)
