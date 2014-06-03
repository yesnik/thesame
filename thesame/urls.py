# -*- coding:utf-8 -*-
from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
admin.autodiscover()
from .views import IndexView, ContactsView


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'thesame.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^blog/', include('articles.urls', namespace='articles')),

    # Форма обратной связи
    url(r'^feedback/', include('feedback.urls', namespace='feedback')),
    
    url(r'^$', IndexView.as_view(), name='index'),

    url(r'^comments/', include('django.contrib.comments.urls')),

    url(r'^contacts/', ContactsView.as_view(), name='contacts'),

    url(r'^', include('pages.urls')),
 
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) \
+ static(r'(?:.*?/)?(?P<path>(css|jquery|js|images)/.+)$', document_root=settings.STATIC_ROOT)