from django.contrib import admin
from .models import Projects, Profile


@admin.register(Projects)
class PrijectAdmin(admin.ModelAdmin):
    pass


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    pass
