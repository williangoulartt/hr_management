from django.forms import ModelForm
from .models import OverTime
from apps.employees.models import Employee


class OverTimeForm(ModelForm):
    def __init__(self, user, *args, **kwargs):
        super(OverTimeForm, self).__init__(*args, **kwargs)
        self.fields['employee'].queryset = Employee.objects.filter(
            company=user.employee.company)

    class Meta:
        model = OverTime
        fields = ['reason', 'employee', 'hour']
