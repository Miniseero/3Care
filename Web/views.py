from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'Web/index.html')

def quiz(request):
    return render(request,'Web/quiz.html')
def noticias(request):
    return render(request,'Web/noticias.html')