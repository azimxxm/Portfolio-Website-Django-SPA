from django.contrib import admin
from .models import *

@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'age', 'work_type', 'birthday', 'phone', 'website', 'degree', 'freelance', 'emil', 'city' ]
    list_filter = ['work_type', 'degree', 'freelance']
    search_fields = ['name', 'age', 'work_type', 'emil', ]

@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'image', 'url', 'date_created']

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['id', 'firstName', 'lastName', 'phoneNumber', 'email', 'message']