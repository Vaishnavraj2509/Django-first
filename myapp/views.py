from django.shortcuts import render, HttpResponse

# Create your views here.

def index(request):
     return render(request, 'index.html')
    # return HttpResponse("title is home page")

def home(request):
    #  return HttpResponse("title is home page")
         return render(request, 'index.html')


def about(request):
    # return HttpResponse("title is about page")
         return render(request, 'about.html')


def services(request):
    # return HttpResponse("title is services page")
         return render(request, 'services.html')



def contact(request):
    # return HttpResponse("title is contact page")
         return render(request, 'contact.html')

