from django.db import models as m


class Category(m.Model):
    name = m.CharField(max_length=20)

    def __str__(self):
        return self.name


class Item(m.Model):
    title = m.CharField(max_length=20)
    price = m.FloatField()
    # image = m.ImageField(null=True)
    description = m.CharField(max_length=20)
    category = m.ForeignKey(Category, on_delete=m.CASCADE)

    def __str__(self):
        return self.title
