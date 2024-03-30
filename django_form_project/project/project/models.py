from django.db import models

class MyModel(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name
    
class student(models.Model):
    firstname=models.CharField(max_length=150)
    lastname=models.CharField(max_length=150)
    number=models.IntegerField()
    