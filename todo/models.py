from django.db import models

# Create your models here.
class student(models.Model):
    student_id = models.AutoField(primary_key=True)
    student_name = models.CharField(max_length=50)
    student_email = models.EmailField(max_length=180)
    student_password = models.CharField(max_length=180)