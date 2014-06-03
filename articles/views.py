# -*- coding:utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic import DetailView, ListView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Article


class ArticleListView(ListView):
    # Название переменной, которая будет содержать список записей
    context_object_name = 'article_list'
    # Имя шаблона для вывода списка (еще не создали)
    template_name = 'articles/article_list.html'

    def get_queryset(self):
        articles = Article.objects.all()
        paginator = Paginator(articles, 2)
        page = self.request.GET.get('page')
        try:
            articles = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            articles = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            articles = paginator.page(paginator.num_pages)
        return articles

class ArticleDetailView(DetailView):

    model = Article
    context_object_name = 'article'
    template_name = 'articles/article_detail.html'


# Наследуем функционал уже существующего класса, 
# который выводит список всех статей
class ArticleCategoryListView(ArticleListView):

    # Изменяем запрос, чтобы получить только статьи определенной категории
    def get_queryset(self):
        return Article.objects.filter(category__slug=self.kwargs['slug'])