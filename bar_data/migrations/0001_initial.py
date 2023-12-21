# Generated by Django 5.0 on 2023-12-21 16:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("assets", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="CommodityBarData",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("timestamp", models.DateTimeField()),
                ("open", models.DecimalField(decimal_places=4, max_digits=10)),
                ("close", models.DecimalField(decimal_places=4, max_digits=10)),
                ("high", models.DecimalField(decimal_places=4, max_digits=10)),
                ("low", models.DecimalField(decimal_places=4, max_digits=10)),
                ("volume", models.BigIntegerField()),
                (
                    "asset",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="commodity_bardata",
                        to="assets.asset",
                    ),
                ),
            ],
            options={"unique_together": {("asset", "timestamp")},},
        ),
        migrations.CreateModel(
            name="CryptocurrencyBarData",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("timestamp", models.DateTimeField()),
                ("open", models.DecimalField(decimal_places=4, max_digits=10)),
                ("close", models.DecimalField(decimal_places=4, max_digits=10)),
                ("high", models.DecimalField(decimal_places=4, max_digits=10)),
                ("low", models.DecimalField(decimal_places=4, max_digits=10)),
                ("volume", models.BigIntegerField()),
                (
                    "asset",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="cryptocurrency_bardata",
                        to="assets.asset",
                    ),
                ),
            ],
            options={"unique_together": {("asset", "timestamp")},},
        ),
        migrations.CreateModel(
            name="EquityBarData",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("timestamp", models.DateTimeField()),
                ("open", models.DecimalField(decimal_places=4, max_digits=10)),
                ("close", models.DecimalField(decimal_places=4, max_digits=10)),
                ("high", models.DecimalField(decimal_places=4, max_digits=10)),
                ("low", models.DecimalField(decimal_places=4, max_digits=10)),
                ("volume", models.BigIntegerField()),
                (
                    "asset",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="equity_bardata",
                        to="assets.asset",
                    ),
                ),
            ],
            options={"unique_together": {("asset", "timestamp")},},
        ),
    ]
