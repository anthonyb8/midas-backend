# Generated by Django 4.2.7 on 2024-03-02 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("backtest", "0002_staticstats_timeseriesstats_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="trade", old_name="symbol", new_name="ticker",
        ),
        migrations.AlterField(
            model_name="trade",
            name="quantity",
            field=models.DecimalField(decimal_places=4, max_digits=10),
        ),
    ]