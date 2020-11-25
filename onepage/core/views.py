from django.shortcuts import render, redirect
from .forms import SalaryForm
from .taxcalculator import *


def index(request):
    output = None
    if request.method == 'GET':
        form = SalaryForm()
    else:
        form = SalaryForm(request.POST)
        if form.is_valid():
            salary = form.cleaned_data['salary']
            output = "£" + calculateTaxedSalary(float(salary))
            form = SalaryForm()
            return render(request, 'index.html',{'output': output, 'form': form}, {'band', band})
    return render(request, "index.html", {'form': form})
    return render(request, 'index.html')

    