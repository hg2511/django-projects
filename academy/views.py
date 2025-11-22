from django.shortcuts import render
from .models import CourseModel, TrainerModel, StudentModel

# Create your views here.


def course_list(request):
    # fetching all the course list
    courses = CourseModel.objects.all()
    context = {
        "courses" : courses
    }
    return render(request, "courses.html", context)


def trainer_list(request):
    # fetching all the course list
    trainer = TrainerModel.objects.all()
    context = {
        "trainers" : trainer
    }
    return render(request, "trainers.html", context)


def student_list(request):
    # fetching all the course list
    students = StudentModel.objects.all()
    context = {
        "students" : students
    }
    return render(request, "students.html", context)