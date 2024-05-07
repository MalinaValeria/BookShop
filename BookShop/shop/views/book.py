from django.views.generic import DetailView

from shop.models import BookInfo


class BookDetailView(DetailView):
    model = BookInfo
    template_name = 'book_detail.html'
    context_object_name = 'book'




