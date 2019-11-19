from django.contrib import admin
from .models import Invoice

# Register your models here.
admin.site.site_header = 'Boxus - Invoice and Inventory Management'
admin.site.register(Invoice)
