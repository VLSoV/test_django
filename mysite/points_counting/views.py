from django.shortcuts import render, redirect
from .models import Transaction, PointsNumber
from .forms import TransactionForm, PointsNumberForm
from django.views.generic import  DateDetailView

global count
count = 0


def calculate(transactions, points_number):
    paid = {}
    left = {}

    for transaction in transactions:
        if transaction.payer_text not in paid:
            paid[transaction.payer_text] = 0
            left[transaction.payer_text] = 0

        if transaction.points <= points_number:
            paid[transaction.payer_text] += transaction.points
            points_number -= transaction.points
        else:
            paid[transaction.payer_text] += points_number
            left[transaction.payer_text] += transaction.points - points_number
            points_number = 0

    result = []

    for payer in paid.keys():
        result.append((payer, paid[payer], left[payer]))

    return result


def index(request):
    global count
    count += 1

    transactions = Transaction.objects.order_by('date')
    points_number = PointsNumber.objects.last().number
    result = calculate(transactions, points_number)

    data = {
        'transactions': transactions,
        'result': result,
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
