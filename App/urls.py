from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import homepage,DepartmentListView, DepartmentCreateView, DepartmentDetailView, DepartmentUpdateView, DepartmentDeleteView,RoleListView,RoleCreateView,RoleDeleteView,RoleDetailView,RoleUpdateView

urlpatterns = [
    path('home/', homepage, name='home'),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name="logout"),    
    path('department_list/', DepartmentListView.as_view(), name='department_list'),
    path('department_create/', DepartmentCreateView.as_view(), name='department_create_form'),
    path('department_detail/<int:pk>/',DepartmentDetailView.as_view() , name='department_detail'),
    path('update/<int:pk>',DepartmentUpdateView.as_view() , name='department_update'),
    path('delete/<int:pk>', DepartmentDeleteView.as_view(), name='department_delete'),
    path('role_list/',RoleListView.as_view(),name="role_list"),
    path('role_create/',RoleCreateView.as_view(),name="role_create_form"),
    path('role_detail/<int:pk>/',RoleDetailView.as_view(),name="role_detail"),
    path('role_update/<int:pk>/',RoleUpdateView.as_view(),name="role_update"),
    path('role_delete/<int:pk>/',RoleDeleteView.as_view(),name="role_delete"),
]
