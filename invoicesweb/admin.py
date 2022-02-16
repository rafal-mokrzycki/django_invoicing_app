from django.contrib import admin
from .models import Film, DodatkoweInfo, Ocena, Aktor

# admin.site.register(Film)

@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    # fields = ["tytul", "opis", "rok"]
    # exclude = ["opis"]
    list_display = ["tytul", "imdb_rating", "rok"]
    list_filter = ("rok", "imdb_rating")
    search_fields = ("tytul", "opis")

admin.site.register(MoreInfo)
admin.site.register(Score)
admin.site.register(Actor)