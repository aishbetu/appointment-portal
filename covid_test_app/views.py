from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from covid_test_app.forms import Covid_Test_Form


def covid_test(request):
    if request.method == 'POST':
        form = Covid_Test_Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = Covid_Test_Form()
        context = {
            'form': form,
        }
    return render(request, 'covid_test.html', context)

