from django.db import models
# from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from .managers import CustomUserManager



class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(_("email address"), unique=True)
    owner = models.BooleanField(default=False)
    manager = models.BooleanField(default=False)
    password = models.CharField(max_length=100)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email
 


class Property(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    description = models.TextField()
    manager =  models.ManyToManyField(CustomUser, related_name='properties')
    owner = models.ManyToManyField(CustomUser, related_name='propertieso')

    def __str__(self):
        return self.name




class PropertyUnit(models.Model):
    unit_number = models.CharField(max_length=10)
    floor = models.PositiveIntegerField()
    size = models.DecimalField(max_digits=5, decimal_places=2)
    rent = models.DecimalField(max_digits=8, decimal_places=2)
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='units')

    def __str__(self):
        return f"{self.unit_number} - {self.property.name}"


