from ckeditor_uploader.fields import RichTextUploadingField
from ckeditor.fields import RichTextField
from django.db import models
from django.contrib.auth.models import User


# Create your models here.

STATUS = (
    (0,"Draft"),
    (1,"Publish")
)

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Categories"    
    

class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='blog_posts')
    updated_on = models.DateTimeField(auto_now= True)
    content = RichTextUploadingField() # CKEditor Rich Text Field
    category = models.ManyToManyField(Category, related_name="categories")
    created_on = models.DateTimeField(auto_now_add=False, editable=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title
    
class LinkedInAuthToken(models.Model):
    """
    Modelo para almacenar el token de acceso de LinkedIn.
    """
    access_token = models.CharField(max_length=512, unique=True, help_text="Token de acceso para la API de LinkedIn.")
    expires_in = models.IntegerField(help_text="Tiempo de vida del token en segundos.")
    created_at = models.DateTimeField(auto_now_add=True)
    profile_urn = models.CharField(max_length=128, help_text="URN del perfil de LinkedIn para publicar.")

    def __str__(self):
        return self.profile_urn
    




