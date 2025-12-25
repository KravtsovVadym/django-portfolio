from django.db import models

# Create your models here.
class Projects(models.Model):
    title = models.CharField("Projects", max_length=50, unique=True)
    description = models.CharField("Descriptions", max_length=255)

    image = models.ImageField(
        "Projects Images",
        upload_to="project/")
    links = models.URLField("Git Links", max_length=255)
    technologies = models.CharField("Technogies", max_length=255)

    class Meta:
        verbose_name = "Project"
        verbose_name_plural = "Projects"
        
    def __str__(self):
        return self.title


class Profile(models.Model):
    autor_name = models.CharField("Autor name", max_length=50)
    about = models.TextField("About")
    image = models.ImageField("Profile Image", upload_to="profile/")

    class Meta:
        verbose_name = "Profile"
        verbose_name_plural = "Profiles"
