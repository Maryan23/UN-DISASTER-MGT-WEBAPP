from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'index.html')

def article(request):
    return render(request, 'article.html')

def categories(request):
    return render(request, 'categories.html')

def contact(request):
    return render(request, 'contact.html')

def about(request):
    return render(request, 'about.html')

