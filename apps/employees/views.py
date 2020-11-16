from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views.generic.edit import DeleteView,UpdateView
from django.views.generic import ListView,CreateView
from .models import Employee


class EmployeesList(ListView):
    model = Employee

    def get_queryset(self,  **kwargs):
        company_logged = self.request.user.employee.company
        return Employee.objects.filter(company=company_logged)


class EmployeeCreate(CreateView):
    model = Employee
    fields = '__all__'

    def form_valid(self, form):
        # Next line : Create the instance of object but don't save,just keeping on temporary memory.
        employee = form.save(commit=False)
        username = employee.name.split(' ')[0] + employee.name.split(' ')[1]
        employee.company = self.request.user.employee.company
        employee.user = User.objects.create(username=username)
        employee.save()
        return super(EmployeeCreate, self).form_valid(form)


class EmployeeDelete(DeleteView):
    model = Employee
    success_url = reverse_lazy('list_employees')


class EmployeeUpdate(UpdateView):
    model = Employee
    fields = '__all__'
