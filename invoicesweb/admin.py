from django.contrib import admin
from .models import Invoice

# admin.site.register(Invoice)

@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    # fields = ["invoice_number", "opis", "contractor_tax_number"]
    # exclude = ["opis"]
    list_display = ["invoice_number", "contractor_tax_number"]
    list_filter = ("contractor_tax_number",)
    search_fields = ("invoice_number", "opis")

