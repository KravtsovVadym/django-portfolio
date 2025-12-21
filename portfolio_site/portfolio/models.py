from django.db import models

# Create your models here.
class Portfolio(models.Model):
    title = models.CharField("Projects", max_length=50, unique=True)
    description = models.CharField("Descriptions", max_length=255)

    image = models.ImageField(
        "Images",
        upload_to="images/")
    links = models.URLField("Git Links", max_length=255)
    technologies = models.CharField("Technogies", max_length=255)

    class Meta:
        verbose_name = "Project"
        verbose_name_plural = "Projects"
        
    def __str__(self):
        return self.title