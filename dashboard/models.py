from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from PIL import Image

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, unique=True, primary_key=True, related_name="profile", on_delete=models.CASCADE)
    rank = models.IntegerField(default=0)
    xp = models.IntegerField(default=0)
    wins = models.IntegerField(default=0)
    losses = models.IntegerField(default=0)
    wlratio = models.DecimalField(default=0, max_digits=6, decimal_places=2)
    kills = models.IntegerField(default=0)
    deaths = models.IntegerField(default=0)
    kdratio = models.DecimalField(default=0, max_digits=6, decimal_places=2)
    image = models.ImageField(default='default.png', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance=None, created=False, **kwargs):
    if created:
        Profile.objects.get_or_create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
