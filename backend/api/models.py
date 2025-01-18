from django.db import models

# Create your models here.
class Image(models.Model):
    description = models.CharField(max_length=200, default="")
    image = models.ImageField(upload_to='uploads/')
    
    def __str__(self) -> str:
        return f"Image: {self.description}"