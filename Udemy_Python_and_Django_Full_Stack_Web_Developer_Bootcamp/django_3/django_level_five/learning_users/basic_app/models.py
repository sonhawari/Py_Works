from django.db import models
from django.contrib.auth.models import User



class UserProfileInfo(models.Model):

    user = models.OneToOneField(user)

    portfolio = models.URLField(blank=True)

    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)

    def __str__(self):
        return self.user.username
