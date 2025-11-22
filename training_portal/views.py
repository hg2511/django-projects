from django.http import HttpResponse
from academy.models import CourseModel, TrainerModel, StudentModel
from django.shortcuts import render




def home(request):
    # fetching all the data here 
    courses = CourseModel.objects.all().count()
    trainer = TrainerModel.objects.all().count()
    students = StudentModel.objects.all().count()

    context = {
        'courses' : courses,
        'trainers' : trainer,
        'students' : students
    }
    return render(request, 'home.html', context)




# def course_list(request):
#     courses = CourseModel.objects.all()
#     return render(request, "academy/courses.html", {"courses": courses})