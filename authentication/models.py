from django.db import models
from django.contrib.auth.models import  AbstractUser

class User(AbstractUser):
# Create your models here.
    CREATOR = 'CREATOR'
    SUBSCRIBER = 'SUBSCRIBER'

    ROL_CHOICES = ((CREATOR, 'Createur'),
                   (SUBSCRIBER, 'Abonne'),
                   )
    profile_photo = models.ImageField(verbose_name='Photo de profil')
    role = models.CharField(max_length=30, choices=ROL_CHOICES, verbose_name='Role')