
# --- tracker/forms.py ---
from django import forms
from .models import DailyLog

class DailyLogForm(forms.ModelForm):
    class Meta:
        model = DailyLog
        fields = '__all__'
