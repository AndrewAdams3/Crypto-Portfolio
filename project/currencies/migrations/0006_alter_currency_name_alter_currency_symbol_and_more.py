# Generated by Django 4.2.3 on 2023-07-23 08:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('currencies', '0005_alter_currencysnapshot_currency'),
    ]

    operations = [
        migrations.AlterField(
            model_name='currency',
            name='name',
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='currency',
            name='symbol',
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='currencysnapshot',
            name='currency',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='currencySnapshot', to='currencies.currency', unique=True),
        ),
    ]
