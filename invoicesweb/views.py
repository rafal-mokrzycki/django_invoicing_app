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

class FilmView(viewsets.ModelViewSet):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer


def wszystkie_filmy(request):
    wszystkie = Invoice.objects.all()
    return render(request, 'filmy.html', {'filmy': wszystkie})

@login_required
def nowy_film(request):
    form_film = InvoiceForm(request.POST or None, request.FILES or None)
    form_dodatkowe = MoreInfoForm(request.POST or None)

    if all((form_film.is_valid(), form_more.is_valid())):
        film = form_invoice.save(commit=False)
        more = form_more.save()
        invoice.more = more
        invoice.save()
        return redirect(wszystkie_filmy)

    return render(request, 'film_form.html', {'form': form_film, 'form_dodatkowe': form_dodatkowe, 'oceny': None, 'form_ocena': None, 'nowy': True})

@login_required
def edytuj_film(request, id):
    film = get_object_or_404(Invoice, pk=id)
    oceny = Score.objects.filter(film=film)
    aktorzy = film.aktorzy.all()

    try:
        dodatkowe = MoreInfo.objects.get(film=film.id)
    except MoreInfo.DoesNotExist:
        dodatkowe = None

    form_film = InvoiceForm(request.POST or None, request.FILES or None, instance=film)
    form_dodatkowe = MoreInfoForm(request.POST or None, instance=dodatkowe)
    form_ocena = ScoreForm(None)

    if request.method == 'POST':
        if 'gwiazdki' in request.POST:
            ocena = form_ocena.save(commit=False)
            ocena.film = film
            ocena.save()

    if all((form_film.is_valid(), form_dodatkowe.is_valid())):
        film = form_film.save(commit=False)
        more = more.save()
        film.more = more
        film.save()
        return redirect(wszystkie_filmy)

    return render(request, 'film_form.html', {'form': form_film, 'form_dodatkowe': form_dodatkowe, 'oceny': oceny, 'form_ocena': form_ocena, 'nowy': False})

@login_required
def usun_film(request, id):
    film = get_object_or_404(Invoice, pk=id)

    if request.method == "POST":
        film.delete()
        return redirect(wszystkie_filmy)

    return render(request, 'potwierdz.html', {'film': film})

# Create
# Read
# Update
# Delete