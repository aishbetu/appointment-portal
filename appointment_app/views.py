from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.core.mail import send_mail

# Create your views here.
from appointment_app.forms import AppoAppointmentForm


def appointment(request):
    if request.method == 'POST':
        form = AppoAppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            # name = form.cleaned_data.get("name")
            # appointment_date = form.cleaned_data.get("date")
            # appointment_time = form.cleaned_data.get("Time")
            # doctor_name = form.cleaned_data.get("Doctor")
            # email_to = form.cleaned_data.get("email")
            #
            # send_mail(
            #     'Appointment Booked at ' + appointment_date,
            #     'Dear' + name + 'appointment is successfully done at ' + appointment_time + 'with ' + doctor_name,
            #     'aishbetu@gmail.com',
            #     [email_to],
            #     fail_silently=False,
            # )
            return redirect('success')
    else:
        form = AppoAppointmentForm()
        context = {
            'form': form,
        }
    return render(request, "appointment.html", context)

def success(request):
    return render(request, 'success.html')