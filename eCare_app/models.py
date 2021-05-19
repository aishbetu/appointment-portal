from django.db import models

# Create your models here.
class CaraouselData(models.Model):
    title = models.CharField(max_length=100, null=False)
    description = models.TextField(max_length=200, null=True)
    image = models.URLField(null = False, default=True)

    def __str__(self):
        return self.title