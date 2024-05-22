from django.contrib import admin
from imsApp.models import *
# Register your models here.
admin.site.register(CompanyInfo)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Stock)
admin.site.register(Invoice)
admin.site.register(Invoice_Item)

