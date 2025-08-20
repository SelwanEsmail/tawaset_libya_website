from django.contrib import admin
from .models import Project
from .models import News, NewsMedia
# news/admin.py
from django.utils.html import format_html
# Register your models here.
@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')
    search_fields = ('name',)

class NewsMediaInline(admin.TabularInline):
    model = NewsMedia
    extra = 1 # عدد الحقول الفارغة للوسائط الجديدة

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    search_fields = ('title', 'description')
    list_filter = ('author', 'created_at')
    inlines = [NewsMediaInline]
    readonly_fields = ('author',)

    # لحفظ المستخدم الذي أضاف الخبر تلقائياً
    def save_model(self, request, obj, form, change):
        if not obj.pk: # عند الإنشاء فقط
            obj.author = request.user
        super().save_model(request, obj, form, change)

    def image_preview(self, obj):
        images = obj.media.all()
        image_list = []
        for media in images:
            if media.file:
                image_list.append(format_html('<img src="{}" style="height: 60px; width: auto; margin-right: 5px;" />', media.file.url))
        return format_html(''.join(image_list)) if image_list else "—"

    image_preview.short_description = 'الصور'
    
