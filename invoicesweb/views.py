from django.shortcuts import render, get_object_or_404, redirect
from .models import Invoice, MoreInfo, Score
from .forms import InvoiceForm, MoreInfoForm, ScoreForm
from django.contrib.auth.decorators import login_required
from rest_framework import viewsets
from django.contrib.auth.models import User
from .serializers import UserSerializer, InvoiceSerializer

class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class InvoiceView(viewsets.ModelViewSet):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer


def wszystkie_invoices(request):
    wszystkie = Invoice.objects.all()
    return render(request, 'invoices.html', {'invoices': wszystkie})

@login_required
def new_invoice(request):
    form_invoice = InvoiceForm(request.POST or None, request.FILES or None)
    form_dodatkowe = MoreInfoForm(request.POST or None)

    if all((form_invoice.is_valid(), form_more.is_valid())):
        invoice = form_invoice.save(commit=False)
        more = form_more.save()
        invoice.more = more
        invoice.save()
        return redirect(wszystkie_invoices)

    return render(request, 'invoice_form.html', {'form': form_invoice, 'form_dodatkowe': form_dodatkowe, 'oceny': None, 'form_ocena': None, 'nowy': True})

@login_required
def edit_invoice(request, id):
    invoice = get_object_or_404(Invoice, pk=id)
    scores = Score.objects.filter(invoice=invoice)
    actors = invoice.actors.all()

    try:
        dodatkowe = MoreInfo.objects.get(invoice=invoice.id)
    except MoreInfo.DoesNotExist:
        dodatkowe = None

    form_invoice = InvoiceForm(request.POST or None, request.FILES or None, instance=invoice)
    form_dodatkowe = MoreInfoForm(request.POST or None, instance=dodatkowe)
    form_ocena = ScoreForm(None)

    if request.method == 'POST':
        if 'gwiazdki' in request.POST:
            ocena = form_ocena.save(commit=False)
            ocena.invoice = invoice
            ocena.save()

    if all((form_invoice.is_valid(), form_dodatkowe.is_valid())):
        invoice = form_invoice.save(commit=False)
        more = more.save()
        invoice.more = more
        invoice.save()
        return redirect(wszystkie_invoices)

    return render(request, 'invoice_form.html', {'form': form_invoice, 'form_more': form_dodatkowe, 'scores': scores, 'form_score': form_score, 'new': False})

@login_required
def delete_invoice(request, id):
    invoice = get_object_or_404(Invoice, pk=id)

    if request.method == "POST":
        invoice.delete()
        return redirect(wszystkie_invoices)

    return render(request, 'confirm.html', {'invoice': invoice})

# Create
# Read
# Update
# Delete