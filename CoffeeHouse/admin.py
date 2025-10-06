from django.contrib import admin
from .models import *

admin.site.register(Clients)
admin.site.register(Positions)
admin.site.register(Employees)
admin.site.register(CategoriesOfProducts)
admin.site.register(Products)
admin.site.register(Orders)
admin.site.register(OrderDetails)

