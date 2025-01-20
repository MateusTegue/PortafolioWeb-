from django.shortcuts import render

from .models import Project, Perfil

# Create your views here.


def home(request):
    projects = Project.objects.all()
    perfil = Perfil.objects.all()
    return render(request, 'home.html', {'projects': projects, 'perfil': perfil})
