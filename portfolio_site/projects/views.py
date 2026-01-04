from django.shortcuts import render
from projects.models import Project



def index(request):
    project = Project.objects.select_related(
        'profile__author'
    ).prefetch_related(
        'profile__skills__icon'
    ).first()
    title = project.profile.author
    return render(request, 'projects/index.html', {project: 'projects', 'title': f'Protfolio {title}'})
