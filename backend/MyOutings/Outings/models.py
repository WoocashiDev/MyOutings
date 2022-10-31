from django.db import models

# Create your models here.
class Outing(models.Model):
    title=models.TextField(null=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    place = models.TextField(null=True, blank=True)
    #participants to be set as a foreign key
    participants=models.IntegerField(null=True, blank="True")
    #costs will be a foreign key
    costs=models.FloatField(null=True, blank=True)
    

    def __str__(self):
        return self.title[0:30]