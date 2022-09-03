from django.test import TestCase
from .models import Transaction, PointsNumber, Payer
from .views import calculate

class CountingModelTests(TestCase):
    def test_main(self):

        transactions = Transaction.objects.all()
        transactions.create(payer_text='DANNON', points=1000, date='2020-11-02T14:00:00Z')
        transactions.create(payer_text='UNILEVER', points=200, date='2020-10-31T11:00:00Z')
        transactions.create(payer_text='DANNON', points=-200, date='2020-10-31T15:00:00Z')
        transactions.create(payer_text='MILLER COORS', points=10000, date='2020-11-01T14:00:00Z')
        transactions.create(payer_text='DANNON', points=300, date='2020-10-31T10:00:00Z')

        points_number_query = PointsNumber.objects.all()
        points_number_query.create(number=5000)
        points_number = PointsNumber.objects.last()

        payers = Payer.objects.all()

        calculate(transactions, payers, points_number)

        answer = Payer.objects.all()
        answer.create(payer_text='DANNON', paid=100, left=1000)
        answer.create(payer_text='UNILEVER', paid=200, left=0)
        answer.create(payer_text='MILLER COORS', paid=4700, left=5300)

        self.assertEquals(list(payers), list(answer))
