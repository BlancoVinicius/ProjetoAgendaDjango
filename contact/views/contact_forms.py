from django import forms
from django.http import request
from django.shortcuts import render, get_object_or_404, redirect
from django.http import request
from contact.models import Contact

# Create your views here.
class ContatcForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('first_name', 'last_name', 'phone')

def create(request:request.HttpRequest):
    
    if request.method == 'POST':
        print("aqui")
        context = {
            'form': ContatcForm(request.POST),
        }
    
        return render(
            request,
            "contact/create.html",
            context=context
        )
    
    context = {
        'form': ContatcForm(),
    }
    
    return render(
        request,
        "contact/create.html",
        context=context
    )
