from django.shortcuts import render
from portfolio.models import Portfolio
# Create your views here.

def index(request):
    projects = Portfolio.objects.all()
    context = {
        "projects": projects,
        "title": "Vadym Kravtsov",
        }
    return render(request, "portfolio/index.html",context=context)