from django.contrib import admin

from .models import Transaction, PointsNumber, Payer

admin.site.register(Transaction)
admin.site.register(PointsNumber)
admin.site.register(Payer)