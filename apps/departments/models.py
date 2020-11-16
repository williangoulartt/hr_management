from django.db import models
from django.urls import reverse
from apps.companies.models import Company


class Department(models.Model):
    name = models.CharField(max_length=10,help_text='Departament Name')
    company = models.ForeignKey(Company, on_delete=models.PROTECT)

    def get_absolute_url(self):
        return reverse('list_departments')

    def __str__(self):
        return self.name
