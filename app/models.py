from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class CustomUser(User):
    profileImg=models.ImageField("Profile Image", upload_to='app/profileImage/', default='app/profileImage/profile.jpg')
    def __str__(self) -> str:
        return self.username