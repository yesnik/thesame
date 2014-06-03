# -*- coding:utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic import DetailView, ListView

from .models import Page


class PageListView(ListView):
    # Модель, список записей которой хотим выводить
    model = Page
    # Название переменной, которая будет содержать список записей
    context_object_name = 'page_list'
    # Имя шаблона для вывода списка (еще не создали)
    template_name = 'page_list.html'

class PageDetailView(DetailView):

    model = Page
    context_object_name = 'page'
    template_name = 'page_detail.html'


# Наследуем функционал уже существующего класса, 
# который выводит список всех статей
class PageCategoryListView(PageListView):

    # Изменяем запрос, чтобы получить только статьи определенной категории
    def get_queryset(self):
        return Page.objects.filter(category__slug=self.kwargs['slug'])