from django import forms
from .models import income

class transactionform(forms.ModelForm):
    class Meta:
        model=income
        fields = ['name','type','amount']
    

# class transactionform(forms.Form):
#     income = forms.ModelChoiceField(queryset=income.objects.all())
#     expense = forms.ModelChoiceField(queryset=expense.objects.none())
