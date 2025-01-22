from django.shortcuts import render, get_object_or_404

from .models import Formacion
# Create your views here.


def formacion(request):
    formaciones = Formacion.objects.all().order_by('-date')
    return render(request, 'formacion.html' , {'formaciones': formaciones})  


def formacion_detail(request, formacion_id):
    formacion = get_object_or_404(Formacion, pk=formacion_id)
    return render(request, 'formacion_detail.html', {'formacion': formacion})
