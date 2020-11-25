from django import forms

class SalaryForm(forms.Form):
    salary= forms.CharField(max_length=500, label="Salary")

    