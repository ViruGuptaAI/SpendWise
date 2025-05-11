# --- tracker/views.py ---
from django.shortcuts import render, redirect
from .forms import DailyLogForm

def add_log(request):
    form = DailyLogForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('/')
    return render(request, 'tracker/add_log.html', {'form': form})
