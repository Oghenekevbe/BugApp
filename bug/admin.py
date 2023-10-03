from django.contrib import admin
from .models import Bug
# Register your models here.

@admin.register(Bug)
class BugAdmin(admin.ModelAdmin):
    '''Admin View for '''

    list_display = ('bug_type', 'status', 'report_date')
    list_filter = ('report_date',)
