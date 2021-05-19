from django.db import models

# Create your models here.
class Covid_Test_Model(models.Model):
    gender_chooice = [
        ('Male', 'Male'),
        ('Female', 'Female')
    ]
    name = models.CharField(max_length=100, null=False)
    age = models.IntegerField(null=False)
    gender = models.CharField(max_length=20, choices=gender_chooice, default='Male', null=False)
    phone = models.CharField(max_length=15, null=False)
    email = models.EmailField(max_length=100, null=False)
    adhaar_no = models.CharField(max_length=16, null=False)
    address = models.TextField(null=False)
    date = models.DateField(null=False)
    Time = models.TimeField(auto_now=False, auto_now_add=False, null=False)

    def __str__(self) -> str:
        return self.name