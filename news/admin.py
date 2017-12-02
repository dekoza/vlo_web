from django.contrib import admin

from .models import Entry


@admin.register(Entry)
class EntryAdmin(admin.ModelAdmin):
    date_hierarchy = 'pub_date'
    search_fields = ['title']
    list_filter = ['important']
    list_display = ['title', 'pub_date', 'important']

# dominik@kozaczko.info
