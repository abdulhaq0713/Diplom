from django.shortcuts import render
from django.http import HttpResponse
from .floyd import get_path, P 

def HomeView(respons):
    return render(respons, "home.html")
def calculate(request):
    bir = int(request.POST.get('bir'))
    ikki = int(request.POST.get('ikki'))
    result = get_path(P, bir, ikki)  
    return HttpResponse(f"A stansiydan B stansiyaga qisqa yo'l: {result}")

