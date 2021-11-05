from django.db import models

# Create your models here.
class Teacher(models.Model):

     name = models.CharField(max_length=100)
     email = models.EmailField
     img = models.CharField(max_length=250)
     created_at = models.DateTimeField(auto_now_add=True)

     def __str__(self):
         return self.name

class Student(models.Model):

    name = models.CharField(max_length=100)
    email = models.EmailField
    img = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']             