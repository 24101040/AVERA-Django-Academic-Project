from django.shortcuts import render

def adoption_hub(request):
    return render(request, 'adoption/hub.html')