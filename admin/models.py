from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class CustomUser(AbstractUser):
    # Add any additional fields or properties you want for your user model
    # For example, you can add a profile picture field:
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)

    # Add any additional methods or customizations you want for your user model
    # For example, you can add a method to get the full name of the user:
    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'

    pass
