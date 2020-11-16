from django.urls import reverse
from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=100,help_text='Company Name')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('home')