from django.contrib.auth import get_user_model
from django.db import models


class ExpanseTracking(models.Model):
    balance = models.FloatField(default=0)
    status = models.CharField(max_length=30)
    date = models.DateField()
    price = models.FloatField()
    description = models.CharField(max_length=10)
    user = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, related_name="user_exp"
    )
