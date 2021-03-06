from django.urls import path, include
from rest_framework.routers import DefaultRouter
from profile_api import views

router = DefaultRouter()
router.register('hello-viewset', views.HelloViewSet, base_name='hello_viewset')
router.register('profile', views.UserProfileViewSet)

urlpatterns = [
    path('hello-apiview/', views.HelloAPIView.as_view()),
    path('login/', views.UserLoginApiView.as_view()),
    path('', include(router.urls)),
]
