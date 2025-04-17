from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
    """
    Custom User model that extends the default Django User model.
    """
    # Add any additional fields or methods here if needed
    pass

class Location(models.Model):
    """
    Model to store geolocation data.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='location')
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Location({self.latitude}, {self.longitude}) for {self.user.username} at {self.created_at}"
        
    def save(self, *args, **kwargs):
        # Round latitude and longitude to 6 decimal places before saving
        self.latitude = round(float(self.latitude), 6)
        self.longitude = round(float(self.longitude), 6)
        super().save(*args, **kwargs)