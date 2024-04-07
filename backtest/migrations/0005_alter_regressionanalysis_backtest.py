# Generated by Django 4.2.7 on 2024-04-04 20:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        (
            "backtest",
            "0004_rename_daily_return_timeseriesstats_daily_benchmark_return_and_more",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="regressionanalysis",
            name="backtest",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="regression_stats",
                to="backtest.backtest",
            ),
        ),
    ]