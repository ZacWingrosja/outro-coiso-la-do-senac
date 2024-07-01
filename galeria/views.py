from django.shortcuts import render
from galeria.models import Produtos

# Create your views here.
def index(request):
    return render(request, 'index.html', {"cards":produtos})
