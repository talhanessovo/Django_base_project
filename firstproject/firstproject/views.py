from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    # return HttpResponse("Hello, World. you're at homepage")
    return render(request, 'website/index.html')

def about(request):
    #return HttpResponse("Hello, World. you're at about")
    return render(request, 'website/about.html')

def contact(request):
    #return HttpResponse("Hello, World. you're at contact")
    return render(request, 'website/contact.html')

def solutions(request):
    #return HttpResponse("Hello, World. you're at contact")
    return render(request, 'website/solutions.html')