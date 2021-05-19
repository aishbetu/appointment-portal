from django.db import models

# Create your models here.
class AppointmentModel(models.Model):
    doctor_list = [
        ('Dr. Reshma Madan, OPD', 'Dr. Reshma OPD'),
        ('Dr. Shivangi, Cardiologist', 'Dr. Shivangi Cardiologist'),
        ('Dr. Raghav Dixit, Neurologist', 'Dr. Raghav Neurologist'),
        ('Dr. Monalisa Singh, Oncologist', 'Dr. Monalisa Oncologist'),
        ('Dr. Rishika Saini, Dermatologist', 'Dr. Rishika Dermatologist'),
        ('Dr. Varun Rajput, Psychiatric', 'Dr. Varun Psychiatric'),
        ('Dr. Vignesh, Physical Therapist', 'Dr. Vignesh Physical Therapist'),
        ('Dr. Nitin Arora, ENT Specialist', 'Dr. Nitin ENT Specialist'),
        ('Dr. Raghvi Singhania, Gastrologist', 'Dr. Raghvi Gastrologist'),
        ('Dr. Ishika Singh, Diabetic Specialist', 'Dr. Ishika Diabetic Specialist'),
    ]

    name = models.CharField(max_length=100, null=False)
    age = models.IntegerField(null=False)
    gender = models.CharField(max_length=20, null=False)
    phone = models.CharField(max_length=15, null=False)
    email = models.EmailField(max_length=100, null=False)
    address = models.TextField(null=False)
    date = models.DateField(null=False)
    Time = models.TimeField(auto_now=False, auto_now_add=False, null=False)
    Doctor = models.CharField(max_length=100, choices=doctor_list, default='Dr. Reshma Madan, OPD')
    disease_description = models.TextField(max_length=200)

    def __str__(self) -> str:
        return self.name