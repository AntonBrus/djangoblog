from django.shortcuts import render, redirect
from .models import Article, Comment
from . import forms
# Create your views here.


def post_list(request):
    articles = Article.objects.all().order_by('date')
    return render(request, 'post_list.html', {'articles': articles})


def post_detail(request, slug):
    # Получение статьи
    article = Article.objects.get(slug=slug)

    # Сохранение комментария
    if request.method == 'POST':
        form = forms.CreateComment(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.article = article
            instance.save()
            return  redirect(request.get_full_path())

    # Получение связанных комментариев
    comments = Comment.objects.filter(article=article)

    # Получение уже готовой формы для вставки в тег form
    form = forms.CreateComment()

    return render(request, 'post_detail.html', {'article': article, 'comments': comments, 'form': form})