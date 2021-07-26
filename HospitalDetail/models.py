from django.db import models

class HospitalDetails(models.Model):
    hName = models.CharField(max_length=100, default='NULL')
    hCode = models.CharField(max_length=10, default='NULL')
    hAddress = models.CharField(max_length=200, default='NULL')
    hState = models.CharField(max_length=50, default="NULL")
    hCity = models.CharField(max_length=50, default="NULL")
    hPincode = models.CharField(max_length=50, default="NULL")
    hTotalNumBed = models.IntegerField(default=-1)
    hBedBooked = models.IntegerField(default=0)
    hBedAvail = models.IntegerField(default=1)
    hLocation = models.URLField(default="NULL")

    def __str__(self):
        return "Hospital name:" + self.hName + " Address:" + self.hAddress + " Beds available = " + str(self.hTotalNumBed - self.hBedBooked)

