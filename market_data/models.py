from django.db import models

class BarData(models.Model):
    symbol = models.ForeignKey('symbols.Symbol', on_delete=models.CASCADE, related_name='bardata')
    timestamp = models.DateTimeField(db_index=True)
    open = models.DecimalField(max_digits=10, decimal_places=4)
    close = models.DecimalField(max_digits=10, decimal_places=4)
    high = models.DecimalField(max_digits=10, decimal_places=4)
    low = models.DecimalField(max_digits=10, decimal_places=4)
    volume = models.BigIntegerField()

    class Meta:
        unique_together = ('symbol', 'timestamp')
        ordering = ['timestamp']
        indexes = [
            models.Index(fields=['symbol', 'timestamp']), # Composite index for optimizing queries
        ]


    def __str__(self):
        return f"BarData(ticker={self.symbol}, timestamp={self.timestamp})"


