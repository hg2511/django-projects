from django.contrib import admin
from .models import CourseModel, TrainerModel, StudentModel
# Register your models here.

admin.site.register(CourseModel)
admin.site.register(TrainerModel)
admin.site.register(StudentModel)