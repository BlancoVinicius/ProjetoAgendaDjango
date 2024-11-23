from django.http import request
from django.shortcuts import render, get_object_or_404, redirect
from django.http import request
from contact.forms import ContatcForm

# Create your views here.

def create(request:request.HttpRequest):
    
    if request.method == 'POST':
        form = ContatcForm(request.POST)
        context = {
            'form': form
        }

        if form.is_valid():
            form.save()
            return redirect('contact:create')
    
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
