# Generated by Django 4.2.7 on 2024-04-20 20:41

from decimal import Decimal
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Backtest",
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
                ("strategy_name", models.CharField(max_length=255)),
                ("tickers", models.JSONField(default=list)),
                ("benchmark", models.JSONField(default=list)),
                ("data_type", models.CharField(max_length=10)),
                ("train_start", models.BigIntegerField(blank=True, null=True)),
                ("train_end", models.BigIntegerField(blank=True, null=True)),
                ("test_start", models.BigIntegerField(blank=True, null=True)),
                ("test_end", models.BigIntegerField(blank=True, null=True)),
                ("capital", models.FloatField(blank=True, null=True)),
                ("strategy_allocation", models.FloatField(blank=True, null=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name="Signal",
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
                ("timestamp", models.BigIntegerField()),
                (
                    "backtest",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="signals",
                        to="backtest.backtest",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="TradeInstruction",
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
                ("ticker", models.CharField(max_length=100)),
                ("action", models.CharField(max_length=10)),
                ("trade_id", models.PositiveIntegerField()),
                ("leg_id", models.PositiveIntegerField()),
                ("weight", models.FloatField()),
                (
                    "signal",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="trade_instructions",
                        to="backtest.signal",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Trade",
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
                ("trade_id", models.CharField(max_length=100)),
                ("leg_id", models.CharField(max_length=100)),
                ("timestamp", models.BigIntegerField()),
                ("ticker", models.CharField(max_length=50)),
                ("quantity", models.DecimalField(decimal_places=4, max_digits=10)),
                ("price", models.DecimalField(decimal_places=4, max_digits=10)),
                ("cost", models.DecimalField(decimal_places=4, max_digits=10)),
                ("action", models.CharField(max_length=10)),
                ("fees", models.DecimalField(decimal_places=4, max_digits=10)),
                (
                    "backtest",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="trades",
                        to="backtest.backtest",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="TimeseriesStats",
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
                ("timestamp", models.BigIntegerField()),
                (
                    "equity_value",
                    models.DecimalField(decimal_places=2, default=0.0, max_digits=15),
                ),
                (
                    "period_return",
                    models.DecimalField(decimal_places=6, default=0.0, max_digits=15),
                ),
                (
                    "cumulative_return",
                    models.DecimalField(decimal_places=6, default=0.0, max_digits=15),
                ),
                (
                    "percent_drawdown",
                    models.DecimalField(decimal_places=6, default=0.0, max_digits=15),
                ),
                (
                    "daily_benchmark_return",
                    models.DecimalField(decimal_places=6, default=0.0, max_digits=15),
                ),
                (
                    "daily_strategy_return",
                    models.DecimalField(decimal_places=6, default=0.0, max_digits=15),
                ),
                (
                    "backtest",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="timeseries_stats",
                        to="backtest.backtest",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="StaticStats",
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
                ("net_profit", models.FloatField(null=True)),
                ("total_return", models.FloatField(null=True)),
                ("max_drawdown", models.FloatField(null=True)),
                ("annual_standard_deviation", models.FloatField(null=True)),
                ("ending_equity", models.FloatField(null=True)),
                ("total_fees", models.FloatField(null=True)),
                ("total_trades", models.IntegerField(null=True)),
                ("num_winning_trades", models.IntegerField(null=True)),
                ("num_lossing_trades", models.IntegerField(null=True)),
                ("avg_win_percent", models.FloatField(null=True)),
                ("avg_loss_percent", models.FloatField(null=True)),
                ("percent_profitable", models.FloatField(null=True)),
                ("profit_and_loss", models.FloatField(null=True)),
                ("profit_factor", models.FloatField(null=True)),
                ("avg_trade_profit", models.FloatField(null=True)),
                ("sortino_ratio", models.FloatField(null=True)),
                (
                    "backtest",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="static_stats",
                        to="backtest.backtest",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="RegressionAnalysis",
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
                (
                    "r_squared",
                    models.DecimalField(
                        decimal_places=8,
                        max_digits=10,
                        validators=[
                            django.core.validators.MinValueValidator(Decimal("0.0")),
                            django.core.validators.MaxValueValidator(Decimal("1.0")),
                        ],
                    ),
                ),
                ("p_value_alpha", models.DecimalField(decimal_places=8, max_digits=10)),
                ("p_value_beta", models.DecimalField(decimal_places=8, max_digits=10)),
                ("risk_free_rate", models.DecimalField(decimal_places=4, max_digits=5)),
                ("alpha", models.DecimalField(decimal_places=8, max_digits=10)),
                ("beta", models.DecimalField(decimal_places=8, max_digits=10)),
                ("sharpe_ratio", models.DecimalField(decimal_places=8, max_digits=10)),
                (
                    "annualized_return",
                    models.DecimalField(decimal_places=8, max_digits=10),
                ),
                (
                    "market_contribution",
                    models.DecimalField(decimal_places=8, max_digits=10),
                ),
                (
                    "idiosyncratic_contribution",
                    models.DecimalField(decimal_places=8, max_digits=10),
                ),
                (
                    "total_contribution",
                    models.DecimalField(decimal_places=8, max_digits=10),
                ),
                (
                    "annualized_volatility",
                    models.DecimalField(decimal_places=8, max_digits=10),
                ),
                (
                    "market_volatility",
                    models.DecimalField(decimal_places=8, max_digits=10),
                ),
                (
                    "idiosyncratic_volatility",
                    models.DecimalField(decimal_places=8, max_digits=10),
                ),
                (
                    "total_volatility",
                    models.DecimalField(decimal_places=8, max_digits=10),
                ),
                (
                    "portfolio_dollar_beta",
                    models.DecimalField(decimal_places=8, max_digits=15),
                ),
                (
                    "market_hedge_nmv",
                    models.DecimalField(decimal_places=8, max_digits=15),
                ),
                (
                    "backtest",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="regression_stats",
                        to="backtest.backtest",
                    ),
                ),
            ],
        ),
    ]
