# Generated by Django 4.2.3 on 2023-07-23 20:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('currencies', '0007_alter_currencysnapshot_currency'),
    ]

    operations = [
        migrations.AlterField(
            model_name='currencysnapshot',
            name='market_cap',
            field=models.DecimalField(decimal_places=16, max_digits=30),
        ),
        migrations.AlterField(
            model_name='currencysnapshot',
            name='price',
            field=models.DecimalField(decimal_places=16, max_digits=30),
        ),
        migrations.AlterField(
            model_name='currencysnapshot',
            name='volume',
            field=models.DecimalField(decimal_places=16, max_digits=30),
        ),
    ]
