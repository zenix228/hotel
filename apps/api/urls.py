from django.contrib import admin
from django.urls import path,include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from rest_framework.routers import DefaultRouter

from .views import HotelViewSet, RoomViewSet, BookingViewSet, GuestViewSet

urlpatterns = [
#    path('post/', PostAPIView.as_view()),
#    path('post/<int:pk>/', PostDetailAPIView.as_view()),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
#    path('auth/', include('dj_rest_auth.urls')),
]

router = DefaultRouter()
router.register('hotel', HotelViewSet, basename='hotel')

router = DefaultRouter()
router.register('room', RoomViewSet, basename='room')

router = DefaultRouter()
router.register('booking', BookingViewSet, basename='booking')

router = DefaultRouter()
router.register('guest', GuestViewSet, basename='guest')

urlpatterns += router.urls      