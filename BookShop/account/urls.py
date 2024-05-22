from django.urls import path
from account import views

urlpatterns = [
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('registration/', views.RegisterView.as_view(), name='register'),
    path('registration/done/', views.RegisterDoneView.as_view(), name='register_done'),
    path('activate/<uidb64>/<token>/', views.ActivateView.as_view(), name='activate'),
]
