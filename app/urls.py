
# from django.urls import path
# from .views import UserDetailAPI,RegisterUserAPIView
# urlpatterns = [
#   path("get-details",UserDetailAPI.as_view()),
#   path('register',RegisterUserAPIView.as_view()),
# ]

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
