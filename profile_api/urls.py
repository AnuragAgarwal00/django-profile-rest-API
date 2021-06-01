from django.urls import path
from . import views

urlpatterns = [
    path('hello-apiview/', views.HelloAPIView.as_view()),
]
