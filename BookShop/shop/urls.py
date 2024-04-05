from django.urls import path
from shop.views import Main

urlpatterns = [
    path('', Main.as_view(), name='main'),
]