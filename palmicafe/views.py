from django.shortcuts import render

# Vista para el index
def index(request):
    return render(request, 'index.html')
