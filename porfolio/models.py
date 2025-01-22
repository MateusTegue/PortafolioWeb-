from django.db import models

# Create your models here.


class Perfil(models.Model):
    imagen = models.ImageField(upload_to='porfolio/imagesPerfil/')
    nombre = models.CharField(max_length=50)
    perfilOcupaciona = models.CharField(max_length=100)
    curriculum = models.FileField(upload_to='porfolio/curriculums/')
    descripcion = models.TextField()


class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='porfolio/images/')
    url = models.URLField(blank=True)


