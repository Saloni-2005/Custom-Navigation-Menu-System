from django import forms
from .models import Student, Instructor

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'age', 'grade']

class InstructorForm(forms.ModelForm):
    class Meta :
        model = Instructor
        fields = ['name', 'course', 'experience']