from django.urls import path
from . import views

urlpatterns = [
    path('',views.home),
    # path('',views.IndexView.as_view()),
    path('accounts/login/', views.login),
]