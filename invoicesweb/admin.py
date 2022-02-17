from django.contrib import admin
from .models import Invoice, MoreInfo, Score, Actor

# admin.site.register(Invoice)

@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    # fields = ["invoice_number", "opis", "contractor_tax_number"]
    # exclude = ["opis"]
    list_display = ["invoice_number", "imdb_rating", "contractor_tax_number"]
    list_filter = ("contractor_tax_number", "imdb_rating")
    search_fields = ("invoice_number", "opis")

admin.site.register(MoreInfo)
admin.site.register(Score)
admin.site.register(Actor)