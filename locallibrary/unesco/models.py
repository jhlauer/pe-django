from django.db import models

# Create your models here.
class Category(models.Model) :
    name = models.CharField(max_length=128)
    def __str__(self) :
        return self.name

class Iso(models.Model):
    name = models.CharField(max_length=2)
    def __str__(self) :
        return self.name

class Region(models.Model):
    name = models.CharField(max_length=128)
    def __str__(self) :
        return self.name

class States(models.Model):
    name = models.CharField(max_length=128)
    def __str__(self) :
        return self.name

class Site(models.Model):
    #Foreignkeys
    region = models.ForeignKey(Region, on_delete=models.CASCADE, null=True)
    iso = models.ForeignKey(Iso, on_delete=models.SET_NULL, null=True)
    states = models.ForeignKey(States, on_delete=models.CASCADE, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)

    #sitekeys
    name = models.CharField(max_length=128)
    year = models.IntegerField(null=True)
    description = models.CharField(max_length=1000, blank=True, null=True, help_text="description")
    justification = models.CharField(max_length=1000, blank=True, null=True, help_text="justification")
    longitude = models.DecimalField(null=True, max_digits=15, decimal_places=7)
    latitude = models.DecimalField(null=True, max_digits=15, decimal_places=7)
    area_hectares = models.DecimalField(null=True, max_digits=10, decimal_places=2)

    def __str__(self) :
        return self.name
