from django.contrib import admin
from .models import Project
from .models import News, NewsMedia,Category
# news/admin.py
from django.utils.html import format_html

from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.admin import GroupAdmin as BaseGroupAdmin
from django.contrib.auth.models import User, Group

from unfold.forms import AdminPasswordChangeForm, UserChangeForm, UserCreationForm
from unfold.admin import ModelAdmin


from import_export.admin import ImportExportModelAdmin
from unfold.contrib.import_export.forms import ExportForm, ImportForm, SelectableFieldsExportForm



admin.site.unregister(User)



@admin.register(User)
class UserAdmin(BaseUserAdmin, ModelAdmin):
    # Forms loaded from `unfold.forms`
    form = UserChangeForm
    add_form = UserCreationForm
    change_password_form = AdminPasswordChangeForm



@admin.register(Project)
class ProjectAdmin(ModelAdmin,ImportExportModelAdmin):

    list_display = ('name', 'created_at')
    search_fields = ('name',)
    
    import_form_class = ImportForm
    export_form_class = ExportForm

class NewsMediaInline(admin.TabularInline):
    model = NewsMedia
    extra = 1 # عدد الحقول الفارغة للوسائط الجديدة

@admin.register(News)
class NewsAdmin(ModelAdmin,ImportExportModelAdmin):

    list_display = ('title', 'category','created_at')
    search_fields = ('title', 'description')
    list_filter = ('author', 'created_at')
    inlines = [NewsMediaInline]
    readonly_fields = ('author',)

    import_form_class = ImportForm
    export_form_class = ExportForm

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


@admin.register(Category)
class CategoryAdmin(ModelAdmin,ImportExportModelAdmin):
    list_display = ('name',)
    # prepopulated_fields = {"slug": ("name",)}  # يملأ الـ slug تلقائياً من الاسم