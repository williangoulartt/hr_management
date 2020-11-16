from django.db import models
from django.urls import reverse
from apps.employees.models import Employee


class OverTime(models.Model):
    reason = models.CharField(max_length=100,help_text='Reason')
    employee = models.ForeignKey(Employee,on_delete=models.PROTECT)
    hour = models.DecimalField(max_digits=5, decimal_places=2)

    def get_absolute_url(self):
        return reverse('update_employee', args=[self.employee.id])

    def __str__(self):
        return self.reason
