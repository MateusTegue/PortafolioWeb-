from django.shortcuts import render

from .models import Project, Perfil

# Create your views here.


def home(request):
    perfil = Perfil.objects.all()
    return render(request, 'home.html', { 'perfil': perfil})



def Projects(request):
    projects = Project.objects.all()
    return render(request, 'projects.html', {'projects': projects})
