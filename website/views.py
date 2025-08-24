from django.shortcuts import render

# Create your views here.
def home_page(request):
    return render(request,'index-6-one-page.html')

def news(request):
    return render(request,'news.html')