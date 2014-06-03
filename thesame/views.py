# -*- coding:utf-8 -*-

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.views.generic import ListView, DetailView, TemplateView
from articles.models import Article
from tariffs.models import Tariff
from slides.models import Slide
from works.models import Work
from pages.models import Page
from feedback.views import FeedbackCreate


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['posts_list_recent'] = Article.objects.all()
        context['tariffs_list'] = Tariff.objects.all()
        context['slides_list'] = Slide.objects.all()
        context['works_list'] = Work.objects.all()[:4]
        return context

class ContactsView(FeedbackCreate):

    template_name = 'two_columns.html'

    def get_context_data(self, **kwargs):
        context = super(ContactsView, self).get_context_data(**kwargs)
        page = get_object_or_404(Page, slug='contacts')
        context['page'] = page

        return context

'''
class PollDetailView(DetailView):
    model = Question
    template_name = 'polls/detail.html'

    def get_context_data(self, **kwargs):
        context = super(PollDetailView, self).get_context_data(**kwargs)
        user = User()
        user.ip = user.get_user_ip(self.request)
        user.question = Question.objects.get(pk=self.kwargs['pk'])
        # Передаем в шаблон переменную
        context['voted_already'] = user.voted_already()
        return context


class ResultsView(DetailView):
    model = Question
    template_name = 'polls/results.html'
    
'''