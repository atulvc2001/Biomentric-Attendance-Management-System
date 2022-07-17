from django.db import models

# Create your models here.


class stud_db_dest:
    name = models.CharField(max_length=100)
    cmritUSN = models.CharField(max_length=10)
    UniqID = models.IntegerField(max_length=2)
    Pwd = models.CharField(max_length=6)
    present = models.IntegerField(max_length=3)
    date = models.CharField(max_length=10)
