from django.db import models

# Create your models here.

class Branches(models.Model):
    Branch=models.CharField(max_length=5)

    def __str__(self):
        return str(self.Branch)

class Register(models.Model):
    Name=models.CharField(max_length=50)
    Email=models.EmailField()
    Roll=models.PositiveIntegerField()
    Branch=models.OneToOneField(Branches,on_delete=models.CASCADE)

    def __str__(self):
        return str(self.Roll)