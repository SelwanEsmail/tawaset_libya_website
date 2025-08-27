# news/translation.py

from modeltranslation.translator import translator, TranslationOptions

from modeltranslation.translator import register, TranslationOptions
from .models import News,Category,Project

@register(News)
class NewsTranslationOptions(TranslationOptions):
    fields = ('title', 'description')


class CategoryTranslationOptions(TranslationOptions):
    fields = ('name',) # الحقول اللي تبي تترجمها
class ProjectTranslationOptions(TranslationOptions):
    fields = ('name',) # الحقول اللي تبي تترجمها

translator.register(Category, CategoryTranslationOptions)
translator.register(Project, CategoryTranslationOptions)

    