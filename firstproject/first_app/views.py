from django.shortcuts import render
from .models import Varity

# Create your views here.
def first_app(request):
    chais = Varity.objects.all()
    return render(request, 'first_app/all_app.html', {'chais': chais})