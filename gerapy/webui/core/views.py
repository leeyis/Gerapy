from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

from .models import Spider


def index(request):
    latest_question_list = Spider.objects.all()
    return render(request, 'pages/index.html')