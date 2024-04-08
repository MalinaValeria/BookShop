from django.views.generic import TemplateView

from shop.models import BookInfo


class Main(TemplateView):
    template_name = 'main.html'
    model = BookInfo
    context_object_name = 'books'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['new_books'] = self.model.objects.all().order_by('-publication_year')[:18]
        return context
