# Generated by Django 4.1 on 2022-09-01 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payer_text', models.CharField(max_length=50, verbose_name='payer name')),
                ('points', models.IntegerField(verbose_name='points number')),
                ('date', models.DateTimeField(verbose_name='transaction date')),
            ],
        ),
    ]
