from django.db import models


# 朝代
class Dynasty(models.Model):
    name = models.CharField(max_length=256)
    begin_year = models.IntegerField()
    end_year = models.IntegerField()
