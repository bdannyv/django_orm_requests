from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField("Группа товара", max_length=64)

    def __str__(self):
        return 'category: %s' % self.name


class Product(models.Model):
    category = models.ForeignKey(Category, verbose_name="Группа", on_delete=models.CASCADE)
    name = models.CharField("Название товара", max_length=128)
    price = models.DecimalField(
        "Стоимость единицы, руб.",
        max_digits=10,
        decimal_places=2
    )

    def __str__(self):
        return '%s: %d' %(self.name, self.price)
