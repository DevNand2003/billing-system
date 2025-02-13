from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Bill

@admin.register(Bill)
class BillAdmin(admin.ModelAdmin):
    list_display = ['invoice_number', 'company', 'total_amount', 'email', 'start_date', 'end_date']
