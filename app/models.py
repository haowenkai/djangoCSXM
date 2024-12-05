from django.db import models

class Property(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=255)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Community(models.Model):
    name = models.CharField(max_length=100)
    property = models.ForeignKey(Property, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class House(models.Model):
    community = models.ForeignKey(Community, on_delete=models.CASCADE)
    room_number = models.CharField(max_length=10)
    area = models.FloatField()

    def __str__(self):
        return f"{self.community.name} - {self.room_number}"

class Owner(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    house = models.ForeignKey(House, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
