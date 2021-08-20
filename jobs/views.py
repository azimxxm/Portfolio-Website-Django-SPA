from django.shortcuts import redirect, render
from .models import *
from .forms import *

def index(request):
    about = About.objects.all()
    portfolio = Portfolio.objects.all()
    certificat = Certificate.objects.all()
    form = ContactForm
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {
        'about':about,
        'portfolio':portfolio,
        'certificat':certificat,
    }
    return render(request, 'jobs/index.html', context)

def message(request):

    return render(request, 'jobs/index.html')
