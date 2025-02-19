from django.shortcuts import render, get_object_or_404, redirect
from .models import Department, Role
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView
from django.views.generic.edit import UpdateView, DeleteView
from django.contrib.auth.models import Permission
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse


def homepage(request):
    return render(request, 'home.html')


def login(request):
    return render(request, 'login.html')


class DepartmentListView(ListView):
    model = Department
    template_name = 'department_list.html'
    context_object_name = 'departments'

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return Department.objects.filter(name__icontains=query)
        return Department.objects.all()


class DepartmentCreateView(CreateView):
    model = Department
    template_name = 'department_create_form.html'
    fields = ['name', 'description']
    success_url = reverse_lazy('department_list')


class DepartmentDetailView(DetailView):
    model = Department
    template_name = 'department_detail.html'
    context_object_name = 'department'


class DepartmentUpdateView(UpdateView):
    model = Department
    template_name = 'department_update.html'
    fields = ['name', 'description']
    success_url = reverse_lazy('department_list')


class DepartmentDeleteView(DeleteView):
    model = Department
    template_name = 'department_delete.html'
    success_url = reverse_lazy('department_list')


class RoleListView(ListView):
    model = Role
    template_name = 'role_list.html'
    context_object_name = 'roles'

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return Role.objects.filter(name__icontains=query)
        return Role.objects.all()


class RoleCreateView(CreateView):
    model = Role
    template_name = 'role_create_form.html'
    fields = ['r_name', 'r_description']
    success_url = reverse_lazy('role_list')


class RoleDetailView(DetailView):
    model = Role
    template_name = 'role_detail.html'
    context_object_name = 'role'


class RoleUpdateView(UpdateView):
    model = Role
    template_name = 'role_update.html'
    fields = ['r_name', 'r_description']
    success_url = reverse_lazy('role_list')


class RoleDeleteView(DeleteView):
    model = Role
    template_name = 'role_delete.html'
    success_url = reverse_lazy('role_list')
