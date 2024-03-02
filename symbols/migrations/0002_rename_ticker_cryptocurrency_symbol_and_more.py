# Generated by Django 5.0.1 on 2024-02-10 14:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("symbols", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="cryptocurrency", old_name="ticker", new_name="symbol",
        ),
        migrations.RenameField(
            model_name="equity", old_name="ticker", new_name="symbol",
        ),
        migrations.RenameField(
            model_name="future", old_name="ticker", new_name="symbol",
        ),
        migrations.RenameField(
            model_name="option", old_name="ticker", new_name="symbol",
        ),
        migrations.AlterField(
            model_name="symbol",
            name="security_type",
            field=models.CharField(
                choices=[
                    ("EQUITY", "EQUITY"),
                    ("FUTURE", "FUTURE"),
                    ("OPTION", "OPTION"),
                    ("INDEX", "INDEX"),
                ],
                max_length=10,
            ),
        ),
        migrations.CreateModel(
            name="Index",
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
                ("name", models.CharField(max_length=100)),
                ("exchange", models.CharField(max_length=50)),
                (
                    "asset_class",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="symbols.assetclass",
                    ),
                ),
                (
                    "currency",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="symbols.currency",
                    ),
                ),
                (
                    "symbol",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="index",
                        to="symbols.symbol",
                    ),
                ),
            ],
        ),
        migrations.DeleteModel(name="Benchmark",),
    ]