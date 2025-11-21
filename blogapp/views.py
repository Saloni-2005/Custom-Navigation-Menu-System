from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, "blogapp/home.html")

def about(request):
    return render(request, "blogapp/about.html")

def contact(request):
    return render(request, "blogapp/contact.html")