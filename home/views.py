from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):

    context = {}

    # Add context data here
    # context['test'] = 'OK'

    # Page from the theme 
    return render(request, 'pages/dashboard.html', context=context)

def spbi_page(request):
    return render(request, 'pages/spbi.html')
