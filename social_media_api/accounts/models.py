from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    bio = models.TextField(blank=True, null=True)  # Optional bio for the user
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)  # Profile picture field
    # followers: Many-to-Many relationship with itself (not symmetrical)
    followers = models.ManyToManyField(
        'self', 
        symmetrical=False,  # Not symmetrical, as one user can follow another without being followed back
        blank=True,  # Allow users to have no followers
        related_name='following',  # Allows access to the list of users the current user is following
    )

    def __str__(self):
        return self.username  # Return the username when the user instance is printed
