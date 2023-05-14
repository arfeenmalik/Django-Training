from django.db import models


# Create your models here.
class CatCity(models.Model):
    name = models.CharField(max_length=255)
    abbreviation = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class CatTrainingType(models.Model):
    name = models.CharField(max_length=255)
    abbreviation = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class Training(models.Model):
    name = models.CharField(max_length=255)
    type = models.ForeignKey(CatTrainingType, on_delete=models.CASCADE)
    date_start = models.DateField()
    date_end = models.DateField()
    city = models.ForeignKey(CatCity, on_delete=models.CASCADE)
    street_address = models.CharField(max_length=255)
    resources = models.ManyToManyField('Resource')


class ResourceItem(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.IntegerField()
    estimated_price = models.IntegerField()
    fk_training = models.ForeignKey(Training, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Resource(models.Model):
    name = models.CharField(max_length=255)
    dob = models.DateField()
    pin = models.CharField(max_length=6)
    father_name = models.CharField(max_length=255)
    CNIC = models.CharField(max_length=13)

    def __str__(self):
        return self.name
