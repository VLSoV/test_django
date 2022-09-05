from django.shortcuts import render, redirect
from .models import Transaction, PointsNumber, Payer
from .forms import TransactionForm, PointsNumberForm

global count
count = 0


def calculate(transactions, payers, points_number):
    transactions = transactions.order_by('date')
    points_number_int = points_number.number
    payers.update(left=0)

    for transaction in transactions:
        payer = payers.filter(payer_text=transaction.payer_text).last()
        if payer is None:
            payers.create(payer_text=transaction.payer_text, paid=0, left=0)
            payer = payers.filter(payer_text=transaction.payer_text).last()

        if transaction.points <= points_number_int:
            payer.paid += transaction.points
            points_number_int -= transaction.points
            transaction.delete()
        else:
            payer.paid += points_number_int
            payer.left += transaction.points - points_number_int
            transaction.points -= points_number_int
            transaction.save()
            points_number_int = 0

        payer.save()

    transactions.update()
    if points_number_int == 0:
        points_number.delete()


def index(request):
    global count
    count += 1

    transactions = Transaction.objects.all()
    payers = Payer.objects.all()

    points_number = PointsNumber.objects.last()
    if points_number is not None:
        calculate(transactions, payers, points_number)

    data = {
        'transactions': transactions,
        'payers': payers,
        'start_count': count,
    }
    return render(request, 'points_counting/index.html', data)


def create(request):
    form = TransactionForm()

    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')

    data = {
        'form': form,
    }
    return render(request, 'points_counting/create.html', data)


def paying(request):
    form = PointsNumberForm()

    if request.method == 'POST':
        form = PointsNumberForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')

    data = {
        'form': form,
    }
    return render(request, 'points_counting/paying.html', data)
