from django.db import models

 


class Property(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.name




class PropertyUnit(models.Model):
    unit_number = models.CharField(max_length=10)
    floor = models.PositiveIntegerField()
    size = models.DecimalField(max_digits=5, decimal_places=2)
    rent = models.DecimalField(max_digits=8, decimal_places=2)
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='units')

    def __str__(self):
        return f"{self.unit_number} - {self.property.name}"



class PropertyOwner(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    properties = models.ManyToManyField(Property, related_name='owners')
    

    def __str__(self):
        return self.name

class PropertyManager(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    properties = models.ManyToManyField(Property, related_name='managers')
    

    def __str__(self):
        return self.name