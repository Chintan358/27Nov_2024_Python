from django.contrib import admin

# Register your models here.
from myapp.models import *
# Register your models here.

class ProductList(admin.ModelAdmin):
    list_display = ('productname','price','qty','description','productImage')
   

admin.site.register(Category)
admin.site.register(Product,ProductList)
admin.site.register(Cart)
admin.site.register(UserAddress)
admin.site.register(UserOrder)
admin.site.register(OrderItems)
