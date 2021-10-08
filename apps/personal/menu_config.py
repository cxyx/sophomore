"""
    id                : 按钮
    -----------------------------
    submit            : 提交
    cancel            : 取消
    edit              : 编辑
    approve           : 审核
    final_approve     : 终审
    assign            : 分派
    rm_data_assign    : 脱敏
    finish            : (工单)完成
    excute_finish     : (执行)完成
    rm_data_finish    : (脱敏)完成
    comment           : 评论
    back              : 退回


"""
"""

脱敏流程探讨

1. 时间点
执行人完成工单后, 点击完成,直接提交给审核人
2. 尽量缩减按钮

3. 不可绕过
状态只展示当前以及状态前后状态, 没有前后则不展示
执行中:执行点击(执行)完成按钮(直接发送给初审人)==>待脱敏:初审人点击脱敏按钮(获取脱敏人名单,分派脱敏)
==>脱敏中:脱敏人点击(脱敏)完成按钮(发送给审核人)==>脱敏完成:点击完成

"""
menu = {
    # 环境新建
    "1": {
        # 示例 : 工单类型为"环境搭建"(type=1),在"工单状态"为"提交状态"的处理人能看到的"菜单"为["提交","编辑","评论"]
        "1": ["submit", "edit", "comment"],
        "2": ["approve", "finish", "commit"],
        "3": ["submit", "approve", "final_approve", "comment"],
        "4": ["submit", "approve", "final_approve", "comment"],
        "5": ["submit", "approve", "final_approve", "comment"],
        "6": ["submit", "approve", "final_approve", "comment"],
        "7": ["close", "comment"]
    },
    # 数据恢复
    "2": {
        "1": ["submit", "edit", "comment"],
        "2": ["approve", "finish", "comment"],
        "3": ["submit", "approve", "final_approve", "comment"],
        "7": ["close", "comment"]
    },

    "3": {
        "1": ["submit", "edit", "comment"],
        "2": ["approve", "finish", "comment"],
        "3": ["submit", "approve", "final_approve", "comment"],
        "7": ["close", "commit"]
    },
    "4": {
        "1": ["submit", "edit", "comment"],
        "2": ["approve", "finish", "comment"],
        "3": ["submit", "approve", "final_approve", "comment"],
        "7": ["close", "comment"]
    }
}

menus = {
    "1": {
        "1": ["submit", "edit", "commit"],
        "2": ["approve", "finish", "commit"],
        "3": ["submit", "approve", "final_approve", "commit"],
        "4": ["submit", "approve", "final_approve", "commit"],
        "5": ["submit", "approve", "final_approve", "commit"],
        "6": ["submit", "approve", "final_approve", "commit"],
        "7": ["close", "commit"]
    },
    "2": {
        "1": ["submit", "edit", "commit"],
        "2": ["approve", "finish", "commit"],
        "3": ["submit", "approve", "final_approve", "commit"],
        "7": ["close", "commit"]
    },
    "3": {
        "1": ["submit", "edit", "commit"],
        "2": ["approve", "finish", "commit"],
        "3": ["submit", "approve", "final_approve", "commit"],
        "7": ["close", "commit"]
    },
    "4": {
        "1": ["submit", "edit", "commit"],
        "2": ["approve", "finish", "commit"],
        "3": ["submit", "approve", "final_approve", "commit"],
        "7": ["close", "commit"]
    }
}

# def get_menu(workorder_type,status):
