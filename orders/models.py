from django.db import models

# Create your models here.
class OrderStatus(models.Model):
    name = models.CharField(max_length=50,unique=True)
    def __str__(self):
        return self.name


class Order(models.Model):
    status = models.ForeignKey(OrderStatus,on_delete=models.SET_NULL,null=True,blank=True)
    def __str__(self):
        return f"Order #{self.id} - Status{self.status}"


class Coupon(models.Model):
    code = models.CharField(unique=True)
    discount_percentage = models.DecimalField(max_digits=5,decimal_places=2)
    is_active = models.BooleanField(default=True)
    valid_from = models.DateField()
    valid_until = models.DateField()
    def __str__(self):
        return f"{self.code} - {self.discount_percentage}%"