from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .resource import *

admin.site.site_header = 'sophomore管理后台'  # 设置header
admin.site.site_title = 'sophomore管理后台'  # 设置title
admin.site.index_title = 'sophomore管理后台'


# Register your models here.
# admin.site.register(models.UserProfile)
# admin.site.register(models.Permission)
# admin.site.register(models.Organization)
# admin.site.register(models.Role)
# admin.site.register(models.Menu)


@admin.register(WorkOrder)
class WorkOrderAdmin(ImportExportModelAdmin):
    resource_class = WorkOrderResource
    list_display = ['number', 'title', 'content', 'type', 'status']
    search_fields = ['number', 'title', 'content', 'type', 'status']
    list_filter = ['number']
    list_per_page = 100