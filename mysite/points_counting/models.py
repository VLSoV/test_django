from django.db import models


class Transaction(models.Model):
    payer_text = models.CharField('payer name', max_length=50)
    points = models.IntegerField('points number')
    date = models.DateTimeField('transaction date')

    def __str__(self):
        return f'{self.payer_text}: {self.points}'


class PointsNumber(models.Model):
    number = models.IntegerField('points number')

    def __str__(self):
        return str(self.number)


class Payer(models.Model):
    payer_text = models.CharField('payer name', max_length=50)
    paid = models.IntegerField('points paid')
    left = models.IntegerField('points left to pay')

    def __str__(self):
        return self.payer_text
