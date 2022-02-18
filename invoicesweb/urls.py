from django.urls import path
from invoicesweb.views import all_invoices, new_invoice, edit_invoice, delete_invoice

urlpatterns = [
    path('all/', all_invoices, name="all_invoices"),
    path('new/', new_invoice, name="new_invoice"),
    path('edit/<int:id>/', edit_invoice, name="edit_invoice"),
    path('delete/<int:id>/', delete_invoice, name="delete_invoice"),
]
