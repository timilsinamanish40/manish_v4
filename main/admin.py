from django.contrib import admin
from .models import Contact

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'message', 'created_at')  # Customize fields displayed
    search_fields = ('name', 'email')  # Add search functionality
    list_filter = ('created_at',)  # Filter by date