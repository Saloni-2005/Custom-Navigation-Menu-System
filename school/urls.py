from django.urls import path
from . import views

urlpatterns = [
    path('students/', views.student_list, name='students'),
    path('students/add/', views.student_add, name='add_student'),
    path('students/edit/<int:id>/', views.student_edit, name='edit_student'),
    path('students/delete/<int:id>/', views.student_delete, name='delete_student'),
    path('instructors/', views.instructor_list, name='instructors'),
    path('instructors/add', views.instructor_add, name='add_instructor'),
]