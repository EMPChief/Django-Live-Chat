from django.db import models
from django.utils.text import slugify
import random
from django.contrib.auth.models import User
from django.utils.text import slugify  # Add this import statement

class Room(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)

    def generate_slug(self):
        number = random.randint(100000, 999999)
        return f"{slugify(self.name)}-{number}"

    def save(self, *args, **kwargs):
        if self.pk is not None:
            existing_obj = Room.objects.get(pk=self.pk)
            if existing_obj.name != self.name:
                self.slug = self.generate_slug()
        else:
            self.slug = self.generate_slug()

        while Room.objects.filter(slug=self.slug).exclude(pk=self.pk).exists():
            self.slug = self.generate_slug()

        super(Room, self).save(*args, **kwargs)



class Message(models.Model):
    room = models.ForeignKey(Room, related_name='messages', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='messages', on_delete=models.CASCADE)
    content = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('date_added',)