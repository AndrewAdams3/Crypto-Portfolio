# Generated by Django 4.2.3 on 2023-07-22 19:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('currencies', '0001_initial'),
        ('portfolios', '0003_remove_portfolio_owner_portfolio_userid'),
    ]

    operations = [
        migrations.CreateModel(
            name='CurrencyAllocation',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('allocation', models.FloatField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('currencyId', models.ForeignKey(db_column='currencyId', on_delete=django.db.models.deletion.CASCADE, related_name='currencyAllocation', to='currencies.currency')),
                ('portfolioId', models.ForeignKey(db_column='portfolioId', on_delete=django.db.models.deletion.CASCADE, related_name='portfolio', to='portfolios.portfolio')),
            ],
        ),
    ]
