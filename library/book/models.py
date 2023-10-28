from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=100)
    price = models.IntegerField()

    def __str__(self):
        return f"{self.pk} - {self.title} - {self.price}"
