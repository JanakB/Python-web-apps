from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .forms import ReservationForm
# Create your views here.

def hello_world(request):
    return HttpResponse("Hello world") 


class HelloNepal(View):
    def get(self, request):
        return HttpResponse("Hello Nepal")


def home(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Success")
        # If POST but form invalid
        return render(request, 'index.html', {'form': form})
    
    # Handle GET request
    form = ReservationForm()
    return render(request, 'index.html', {'form': form})