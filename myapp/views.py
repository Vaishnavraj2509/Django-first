from django.shortcuts import render, HttpResponse

# Create your views here.

def index(request):
     return render(request, 'index.html')
    # return HttpResponse("title is home page")

def home(request):
     return HttpResponse("title is home page")

def about(request):
    return HttpResponse("title is about page")

def services(request):
    return HttpResponse("title is services page")

def contact(request):
    return HttpResponse("title is contact page")
