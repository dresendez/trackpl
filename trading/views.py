from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Sum
from calendar import Calendar, monthrange
from datetime import datetime, timedelta
from .models import DailyTrade
from .forms import DailyTradeForm

def calendar_view(request, year=None, month=None):
    if year is None or month is None:
        current_date = datetime.now()
        year = current_date.year
        month = current_date.month
    else:
        current_date = datetime(year, month, 1)
    
    cal = Calendar(firstweekday=6).monthdayscalendar(year, month)  # Start week on Sunday
    trades = DailyTrade.objects.filter(date__year=year, date__month=month)  # Filter trades for the current month
    
    monthly_total = trades.aggregate(Sum('profit_loss'))['profit_loss__sum'] or 0
    yearly_total = DailyTrade.objects.filter(date__year=year).aggregate(Sum('profit_loss'))['profit_loss__sum'] or 0
    
    monthly_total = round(monthly_total, 2)
    yearly_total = round(yearly_total, 2)
    
    prev_month = (current_date.replace(day=1) - timedelta(days=1)).replace(day=1)
    next_month = (current_date.replace(day=monthrange(year, month)[1]) + timedelta(days=1)).replace(day=1)
    
    context = {
        'calendar': cal,
        'trades': trades,
        'monthly_total': monthly_total,
        'yearly_total': yearly_total,
        'current_date': current_date,
        'prev_month': prev_month,
        'next_month': next_month,
    }
    return render(request, 'trading/calendar.html', context)

def add_trade_view(request, year, month, day):
    date = datetime(year, month, day)
    trade = get_object_or_404(DailyTrade, date=date) if DailyTrade.objects.filter(date=date).exists() else None
    
    if request.method == 'POST':
        form = DailyTradeForm(request.POST, instance=trade)
        if form.is_valid():
            form.save()
            return redirect('calendar', year=year, month=month)
    else:
        form = DailyTradeForm(instance=trade, initial={'date': date})
    
    context = {
        'form': form,
        'date': date,
    }
    return render(request, 'trading/add_trade.html', context)