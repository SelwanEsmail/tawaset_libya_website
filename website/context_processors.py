
from .models import News,Project 

def latest_news_and_projects_processor(request):
   
    # جلب آخر 3 أخبار مرتبة من الأحدث للأقدم
    latest_news = News.objects.all()
    projects = Project.objects.all()

    return {'global_news': latest_news,'global_projects':projects}

    #
    