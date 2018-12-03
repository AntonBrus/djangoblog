from django.contrib import admin
from .models import Article, Comment, Tag

# Register your models here.
admin.site.register(Article)
admin.site.register(Comment)


# Настройка колонок
class TagAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')


# Tags register
admin.site.register(Tag, TagAdmin)