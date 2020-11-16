from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, DeleteView, CreateView
from .models import OverTime
from .forms import OverTimeForm


class OverTimeCreate(CreateView):
    model = OverTime
    form_class = OverTimeForm

    def get_form_kwargs(self):
        kwargs = super(OverTimeCreate, self).get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs


class OverTimeList(ListView):
    model = OverTime

    def get_queryset(self):
        logged_company = self.request.user.employee.company
        return OverTime.objects.filter(
            employee__company=logged_company)


class OverTimeEdit(UpdateView):
    model = OverTime
    form_class = OverTimeForm

    def get_form_kwargs(self):
        kwargs = super(OverTimeEdit, self).get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs


class OverTimeDelete(DeleteView):
    model = OverTime
    success_url = reverse_lazy('list_overtime')