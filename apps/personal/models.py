from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()
# Create your models here.

'''
之前被限定住了

工单角色 : 用来为下拉筛选框提供可选择对象

工单权限 : 之前是当前处理人+工单状态+工单类型 = 工单权限
    设计思路两种 : 
        1. 设计工单权限表,根据工单状态+工单类型获取工单权限
        2. 直接在工单表中加字段
'''


class WorkOrder(models.Model):
    type_choices = (
        ('1', '环境申请'),
        ('2', '数据恢复'),
        ('3', '故障处理'),
        ('4', '服务请求'),
    )

    status_choices = (
        ('1', '待提交'),
        ('2', '待审核'),
        ('3', '执行中'),
        ('4', '待脱敏'),
        ('5', '脱敏中'),
        ('6', '已脱敏'),
        ('7', '待确认'),
        ('8', '已关闭'),
    )
    number = models.CharField(max_length=30, unique=True, verbose_name="工单号", help_text="工单号")
    title = models.CharField(max_length=30, unique=True, verbose_name="工单标题", help_text="工单标题")
    content = models.CharField(max_length=30, unique=True, verbose_name="工单内容", help_text="工单内容")
    # paso_name = models.ForeignKey(max_length=30, unique=True, verbose_name="工单内容",help_text="工单内容")
    type = models.CharField(max_length=30, choices=type_choices, default='0', verbose_name="工单类型", help_text="工单类型")
    status = models.CharField(max_length=30, choices=status_choices, default='0', verbose_name="工单状态", help_text="工单状态")
    is_show = models.BooleanField(blank=True, null=False, default=True, verbose_name='是否显示')
    is_return = models.BooleanField(blank=True, null=False, default=True, verbose_name='是否退回')
    add_time = models.DateTimeField(null=True, blank=True, verbose_name="创建时间")
    expect_time = models.DateTimeField(null=True, blank=True, verbose_name="期望时间")
    approve_time = models.DateTimeField(null=True, blank=True, verbose_name="审核时间")
    complete_time = models.DateTimeField(null=True, blank=True, verbose_name="完成时间")
    target_time = models.DateTimeField(null=True, blank=True, verbose_name="目标时间")

    todoer = models.ForeignKey(User, related_name='todoer', blank=True, null=True, on_delete=models.SET_NULL,
                               verbose_name='当前处理人')
    proposer = models.ForeignKey(User, related_name='proposer', blank=True, null=True, on_delete=models.SET_NULL,
                                 verbose_name='申请人')
    approver = models.ForeignKey(User, related_name='approver', blank=True, null=True, on_delete=models.SET_NULL,
                                 verbose_name='审批人')

    # receiver = models.ForeignKey('User',related_name='receiver',blank=True, null=True,on_delete=models.SET_NULL,verbose_name='接单人')

    @property
    def get_menus(self):
        def get_menu_config_dict():
            return {}

        todoer_roles = self.todoer.workorder_role.values_list()

        type = self.type
        status = self.status
        type = str(int(type) + 0.5) if "final_approve" in todoer_roles and 1 else type

        menu_list = get_menu_config_dict[type][status]

        return menu_list


class EnvCreateOrder(models.Model):
    type = "环境新建"


class DbRecoveryOrder(models.Model):
    type = "数据恢复"


class FaultResolveOrder(models.Model):
    type = "故障处理"
