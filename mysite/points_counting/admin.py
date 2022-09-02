from django.contrib import admin

from .models import Transaction, PointsNumber

admin.site.register(Transaction)
admin.site.register(PointsNumber)