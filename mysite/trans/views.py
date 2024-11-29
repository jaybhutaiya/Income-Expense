from typing import Any
from django.shortcuts import render,redirect
from . models import income
from django.views import View
from.import forms
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.db.models import Sum

def home(request):
    return render(request,'home.html')

class transaction(View):
    def get(self,request,*args,**kwargs):
        form = forms.transactionform()
        return render(request,'transaction.html',{'form':form})
    def post(self,request,*args,**kwargs):
        form=forms.transactionform(request.POST)
        if form.is_valid():
            form.save()
        return redirect('list') 


class list(ListView):
    model=income
    template_name='income_list.html'
    context_object_name='data'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context =  super(list,self).get_context_data(**kwargs)
        exp = income.objects.filter(type = 'expense').aggregate(Sum('amount'))['amount__sum']
        inc = income.objects.filter(type = 'income').aggregate(Sum('amount'))['amount__sum']
        context['amount']=inc-exp
        context['inc']=inc
        context['exp']=exp

        return context
        
