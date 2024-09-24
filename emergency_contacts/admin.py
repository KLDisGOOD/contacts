from django.contrib import admin
from .models import Contact

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'phone_number', 'id')
    search_fields = ('first_name', 'last_name', 'phone_number', 'id')
    ordering = ('id',)