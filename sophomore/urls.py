from django.contrib import admin
from django.urls import path, include
from rest_framework.documentation import include_docs_urls

from rest_framework import routers
from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings
# from django.contrib.auth import settings
from rest_framework.authtoken import views as api_view
# from apps.rbac.views import menu, organization, permission, role, user

# router = routers.SimpleRouter()
# router.register(r'menu', menu.MenuViewSet)
# router.register(r'organization', organization.OrganizationViewSet)
# router.register(r'permission', permission.PermissionViewSet)
# router.register(r'role', role.RoleViewSet)
# router.register(r'user', user.UserViewSet)

urlpatterns = [
    # path('', admin.site.urls),
    path('admin/', admin.site.urls),
    # path('api/', include(router.urls)),
    # path(r'docs/', include_docs_urls(title='sophomore')),

    path('rest-auth/', include('rest_auth.urls')),

    path('rbac/', include(('rbac.urls', 'rbac'), namespace='rbac')),
    path('personal/', include(('personal.urls', 'personal'), namespace='personal')),
    path('assets/', include(('assets.urls', 'assets'), namespace='assets')),
    path('operation/', include(('operation.urls', 'operation'), namespace='operation')),
]
