from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from . import views

urlpatterns = [
    path('emp/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('emp/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('empdet', views.empdetailsAPIView.as_view())
]
