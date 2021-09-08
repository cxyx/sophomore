from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .resource import *
from . import models

admin.site.site_header = 'sophomore管理后台'  # 设置header
admin.site.site_title = 'sophomore管理后台'  # 设置title
admin.site.index_title = 'sophomore管理后台'


# Register your models here.
# admin.site.register(models.UserProfile)
# admin.site.register(models.Permission)
# admin.site.register(models.Organization)
# admin.site.register(models.Role)
# admin.site.register(models.Menu)


@admin.register(models.Menu)
class MenuAdmin(ImportExportModelAdmin):
    resource_class = MenuResource
    list_display = ['name', 'icon', 'path', 'is_frame', 'is_show', 'sort', 'component', 'pid']
    search_fields = ['name', 'icon', 'path', 'is_frame', ]
    list_filter = ['name']
    list_per_page = 100


@admin.register(models.Permission)
class PermissionAdmin(ImportExportModelAdmin):
    resource_class = PermissionResource
    list_display = ['id', 'name', 'method', 'pid']
    search_fields = ['name', 'method']
    list_filter = ['name', 'method']
    list_per_page = 100


@admin.register(models.Role)
class RoleAdmin(ImportExportModelAdmin):
    resource_class = RoleResource
    list_display = ['id', 'name', 'desc']
    search_fields = ['name']
    list_filter = ['name']
    list_per_page = 100


@admin.register(models.Organization)
class OrganizationAdmin(ImportExportModelAdmin):
    resource_class = OrganizationResource
    list_display = ['id', 'name', 'type', 'pid']
    # list_display = '__all__'
    search_fields = ['name', 'type']
    list_filter = ['name', 'type']
    list_per_page = 100


@admin.register(models.UserProfile)
class UserProfileAdmin(ImportExportModelAdmin):
    resource_class = UserProfileResource
    list_display = ['username', 'mobile', 'email', 'image', 'department', 'position', 'get_roles_name']
    search_fields = ['name', 'mobile', 'position']
    list_filter = ['name', 'department']
    list_per_page = 100

    '''
    manytomany 字段无法直接展示在list_display中通过自定义就比较好看了
    '''
    def get_roles_name(self, obj):
        ghost_list = []
        for g in obj.roles.all():
            ghost_list.append(g.name)
        return ','.join(ghost_list)

    get_roles_name.short_description = "所属角色"
    # 指定排序字段,多数的函数没有排序的需求,加上比较好看(选择合适字段保持排序一直)
    get_roles_name.admin_order_field = "name"


@admin.register(models.WorkorderRole)
class WorkorderRoleAdmin(ImportExportModelAdmin):
    resource_class = WorkorderRoleResource
    list_display = ['id', 'name']
    # list_display = '__all__'
    list_per_page = 100