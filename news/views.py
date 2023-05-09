from django.shortcuts import render
from .models import News


# Create your views here.
def news(request):
    news_list = News.objects.all().order_by('-date')
    context = {
        'news_list': news_list,
    }
    return render(request, 'news/news.html', context)
