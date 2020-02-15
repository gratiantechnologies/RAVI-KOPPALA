from django.shortcuts import render ,redirect
# Create your views here.
def  about(request):
    return render(request, 'about.html')
def index(request):
    return render(request, 'cat-archives.html')
def products(request):
    return render(request, 'contact.html')
def store(request):
    return render(request, 'index.html')
def typo(request):
    return render(request, 'typo.html')

# Create your views here.
