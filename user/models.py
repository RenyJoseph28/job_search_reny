from django.db import models

class signup:
    name=models.CharField(max_length=20)
    password=models.CharField(max_length=15)
    mobile=models.IntegerField(max_length=15)
class Meta:
    db_table='signup'    