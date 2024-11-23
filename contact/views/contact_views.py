from django.http import request
from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from django.core.paginator import Paginator
from contact.models import Contact

# Create your views here.
def index(request):
    contacts = Contact.objects.all().filter(show=True) \
    .order_by('-id')

    # print(contacts.query)
    paginator = Paginator(contacts, 25)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'title': ' Agenda'
    }
    
    return render(
        request,
        "contact/index.html",
        context=context
    )

def contact(request, contact_id):
    # single_contact = Contact.objects.filter(pk=id_contact).first()
    single_contact = get_object_or_404(Contact,pk=contact_id,show=True)

    return render(
        request,
        "contact/contact.html",
        {'contact':single_contact}
    )

def search(request:request.HttpRequest):
    search_valeu = request.GET.get('q','').strip()

    if search_valeu == '':
        return redirect('contact:index')

    contacts = Contact.objects.all().filter(show=True) \
    .filter(
        Q(first_name__icontains=search_valeu) | 
        Q(last_name__icontains=search_valeu) |
        Q(phone__icontains=search_valeu) |
        Q(email__icontains=search_valeu)
        )\
    .order_by('-id')
    
    paginator = Paginator(contacts, 25)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'title': ' Agenda',
        'search_valeu': search_valeu
    }
    
    return render(
        request,
        "contact/index.html",
        context=context
    )

