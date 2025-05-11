# --- tracker/models.py ---
from django.db import models

class DailyLog(models.Model):
    date = models.DateField(unique=True)

    spendings = models.FloatField(default=0)
    spending_description = models.TextField(blank=True, null=True)

    received = models.FloatField(default=0, blank=True, null=True)
    received_description = models.TextField(blank=True, null=True)

    invested = models.FloatField(default=0)
    invested_description = models.TextField(blank=True, null=True)

    fd_incoming = models.FloatField(default=0)
    fd_outgoing = models.FloatField(default=0)
    current_fd = models.FloatField(default=0)

    axis_savings = models.FloatField(default=0)
    union_savings = models.FloatField(default=0)
    kotak_savings = models.FloatField(default=0)

    grow_pnl = models.FloatField(default=0)
    grow_wallet = models.FloatField(default=0)
    mutualfund_pnl = models.FloatField(default=0)
    kite_pnl = models.FloatField(default=0)
    kite_wallet = models.FloatField(default=0)
    trading_pnl = models.FloatField(default=0)

    wint_wealth = models.FloatField(default=0)
    nps = models.FloatField(default=0)
    epfo = models.FloatField(default=0)

    loan_given = models.FloatField(default=0)
    home_spendings = models.FloatField(default=0)
    home_spend_description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.date}"
