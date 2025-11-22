from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path("courses/", views.course_list, name="course_list"),
    path("trainers/", views.trainer_list, name="trainer_list"),
    path("students/", views.student_list, name="student_list"),
    # path("", views.home, name="home"),
]