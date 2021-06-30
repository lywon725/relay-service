from django.shortcuts import render

# Create your views here.

def about(request):
    return render(request, "relay_app1/about.html")

def blog(request):
    return render(request, "relay_app1/blog.html")

def blog_single(request):
    return render(request, "relay_app1/blog-single.html")

def contact(request):
    return render(request, "relay_app1/contact.html")

def index(request):
    return render(request, "relay_app1/index.html")

def portfolio(request):
    return render(request, "relay_app1/portfolio.html")

def portfolio_single(request):
    return render(request, "relay_app1/portfolio_single.html")

def services(request):
    return render(request, "relay_app1/services.html")