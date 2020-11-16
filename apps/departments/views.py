from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.views.generic.list import ListView
from .models import Department
from django.urls import reverse_lazy


class DepartmentCreate(CreateView):
    model = Department
    fields = '__all__'

    def form_valid(self, form):
        departament = form.save(commit=False)
        departament.company = self.request.user.employee.company
        departament.save()
        return super(DepartmentCreate, self).form_valid(form)


class DepartmentUpdate(UpdateView):
    model = Department
    fields = '__all__'
    template_name_suffix = '_update_form'


class DepartmentDelete(DeleteView):
        model = Department
        success_url = reverse_lazy('list_departament')


class DepartmentList(ListView):
    model = Department

    def get_queryset(self):
        company_logged = self.request.user.employee.company
        return Department.objects.filter(company=company_logged)
