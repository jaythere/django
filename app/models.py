from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.


class EmployeeJob(models.Model):
    title = models.CharField(max_length=200)
