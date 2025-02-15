from django.contrib import admin
from .models import Menu

@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price', 'is_available')
    list_filter = ('is_available',)
    search_fields = ('name', 'description')
