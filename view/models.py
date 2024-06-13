from django.db import models
from django.urls import reverse
# Create your models here.
class School(models.Model):
    school_name=models.CharField(max_length=100)
    school_principal=models.CharField(max_length=100)
    school_location=models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.school_name
    
    def get_absolute_url(self):
        return reverse('detail',kwargs={'pk':self.pk})
        
class Student(models.Model):
    student_name=models.CharField(max_length=100)
    student_age=models.IntegerField()
    school_name=models.ForeignKey(School,on_delete=models.CASCADE,related_name='students')
