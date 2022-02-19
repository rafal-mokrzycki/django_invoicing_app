from django.shortcuts import render, get_object_or_404, redirect
from .models import Invoice, Contractor
from .forms import InvoiceForm
from django.contrib.auth.decorators import login_required
from rest_framework import viewsets
from django.contrib.auth.models import User
from .serializers import UserSerializer, InvoiceSerializer, ContractorSerializer

class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class InvoiceView(viewsets.ModelViewSet):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer

class ContractorView(viewsets.ModelViewSet):
    queryset = Contractor.objects.all()
    serializer_class = ContractorSerializer

def all_invoices(request):
    all = Invoice.objects.all()
    return render(request, 'invoices.html', {'invoices': all})

@login_required
def new_invoice(request):
    form_invoice = InvoiceForm(request.POST or None, request.FILES or None)

    if form_invoice.is_valid():
        invoice = form_invoice.save(commit=False)
        invoice.save()
        return redirect(all_invoices)

    return render(request, 'invoice_form.html', {'form': form_invoice})

@login_required
def edit_invoice(request,invoice_number):
    invoice = get_object_or_404(Invoice, pk=id)

    form_invoice = InvoiceForm(request.POST or None, request.FILES or None, instance=invoice)


    if form_invoice.is_valid():
        invoice = form_invoice.save(commit=False)
        invoice.save()
        return redirect(all_invoices)

    return render(request, 'invoice_form.html', {'form': form_invoice})

@login_required
def delete_invoice(request,invoice_number):
    invoice = get_object_or_404(Invoice, pk=id)

    if request.method == "POST":
        invoice.delete()
        return redirect(all_invoices)

    return render(request, 'confirm.html', {'invoice': invoice})

# Create
# Read
# Update
# Delete