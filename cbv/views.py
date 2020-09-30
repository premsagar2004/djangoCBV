from django.shortcuts import render
from django.views.generic.edit import UpdateView
from .models import Reeta

# Create your views here.
def home(request):
    return render(request,'cbv/home.html')

class GeeksUpdateView(UpdateView):
    model=Reeta
    fields = [
        "title",
        "desc"
    ]
    success_url = "/"