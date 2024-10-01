
from django.shortcuts import render
def home(request):
    return render(request, 'home.html', {'d1': 'This is our home page'})

    
