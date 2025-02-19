from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Employee

class EmployeeForm(UserCreationForm):
    class Meta:
        model = Employee
        fields = [ 'f_name1', 'l_name1', 'email1', 'phone1', 'address1', 'password1', 'password2']
        
    
    def __init__(self, *args, **kwargs):
        super(EmployeeForm, self).__init__(*args, **kwargs)
        
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})
        
        self.fields['password1'].widget.attrs.update({'maxlength': '100'})
        self.fields['password2'].widget.attrs.update({'maxlength': '100'})