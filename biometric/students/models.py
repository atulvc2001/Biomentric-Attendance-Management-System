from django.db import models

# Create your models here.


class stud_db_dest:
    name = models.CharField(max_length=100)
    cmritUSN = models.CharField(max_length=10)
    present = models.IntegerField(max_length=3)
    date = models.CharField(max_length=10)
