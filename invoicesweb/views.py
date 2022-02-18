from django.shortcuts import render, get_object_or_404, redirect
from .models import Invoice, MoreInfo, Score, Contractor
from .forms import InvoiceForm, MoreInfoForm, ScoreForm
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
    form_more = MoreInfoForm(request.POST or None)

    if all((form_invoice.is_valid(), form_more.is_valid())):
        invoice = form_invoice.save(commit=False)
        more = form_more.save()
        invoice.more = more
        invoice.save()
        return redirect(all_invoices)

    return render(request, 'invoice_form.html', {'form': form_invoice, 'form_more': form_more, 'scores': None, 'form_score': None, 'new': True})

@login_required
def edit_invoice(request, id):
    invoice = get_object_or_404(Invoice, pk=id)
    scores = Score.objects.filter(invoice=invoice)
    actors = invoice.actors.all()

    try:
        more = MoreInfo.objects.get(invoice=invoice.id)
    except MoreInfo.DoesNotExist:
        more = None

    form_invoice = InvoiceForm(request.POST or None, request.FILES or None, instance=invoice)
    form_more = MoreInfoForm(request.POST or None, instance=more)
    form_score = ScoreForm(None)

    if request.method == 'POST':
        if 'gwiazdki' in request.POST:
            score = form_score.save(commit=False)
            score.invoice = invoice
            score.save()

    if all((form_invoice.is_valid(), form_more.is_valid())):
        invoice = form_invoice.save(commit=False)
        more = more.save()
        invoice.more = more
        invoice.save()
        return redirect(all_invoices)

    return render(request, 'invoice_form.html', {'form': form_invoice, 'form_more': form_more, 'scores': scores, 'form_score': form_score, 'new': False})

@login_required
def delete_invoice(request, id):
    invoice = get_object_or_404(Invoice, pk=id)

    if request.method == "POST":
        invoice.delete()
        return redirect(all_invoices)

    return render(request, 'confirm.html', {'invoice': invoice})

# Create
# Read
# Update
# Delete