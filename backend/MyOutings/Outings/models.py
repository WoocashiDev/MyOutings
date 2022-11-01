from django.db import models
from Profiles.models import Profile

# Outing model - gathering data for each outing you and your friends have
class Outing(models.Model):
    title=models.TextField(null=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    place = models.TextField(null=True, blank=True)
    date = models.DateField()
    #participants to be set as a foreign key
    participants=models.IntegerField(null=True, blank="True")
    

    def __str__(self):
        return self.title[0:30]

# Expense model - Gathers data on expenses you and your friends have made
class Expense(models.Model):
    outing = models.ForeignKey(Outing, null=True, blank=True, on_delete=models.SET_NULL)
    sponsor = models.ForeignKey(Profile, null=True, blank=True)
    beneficient = models.ForeignKey(Profile, null=True, blank=True)
    title = models.TextField(null=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    value = models.FloatField(null=True, blank=True)
