from django.contrib import admin
from LibraryApp import  models
# Register your models here.

admin.site.register(models.Auther)
admin.site.register(models.Category)
admin.site.register(models.Book)
admin.site.register(models.Student)
admin.site.register(models.Issued_Book)
