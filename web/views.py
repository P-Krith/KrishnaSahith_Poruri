# views.py

from django.shortcuts import render, get_object_or_404, redirect
from .models import Contact
from .forms import ContactForm

def contact_list(request):
    contacts = Contact.objects.all()
    return render(request, 'web/contact_list.html', {'contacts': contacts})

def contact_create(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact_list')
    else:
        form = ContactForm()
    
    return render(request, 'web/contact_create.html', {'form': form})

def contact_update(request, pk):
    contact = get_object_or_404(Contact, pk=pk)

    if request.method == 'POST':
        form = ContactForm(request.POST, instance=contact)
        if form.is_valid():
            form.save()
            return redirect('contact_list')
    else:
        form = ContactForm(instance=contact)
    
    return render(request, 'web/contact_update.html', {'form': form, 'contact': contact})

def contact_delete(request, pk):
    contact = get_object_or_404(Contact, pk=pk)

    if request.method == 'POST':
        contact.delete()
        return redirect('contact_list')

    return render(request, 'web/contact_delete.html', {'contact': contact})

def contact_detail(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    return render(request, 'web/contact_detail.html', {'contact': contact})

def contact_form(request, pk=None):
    if pk:
        contact = get_object_or_404(Contact, pk=pk)
    else:
        contact = None

    if request.method == 'POST':
        form = ContactForm(request.POST, instance=contact)
        if form.is_valid():
            form.save()
            return redirect('contact_detail', pk=form.instance.pk)
    else:
        form = ContactForm(instance=contact)

    return render(request, 'web/contact_form.html', {'form': form, 'contact': contact})
