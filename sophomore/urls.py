from django.contrib import admin
from django.urls import path, include
from apps.rbac.views1 import MyObtainTokenPairView
from rest_framework.routers import DefaultRouter
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_simplejwt.views import TokenRefreshView
from rest_framework.authtoken import views as api_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('token/', MyObtainTokenPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('rbac/', include(('rbac.urls', 'rbac'), namespace='rbac')),
    path('rest-auth/', include('rest_auth.urls')),

]
