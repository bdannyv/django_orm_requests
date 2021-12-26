import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "part_two.settings")
import django
django.setup()

from someapp.models import Category, Product
from django.db.models import Count


def task_a():
    """
    get the number of all products with price greater or equal to 100 for every category
    """
    return (
        Product.objects.values('category__name')
        .annotate(number_of_items=Count('name'))
        .filter(price__gte=100)
    )


def task_b():
    return (
        Product.objects.values('category__name')
        .annotate(number_of_items=Count('name'))
        .filter(
            price__gte=100,
            number_of_items__gt=10
        )
    )


def task_c():
    for item in Product.objects.all():
        print("%s: %s - %s" % (item.category.name, item.name, item.price))


if __name__ == '__main__':
    print(task_a())
    print(task_b())
    task_c()