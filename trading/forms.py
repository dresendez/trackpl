from django import forms
from .models import DailyTrade

class DailyTradeForm(forms.ModelForm):
    class Meta:
        model = DailyTrade
        fields = ['date', 'profit_loss', 'notes']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }