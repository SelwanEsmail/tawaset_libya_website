from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField 

# Create your models here.
#-------------------- Projects --------------#
class Project(models.Model):
    name = models.CharField(max_length=200, verbose_name="اسم المشروع")
    image = models.ImageField(upload_to='projects/', verbose_name="صورة المشروع")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاريخ الإنشاء")

    def __str__(self):
        return self.name
    
   
    class Meta:
        verbose_name = "مشروع"
        verbose_name_plural = "المشاريع"

#-------------------- News --------------#

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="اسم التصنيف")
    # slug = models.SlugField(max_length=120, unique=True, verbose_name="الرابط")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "تصنيف"
        # verbose_name_plural = "التصنيفات"
class News(models.Model):
    title = models.CharField(max_length=255, verbose_name="عنوان الخبر")
    description = RichTextField(verbose_name="وصف الخبر") # السطر الجديد
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="المستخدم الذي أضاف الخبر")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="التصنيف", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاريخ النشر")
    # views = models.PositiveIntegerField(default=0, verbose_name="عدد المشاهدات") 

    def __str__(self):
        return self.title
    
    def save_model(self, request, obj, form, change):
        if not obj.pk:  # هذا الشرط يعني "عند إنشاء خبر جديد فقط"
            obj.author = request.user # اجعل حقل "author" هو المستخدم الحالي
        super().save_model(request, obj, form, change)
    def get_first_image(self):
        first_media = self.media.filter(file__icontains='.jpg').first() or self.media.filter(file__icontains='.png').first()  
        return first_media.file.url if first_media else None
    class Meta:
        verbose_name = "خبر"
        verbose_name_plural = "الأخبار"

class NewsMedia(models.Model):
    news = models.ForeignKey(News, related_name='media', on_delete=models.CASCADE)
    file = models.FileField(upload_to='news_media/', verbose_name="ملف (صورة أو فيديو)")

    def __str__(self):
        return f"ملف للخبر: {self.news.title}"

    class Meta:
        verbose_name = "ملف وسائط"
        verbose_name_plural = "ملفات الوسائط"
