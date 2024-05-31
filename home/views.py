from django.shortcuts import render
from django.http import HttpResponse
from .floyd import get_path2, P, additional_stations, Edit_V
V = Edit_V()

def HomeView(request):
    return render(request, "home.html")

def calculate(request):
    if request.method == "POST":
        bir = int(request.POST.get('station'))  # Bir HTMLdan kelgan stansiya raqami joylanadi
        ikki = list(map(int, request.POST.getlist('country')))  # Convert the list items to integers

        result = get_path2(bir, ikki)  # Assuming this function is correct

        stansiya_1 = additional_stations[bir]
        stansiya_2 = {}
        N = len(ikki)
        
        for i in range(N):
            stansiya_2[additional_stations[ikki[i]]] = V[bir][ikki[i]]  # Correcting the mapping
        
        context = {
            "stansiya_1": stansiya_1,
            "stansiya_2": stansiya_2
        }
        return render(request, "javob.html", context)
    else:
        return HttpResponse("Only POST method is allowed") 
