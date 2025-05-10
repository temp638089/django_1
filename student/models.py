from django.db import models


class student(models.Model):
    DEPARTMENT_CHOICES = [
        ('Bsc','Bsc'),
        ('B.Com','B.Com'),
        ('Bba','Bba')
    ]
    name=models.CharField(max_length=255,null=True)
    email = models.EmailField(unique=True, null=True, blank=True)
    deaprtment=models.CharField(max_length=255,choices=DEPARTMENT_CHOICES)
    grade=models.CharField(max_length=2,null=True)
    mark=models.IntegerField(default=0)
    image = models.ImageField(upload_to='student_images/', null=True, blank=True)

    def __str__(self):
        return self.name
