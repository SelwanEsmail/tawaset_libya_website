from django.shortcuts import render
from .models import News,Project
from django.shortcuts import render, get_object_or_404
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
# Create your views here.
def home_page(request):
    latest_news = News.objects.all()[:3]
    return render(request,'index.html',{'latest_news': latest_news})

def news(request):
    news_list = News.objects.all().order_by('-created_at')  # ترتيب تنازلي حسب تاريخ النشر
    latest_news = News.objects.order_by('-created_at')[:3]
    return render(request, 'news.html', {'news_list': news_list,'latest_news': latest_news})

def projects(request):
    latest_news = News.objects.order_by('-created_at')[:3]
    project_list = Project.objects.all().order_by('-created_at')  # ترتيب تنازلي حسب تاريخ النشر
    return render(request, 'projects.html', {'project_list': project_list,'latest_news': latest_news})
   

def news_detail(request, pk):
    # return pk;
    latest_news = News.objects.order_by('-created_at')[:3]
    news = get_object_or_404(News, pk=pk)
    return render(request, 'news-details.html', {'news': news,'latest_news': latest_news})

def contact_us(request):
    latest_news = News.objects.order_by('-created_at')[:3]
    return render(request, 'contact.html', {'latest_news': latest_news})

def contact_form(request):
    print('----------------------------------------------------- test -----------------')
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # إعداد محتوى الرسالة
        subject = 'استشارة جديدة من موقع التواصل'
        email_message = f'الاسم: {name}\nالبريد الإلكتروني: {email}\nالرسالة:\n{message}'
        from_email = settings.DEFAULT_FROM_EMAIL
        recipient_list = ['your_email@example.com'] # الإيميل اللي تبغى تستقبل عليه الرسائل
        print('----------------------------------------------------- test -----------------')
        try:
            # إرسال الرسالة
            send_mail(subject, email_message, from_email, recipient_list)
            messages.success(request, "تم إرسال رسالتك بنجاح! سنقوم بالرد عليك في أقرب وقت ممكن.")
            print('----------------------------------------------------- Success -----------------')
            # يمكنك إعادة توجيه المستخدم لصفحة نجاح
            return render(request, 'success.html')
        except Exception as e:
            # في حالة حدوث خطأ
            print(f"حدث خطأ أثناء إرسال البريد: {e}")
            return render(request, 'error.html')

    return render(request, 'index.html')


