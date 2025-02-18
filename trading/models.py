from django.db import models

class DailyTrade(models.Model):
    date = models.DateField(unique=True)
    profit_loss = models.DecimalField(max_digits=10, decimal_places=2)
    notes = models.TextField(blank=True, null=True)
    
    class Meta:
        ordering = ['-date']

