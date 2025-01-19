from django.urls import path

from .views import formacion, formacion_detail

app_name = 'formacion'

urlpatterns = [
    path('', formacion, name='formacion'),
    path('<int:formacion_id>', formacion_detail, name='formacion_detail'),

]