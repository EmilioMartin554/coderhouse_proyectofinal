from django.db import models
from django.db.models import Model
from ckeditor.fields import RichTextField
class blog(Model):
    post=RichTextField(null=True,blank=True)
    autor=models.CharField(max_length=50)
    titulo=models.CharField(max_length=400)
    subtitulo=models.CharField(max_length=300)
    descripcion=models.CharField(max_length=400)
    foto = models.ImageField(upload_to="images")
    fecha=models.DateTimeField(auto_now=True)
# Create your models here.
