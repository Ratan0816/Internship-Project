from django.shortcuts import render, get_object_or_404, redirect
from .models import Department, Employee, Role
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView
from django.views.generic.edit import UpdateView, DeleteView
from django.contrib.auth.models import Permission
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .forms import EmployeeForm


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


@login_required
def assign_permission_to_user(request):
    try:
        employee_user = get_object_or_404(Employee, username="user1")
        permission = Permission.objects.get(codename="can_add_employee")
        employee_user.user_permissions.add(permission)

        employee_user2 = get_object_or_404(Employee, username="user2")
        permission2 = Permission.objects.get(codename="can_update_employee")
        employee_user2.user_permissions.add(permission2)

        return HttpResponse("Permissions added successfully.")
    except Exception as e:
        return HttpResponse(f"Error while assigning permissions: {e}")


def EmployeeCreateView(request):
    if request.method == 'POST':
        employee_form = EmployeeForm(request.POST)
        if employee_form.is_valid():
            employee = employee_form.save(commit=False)
            employee.username = employee_form.cleaned_data['f_name1']  
            employee.set_password(employee_form.cleaned_data['password1'])  
            employee.save()
            return redirect('employee_list')
    
    else:
        employee_form = EmployeeForm()
    
    return render(request,'employee_create_form.html',{'employee_form':employee_form})


class EmployeeListView(ListView):
    model=Employee
    template_name='employee_list.html'
    context_object_name='employees'

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return Employee.objects.filter(f_name1__icontains=query) 
        return Employee.objects.all()

class EmployeeDetailView(DetailView):
    model = Employee
    template_name = 'employee_detail.html'
    context_object_name = 'employee'


class EmployeeUpdateView(UpdateView):
    model = Employee
    template_name = 'employee_update.html'
    fields = ['f_name1', 'l_name1', 'email1', 'phone1', 'address1']
    success_url = reverse_lazy('employee_list')


class EmployeeDeleteView(DeleteView):
    model = Employee
    template_name = 'employee_delete.html'
    success_url = reverse_lazy('employee_list')

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
