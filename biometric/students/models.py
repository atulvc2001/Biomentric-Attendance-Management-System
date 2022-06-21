from django.db import models

# Create your models here.


class stud_db_dest:
    name = models.CharField(max_length=100)
    cmritUSN = models.CharField(max_length=10)
    date = models.CharField(max_length=20)
