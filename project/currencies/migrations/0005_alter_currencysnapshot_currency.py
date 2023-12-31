# Generated by Django 4.2.3 on 2023-07-23 06:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('currencies', '0004_rename_currencyid_currencysnapshot_currency'),
    ]

    operations = [
        migrations.AlterField(
            model_name='currencysnapshot',
            name='currency',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='currencySnapshot', to='currencies.currency'),
        ),
    ]
