from django.db import models

class jobs:
    title=models.CharField(max_length=20)
    description=models.CharField(max_length=15)
   
class Meta:
    db_table='jobs'    