from django.urls import path
from . import views

urlpatterns = [
    path('connexion', views.connexion, name='connexion'),
    path('accueil', views.accueil, name='accueil'),
    path('ajouter', views.view_ajouter, name='ajouter_utilisateur'),
    path('modifier/<str:matricule>', views.view_modifier, name='modifier_utilisateur'),
    path('supprimer/<str:matricule>', views.view_supprimer),
    path('afficher', views.afficher, name='liste_utilisateurs'),
    path('rechercher/<str:matricule>', views.view_rechercher),
]