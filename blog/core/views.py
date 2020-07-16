from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def contact(request):
    context = {
        'message': 'Contact me at 417-777-7777'
    }
    return render(request, 'core/contact.html', context)

def register_user(request):
    form = UserCreationForm()
    context = {
        'form': form
    }
    if request.method == 'POST':
        if request.POST.get('password1') == request.POST.get('password2'):
            form = UserCreationForm(request.POST)
            user = form.save()
            login(request, user)
            return redirect('contact')

    return render(request, 'core/register.html', context)