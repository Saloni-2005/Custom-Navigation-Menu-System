from django.urls import path
from . import views

urlpatterns = [
    path('', views.student_list, name='students'),
    path('add/', views.student_add, name='add_student'),
    path('edit/<int:id>/', views.student_edit, name='edit_student'),
    path('delete/<int:id>/', views.student_delete, name='delete_student'),
]