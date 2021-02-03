from django.contrib import admin

# Register your models here.
from .models import MenuItem, Category, OrderModel

# Register your models here.
admin.site.register(MenuItem)
admin.site.register(Category)
admin.site.register(OrderModel)