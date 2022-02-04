from django.shortcuts import render

def indeks(request):
    return render(request, 'medium/clone.html')