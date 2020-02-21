from django.shortcuts import render, redirect
# Create your views here.
def  about(request):
    return render(request, 'index.html')
def index(request):
    return render(request, 'gallery-freestyle.html')
def products(request):
    return render(request, 'blog.html')
def store(request):
    return render(request, 'shortcode-about.html')
def call(request):
    return render(request, 'contact-us.html')


