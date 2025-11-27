from django.contrib import admin
from .models import User
from .models import Product
# Register your models here.
# admin.site.register(User)

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock')
    list_filter = ('price',)
    search_fields = ('name',)

class PeopleAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')

admin.site.register(Product, ProductAdmin)
admin.site.register(User, PeopleAdmin)