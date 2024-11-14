from django.db import models

# Create your models here.

class Category(models.Model):
    slug=models.CharField(max_length=150, null=False, blank=False)
    name=models.CharField(max_length=255)


    def __str__(self):
        return self.name


class Kurs(models.Model):
    slug=models.CharField(max_length=150, null=False, blank=False)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    name=models.CharField(max_length=255)
    price=models.IntegerField()
    description=models.TextField()
    duration=models.TextField

    def __str__(self):
        return self.name


class Malim(models.Model):
    name=models.CharField(max_length=200)
    age=models.IntegerField()
    experience=models.TextField()
    image=models.ImageField(upload_to="new_images/")
    description=models.TextField()


    def __str__(self):
        return self.name











