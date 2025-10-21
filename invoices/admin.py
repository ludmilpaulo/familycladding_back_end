from django.contrib import admin
from .models import Invoice, InvoiceItem

class InvoiceItemInline(admin.TabularInline):
    model = InvoiceItem
    extra = 1

@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    list_display = ['invoice_number', 'client_name', 'client_email', 'total_amount', 'status', 'due_date', 'created_at']
    list_filter = ['status', 'created_at', 'due_date']
    search_fields = ['invoice_number', 'client_name', 'client_email']
    readonly_fields = ['invoice_number', 'tax_amount', 'total_amount', 'created_at', 'updated_at', 'sent_at', 'paid_at']
    inlines = [InvoiceItemInline]
    
    fieldsets = (
        ('Invoice Information', {
            'fields': ('invoice_number', 'status', 'issue_date', 'due_date')
        }),
        ('Client Information', {
            'fields': ('client_name', 'client_email', 'client_address', 'client_phone')
        }),
        ('Financial Details', {
            'fields': ('subtotal', 'tax_rate', 'tax_amount', 'total_amount')
        }),
        ('Additional Information', {
            'fields': ('notes', 'terms_conditions')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at', 'sent_at', 'paid_at'),
            'classes': ('collapse',)
        }),
    )
