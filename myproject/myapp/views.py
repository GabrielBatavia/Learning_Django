from django.shortcuts import render
from django.http import HttpResponse
from .models import Feature

# Create your views here.
def index(request):
    feature1 = Feature()
    feature1.id = 0
    feature1.name = 'Machine Learning Engginer'
    feature1.details = 'Deep Learning - Cloud Computing - Database management'
    return render(request, 'index.html', {'feature': feature1})

def counter(request):
    text = request.POST.get('text')
    amount_of_words = len(text.split())
    return render(request, 'counter.html', {'amount': amount_of_words})
