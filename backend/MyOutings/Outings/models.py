from django.db import models
from Profiles.models import Profile

# Outing model - gathering data for each outing you and your friends have
class Outing(models.Model):
    title=models.CharField(max_length=80, null=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    place = models.CharField(max_length=200, null=True, blank=True)
    date = models.DateField()
    participants=models.ManyToManyField(Profile, blank=True )
    

    def __str__(self):
        return self.title[0:30]

# Expense model - Gathers data on expenses you and your friends have made
class Expense(models.Model):
    outing = models.ForeignKey(Outing, null=True, blank=True, on_delete=models.SET_NULL)
    sponsor = models.ForeignKey(Profile, null=True, blank=True, on_delete=models.SET_NULL, related_name="sponsor")
    beneficient = models.ForeignKey(Profile, null=True, blank=True, on_delete=models.SET_NULL, related_name="beneficient")
    title = models.CharField(max_length=80, null=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    value = models.FloatField(null=True, blank=True)

    def __str__(self):
        return self.title[0:30]
