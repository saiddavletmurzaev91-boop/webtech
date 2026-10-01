from django.shortcuts import render
from .models import News


def index(request):
    news = News.objects.all().order_by('-created_at')
    return render(request, 'news/index.html', {
        'news': news,
        'title': 'Новости'
    })


def test(request):
    return render(request, 'news/test.html')