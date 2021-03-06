# Generated by Django 3.1.7 on 2021-04-10 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AppointmentModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('gender', models.CharField(max_length=20)),
                ('phone', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=100)),
                ('address', models.TextField()),
                ('date', models.DateField()),
                ('Time', models.TimeField()),
                ('Doctor', models.CharField(choices=[('Dr. Reshma Madan, OPD', 'Dr. Reshma OPD'), ('Dr. Shivangi, Cardiologist', 'Dr. Shivangi Cardiologist'), ('Dr. Raghav Dixit, Neurologist', 'Dr. Raghav Neurologist'), ('Dr. Monalisa Singh, Oncologist', 'Dr. Monalisa Oncologist'), ('Dr. Rishika Saini, Dermatologist', 'Dr. Rishika Dermatologist'), ('Dr. Varun Rajput, Psychiatric', 'Dr. Varun Psychiatric'), ('Dr. Vignesh, Physical Therapist', 'Dr. Vignesh Physical Therapist'), ('Dr. Nitin Arora, ENT Specialist', 'Dr. Nitin ENT Specialist'), ('Dr. Raghvi Singhania, Gastrologist', 'Dr. Raghvi Gastrologist'), ('Dr. Ishika Singh, Diabetic Specialist', 'Dr. Ishika Diabetic Specialist')], default='Dr. Reshma Madan, OPD', max_length=100)),
                ('disease_description', models.TextField(max_length=200)),
            ],
        ),
    ]
