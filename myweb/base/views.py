from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home(request):
    context = {"word": "Hello world!!!"}
    return render(request, 'home.html',context)

def about(request):
    return HttpResponse(f"<h1>about page</h1>")