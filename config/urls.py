from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from accounts.views import UserViewSet, CustomTokenObtainPairView
from rest_framework_simplejwt.views import TokenRefreshView

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='users')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('CodingProblems.urls')),
    path('', include('submissions.urls')),
    path('', include('ChoicesProblems.urls')),
    path('', include('BlankProblems.urls')),
    path('', include('oxQuiz.urls')),
    path('', include('qna.urls')),
    path('auth/', include('djoser.urls')), # include Djoser's URLs
    path('auth/jwt/create/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/jwt/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
] + router.urls
