from django.db import models


class Company(models.Model):
    company_token = models.CharField(max_length=100)
    created_at = models.DateField()
    updated_at = models.DateField()

    def __str__(self):
        return self.company_token


class Device(models.Model):
    company_id = models.ForeignKey(Company, on_delete=models.CASCADE)
    device_id = models.CharField(max_length=11)
    device_model = models.CharField(max_length=11)
    created_at = models.DateField()
    updated_at = models.DateField()
    app = models.CharField(max_length=11)
    version = models.CharField(max_length=11)

    def __str__(self):
        return self.app


class Location(models.Model):
    company_id = models.ForeignKey(Company, on_delete=models.CASCADE)
    device_id = models.ForeignKey(Device, on_delete=models.CASCADE)
    latitude = models.CharField(max_length=11)
    longitude = models.CharField(max_length=11)
    created_at = models.DateField()
    updated_at = models.DateField()
    data = models.TextField()


