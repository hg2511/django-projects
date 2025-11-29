from django.db import models
from uuid import uuid4

# Create your models here.

class CourseModel(models.Model):
    course_name = models.CharField(max_length=50)
    description = models.CharField(max_length=250)
    duration_in_week = models.DateTimeField()
    course_image = models.ImageField(upload_to="course_image/")

    def __str__(self):
        return f"{self.course_name}"

class TrainerModel(models.Model):
    trainer_id = models.UUIDField(uuid4)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100, unique=True)
    expertise = models.CharField()
    trainer_photo = models.ImageField(upload_to="trainer_photo/")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    def trainer_name(self):
        return f'{self.first_name} {self.last_name}'

class StudentModel(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    is_active = models.BooleanField(default=True)
    enrolled_course = models.ForeignKey(CourseModel, on_delete=models.SET_NULL, null=True)
    trainer = models.ForeignKey(TrainerModel, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def student_name(self):
        return f"{self.first_name} {self.last_name}"

