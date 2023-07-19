from django.db import models

# Create your models here.
class KirModel(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    subject = models.CharField(max_length=255, null=True, blank=True)
    text = models.TextField(blank=True, null=True)
    def __str__(self):
        return f"{self.phone} -->  {self.name}"


class CourseModel(models.Model):
    v = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    des = models.TextField(blank=True, null=True)
    avatar = models.ImageField(upload_to="aksha")
    def __str__(self):
        return f"{self.name}"