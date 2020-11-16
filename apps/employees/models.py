from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

from apps.departments.models import Department
from apps.companies.models import Company


class Employee(models.Model):
    name = models.CharField(max_length=100,help_text='Employee Name')
    user = models.OneToOneField(User,on_delete=models.PROTECT)
    departments = models.ManyToManyField(Department)
    company = models.ForeignKey(
        Company,on_delete=models.PROTECT,blank=True,null=True)

    def get_absolute_url(self):
        return reverse('list_employees')

    def __str__(self):
        return self.name
