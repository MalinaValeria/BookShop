from django.views.generic import TemplateView


class Main(TemplateView):
    template_name = 'main.html'
    model = 'shop.Book'
    context_object_name = 'books'
