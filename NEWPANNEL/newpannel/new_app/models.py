from django.db import models

# Create your models here.
class Developer(models.Model):
    name = models.CharField(max_length=250)
    image = models.ImageField(upload_to='media')
    address = models.TextField(max_length=250)

    def __str__(self):
        return self.name
    class Meta:
        ordering = ('name', 'image')
        verbose_name_plural = "developer"