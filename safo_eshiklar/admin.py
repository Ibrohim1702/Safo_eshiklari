from django.contrib import admin

from regis.models import User
from safo_eshiklar.models import Category, Products, Contact

# Register your models here.


admin.site.register(User)
admin.site.register(Category)
admin.site.register(Products)
admin.site.register(Contact)
