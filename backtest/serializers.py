import logging
from django.db import transaction
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from symbols.models import Symbol
from market_data.models import BarData
from market_data.serializers import BarDataSerializer
from .services import create_backtest, get_price_data
from .models import Backtest, StaticStats, TimeseriesStats, Trade, Signal, TradeInstruction

logger = logging.getLogger()
class StaticStatsSerializer(serializers.ModelSerializer):
    class Meta:
        model = StaticStats
        fields = [
                    'net_profit', 'total_return','max_drawdown','annual_standard_deviation','ending_equity', 
                    'total_fees', 'total_trades', "num_winning_trades", "num_lossing_trades", "avg_win_percent", 
                    "avg_loss_percent","percent_profitable", "profit_and_loss", "profit_factor", "avg_trade_profit", 
                    'sharpe_ratio', 'sortino_ratio', 'alpha', 'beta'
                ]

class TimeseriesStatsSerializer(serializers.ModelSerializer):
    class Meta:
        model = TimeseriesStats
        fields = ['timestamp', 'equity_value', 'percent_drawdown', 'cumulative_return', 'daily_return']

class TradeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trade
        fields = ['trade_id', 'leg_id', 'timestamp', 'ticker', 'quantity', 'price', 'cost', 'action', 'fees']

class TradeInstructionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TradeInstruction
        fields = ['ticker', 'action', 'trade_id', 'leg_id', 'weight']

class SignalSerializer(serializers.ModelSerializer):
    trade_instructions = TradeInstructionSerializer(many=True)

    class Meta:
        model = Signal
        fields = ['timestamp', 'trade_instructions']
    
    def create(self, validated_data):
        try:
            with transaction.atomic():
                trade_instructions_data = validated_data.pop('trade_instructions', [])
                logger.info("Creating Signal object.")
                signal = Signal.objects.create(**validated_data)

                for ti_data in trade_instructions_data:
                    logger.info(f"Creating TradeInstruction object for signal {signal.id}.")
                    TradeInstruction.objects.create(signal=signal, **ti_data)

                logger.info(f"Successfully created Signal and TradeInstructions for signal {signal.id}.")
                return signal
        except Exception as e:
            logger.error(f"Error creating Signal and TradeInstructions: {str(e)}", exc_info=True)
            raise

class BacktestListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Backtest
        fields = ['id', 'strategy_name', 'tickers', 'benchmark', 'data_type', 'train_start', 'train_end', 'test_start', 'test_end', 'capital', 'created_at']

class BacktestSerializer(serializers.ModelSerializer):
    parameters = BacktestListSerializer(write_only=True)
    timeseries_stats = TimeseriesStatsSerializer(many=True)
    static_stats = StaticStatsSerializer(many=True)
    trades = TradeSerializer(many=True)
    signals = SignalSerializer(many=True)
    price_data = BarDataSerializer(read_only=True)

    class Meta:
        model = Backtest
        fields = ['id', 'parameters', 'static_stats', 'trades', 'timeseries_stats', 'signals', 'price_data']
        
    def validate(self, data):
        logger.info(f"Validating data : {data}")
        try:
            validated_data = super().validate(data)
            logger.info(f"Validating successful.")
            return validated_data
        except ValidationError as e:
            logger.error(f"Validation error: {e}")
            raise e
    
    # POST
    def create(self, validated_data):
        logger.info("Creating a new Backtest instance with data: %s", validated_data)
        try:
            backtest_instance = create_backtest(validated_data)
            logger.info(f"Successfully created Backtest instance with ID: {backtest_instance.id}")
            return backtest_instance
        except Exception as e:
            logger.exception(f"Failed to create a new Backtest instance: {str(e)}")
            raise serializers.ValidationError("Failed to create a new Backtest instance")
        
    # PUT / PATCH
    def update(self, instance, validated_data):
        logger.info(f"Updating for Backtest instance with ID: {instance.id}")
        try:
            # Proceed with the default update process
            instance = super().update(instance, validated_data)
            logger.info(f"Successfully updated Backtest instance with ID: {instance.id}")
            return instance
        except Exception as e:
            logger.exception(f"Unexpected error during update of Backtest instance with ID: {instance.id}: {e}")
            raise serializers.ValidationError(f"Update failed for unexpected reasons: {e}")

    # GET
    def to_representation(self, instance):
        logger.info(f"Retrieving a Backtest instance with ID: {instance.id}")
        try:
            data = super().to_representation(instance)
            data['parameters']  = {
                "strategy_name": instance.strategy_name,
                "tickers": instance.tickers,
                "benchmark": instance.benchmark,
                "data_type": instance.data_type,
                "train_start": instance.train_start,
                "train_end": instance.train_end,
                "test_start": instance.test_start,
                "test_end": instance.test_end,
                "capital": instance.capital,
                "created_at": instance.created_at #.isoformat(),
            }
            data['price_data'] = get_price_data(instance)
            logger.info(f"Successfully retrieved Backtest instance with ID: {instance.id}")
            return data
        except Exception as e:
            logger.exception(f"Error during representation of backtest {instance.id}: {str(e)}")
            return {"error": "An error occurred while processing the request."}  



