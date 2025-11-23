from django.shortcuts import render, redirect, get_object_or_404
from .models import Student, Instructor
from .forms import StudentForm, InstructorForm

# Create your views here.

def student_list(request):
    students = Student.objects.all()
    return render(request, 'students/list.html', {'students': students})

def student_add(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('students')
    else:
        form = StudentForm()
    return render(request, 'students/form.html', {'form': form, 'title':"Add Student"})

def student_edit(request, id):
    student = get_object_or_404(Student, id=id)
    form = StudentForm(request.POST or None, instance=student)
    if form.is_valid():
        form.save()
        return redirect('students')
    return render(request, 'students/form.html', {'form': form, 'title':"Edit Student"})

def student_delete(request, id):
    student = get_object_or_404(Student, id=id)
    if request.method == "POST":
        student.delete()
        return redirect('students')
    return render(request, 'students/delete_confirm.html', {'student': student})


def instructor_list(request):
    students = Instructor.objects.all()
    return render(request, 'instructors/list.html', {'students': students})

def instructor_add(request):
    if request.method == "POST":
        form = InstructorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('instructor')
    else:
        form = InstructorForm()
    return render(request, 'instructors/form.html', {'form': form, 'title':"Add Instructor"})
