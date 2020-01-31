from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect
from datetime import datetime
from utilisateurs.models import Users
from .forms import ConnexionForm

def connexion(request):
    form = ConnexionForm(request.POST or None)
    return render(request, 'connexion.html', locals())

def accueil(request):
    """ Retourne vers la page d'accueil de l'application """
    
    return render(request, 'accueil.html', {'date':datetime.now()})

def view_ajouter(request):
    pass

def view_modifier(request, matricule):
    pass

def view_supprimer(request, matricule):
    pass

def view_rechercher(request, matricule):
    pass

def afficher(request):
    pass
    # user = Users.objects.all()
    # return render(request, 'liste_utilisateurs', locals())