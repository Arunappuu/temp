from django.shortcuts import render
from .models import Developer
# Create your views here.
def index(request):
    a = Developer.objects.all()
    return render(request, "index.html", {'obj': a})

