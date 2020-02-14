from django.shortcuts import render,redirect
# Create your views here.
def  about(request):
    return render(request, 'about.html')
def index(request):
    return render(request, 'index.html')
def products(request):
    return render(request, 'products.html')
def store(request):
    return render(request, 'store.html')

