from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

class Profile(models.Model):
    id = models.AutoField(primary_key = True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    otp = models.CharField(max_length = 6)
    is_verified = models.BooleanField(default = False)
    picture = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100, null=True)
    data = models.TextField(blank=True, null=True)
    in_hash = models.CharField(max_length = 8)
    
    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

class Image(models.Model):
    id = models.AutoField(primary_key = True)
    image = models.ImageField()
    hashcode = models.CharField(max_length = 200)

    def __str__(self):
        return self.hashcode