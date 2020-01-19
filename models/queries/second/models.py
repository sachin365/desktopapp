from django.db import models

# Create your models here.


class Programmer(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    languages = models.ManyToManyField(Language)

    def __str__(self):
        return self.name