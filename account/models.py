from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class AddressBookUser(AbstractUser):
    """
    """

    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    contacts = models.ManyToManyField('contact.Contact', blank=True)

