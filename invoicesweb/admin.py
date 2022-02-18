from django.contrib import admin
from .models import Invoice

# admin.site.register(Invoice)

@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    list_display = [ "issue_date"]
    # list_filter = ("issue_date","invoice_number")
    # search_fields = ("invoice_number", "issue_date")

