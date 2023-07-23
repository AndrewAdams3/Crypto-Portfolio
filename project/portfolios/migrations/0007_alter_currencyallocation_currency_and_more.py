# Generated by Django 4.2.3 on 2023-07-23 06:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('currencies', '0004_rename_currencyid_currencysnapshot_currency'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('portfolios', '0006_rename_currencyid_currencyallocation_currency_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='currencyallocation',
            name='currency',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='currencyAllocation', to='currencies.currency'),
        ),
        migrations.AlterField(
            model_name='currencyallocation',
            name='portfolio',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='portfolio', to='portfolios.portfolio'),
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL),
        ),
    ]
