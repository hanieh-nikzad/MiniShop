from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)

    def str(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField()
    description = models.TextField()

    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )

    image = models.ImageField(
        upload_to='products/',
        blank=True,
        null=True
    )

    def str(self):
        return self.name