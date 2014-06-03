from django.core.urlresolvers import reverse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import TemplateView
from django.core.urlresolvers import reverse_lazy
from .models import Feedback


class FeedbackCreate(CreateView):
    model = Feedback
    success_url = reverse_lazy('feedback:success')


class FeedbackSuccess(TemplateView):
    template_name = 'feedback/feedback_success.html'


'''
class AuthorUpdate(UpdateView):
    model = Author
    fields = ['name']

class AuthorDelete(DeleteView):
    model = Author
    success_url = reverse_lazy('author-list')
'''