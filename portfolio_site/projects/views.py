from django.shortcuts import render
from projects.models import Projects


def index(request):
    projects = Projects.objects.all()
    context = {
        "projects": projects,
        "title": "Vadym Kravtsov",
        }
    return render(request, "projects/index.html",context=context)