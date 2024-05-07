from django.urls import path
from shop.views import Main, BookDetailView

urlpatterns = [
    path('', Main.as_view(), name='main'),
    path('book/<slug:slug>/', BookDetailView.as_view(), name='book'),
]