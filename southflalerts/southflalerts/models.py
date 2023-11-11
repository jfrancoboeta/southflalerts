from django.db import models

class EmpInsert(models.Model):
    URL = models.CharField(max_length = 300)
    email = models.CharField(max_length = 50)
    class Meta:
        db_table = "people"
        unique_together = ('URL', 'email',)

class EmpDelete(models.Model):
    email = models.CharField(max_length = 50)
    class Meta:
        db_table = "people"

