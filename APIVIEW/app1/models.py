from django.db import models

# Create your models here.
class Info(models.Model):
    fname = models.CharField(max_length=20)
    lname = models.CharField(max_length=20)
    phoneno = models.IntegerField()
    city = models.CharField(max_length=20)

    def __str__(self):
        return self.city

class Address(models.Model):
    house_no = models.CharField(max_length=8)
    lane_name = models.CharField(max_length=20)
    area_name = models.CharField(max_length=20)
    city = models.ForeignKey(Info, on_delete=models.CASCADE)

    def __str__(self):
        return self.area_name
