from django.contrib import admin
from .models import Outing, Expense

# Register your models here.
admin.site.register(Outing)
admin.site.register(Expense)