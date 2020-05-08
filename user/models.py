from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from datetime import datetime
# Create your models here.


class UserDetail(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    country = models.CharField(max_length=100)
    image = models.ImageField(default='default.jpg', upload_to='profile_pic')
    created_on = models.DateTimeField(default=datetime.now(), blank=True)

    def __str__(self):
        return f'{self.user.username} details '

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)


class UserSocialMedia(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    facebook = models.CharField(max_length=35, blank=True)
    website = models.CharField(max_length=35, blank=True)
    twitter = models.CharField(max_length=35, blank=True)
    instagram = models.CharField(max_length=35, blank=True)
    youtube = models.CharField(max_length=35, blank=True)

    def __str__(self):
        return f'{self.user.username} social media'


class UserEducation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    school = models.CharField(max_length=100, blank=True)
    started = models.DateTimeField(blank=True)
    ended = models.DateTimeField(blank=True)
    degree = models.CharField(max_length=100, blank=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return f'{self.user.username} education'
