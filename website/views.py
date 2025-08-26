from django.shortcuts import render
from .models import News
from django.shortcuts import render, get_object_or_404

# Create your views here.
def home_page(request):
    return render(request,'test.html')

def news(request):
    news_list = News.objects.all().order_by('-created_at')  # ترتيب تنازلي حسب تاريخ النشر
    latest_news = News.objects.order_by('-created_at')[:3]
    return render(request, 'news.html', {'news_list': news_list,'latest_news': latest_news})
    # return render(request,'news.html')

def news_detail(request, pk):
    # return pk;
    latest_news = News.objects.order_by('-created_at')[:3]
    news = get_object_or_404(News, pk=pk)
    return render(request, 'news-details.html', {'news': news,'latest_news': latest_news})