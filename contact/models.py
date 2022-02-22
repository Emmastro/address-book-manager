from django.db import models


class Contact(models.Model):
    """
    """

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    email = models.EmailField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

