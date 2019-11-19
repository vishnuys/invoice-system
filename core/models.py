from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Invoice(models.Model):
    invoice_no = models.IntegerField()
    item_code = models.CharField(max_length=100)
    item_name = models.CharField(max_length=200)
    quantity = models.IntegerField()
    date = models.DateTimeField()
    unit_price = models.FloatField()
    cashier_id = models.ForeignKey(User, on_delete=models.CASCADE)
    country = models.CharField(max_length=100)

    def __str__(self):
        return "%d - %s - %s" % (self.invoice_no, self.item_code, self.item_name)
