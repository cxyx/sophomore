from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # path('', admin.site.urls),
    path('admin/', admin.site.urls),
    path('rbac/', include(('rbac.urls', 'rbac'), namespace='rbac')),
    path('personal/', include(('personal.urls', 'personal'), namespace='personal')),
    path('assets/', include(('assets.urls', 'assets'), namespace='assets')),
    path('operation/', include(('operation.urls', 'operation'), namespace='operation')),
]
