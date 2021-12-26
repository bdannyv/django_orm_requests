from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


# Create your models here.
def validate_percentage_field(value):
    if 100 < value:
        raise ValidationError('Percentage value is greater then 100%(%d%)' %value)
    elif value < 0:
        raise ValidationError('Percentage value is less then 0%(%d%)' %value)


class Discount(models.Model):
    value = models.DecimalField(validators=[validate_percentage_field])
    start = models.DateField()
    end = models.DateField()


class OnlyNameModel(models.Model):
    name = models.CharField(max_length=100)
    discount = models.ForeignKey(Discount, on_delete=models.CASCADE)

    class Meta:
        abstract = True


class Brand(OnlyNameModel):
    pass


class Category(OnlyNameModel):
    pass

class User(AbstractUser):
    discount = models.ForeignKey


class Basket(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)


class Item(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(decimal_places=2)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    basket = models.ForeignKey(Basket, on_delete=models.CASCADE)

    @property
    def discount(self):
        return max((self.brand.discount, self.category.discount))
