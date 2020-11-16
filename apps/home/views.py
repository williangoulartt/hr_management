from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from apps.employees.models import Employee


@login_required
def home(request):
    data = {}
    data['user'] = request.user
    template_name = 'home/index.html'
    return render(request,template_name,data)
