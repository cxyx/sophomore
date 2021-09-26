from django.shortcuts import render

# Create your views here.

from apscheduler.schedulers.background import BackgroundScheduler # 使用它可以使你的定时任务在后台运行
from django_apscheduler.jobstores import DjangoJobStore, register_events, register_job
import time
'''
date：在您希望在某个特定时间仅运行一次作业时使用
interval：当您要以固定的时间间隔运行作业时使用
cron：以crontab的方式运行定时任务
minutes：设置以分钟为单位的定时器
seconds：设置以秒为单位的定时器
'''

try:
    scheduler = BackgroundScheduler()
    scheduler.add_jobstore(DjangoJobStore(), "default")

    @register_job(scheduler, "interval", seconds=5,replace_existing=True)
    def test_job():
        # 定时每5秒执行一次
        print(time.strftime('%Y-%m-%d %H:%M:%S'))

        with open('/Users/cx/workspace/sophomore/apps/personal/text.txt','a+') as f:
            f.write(f'当前时间{time.asctime()}\r\n')

    register_events(scheduler)
    # 启动定时器
    scheduler.start()
except Exception as e:
    print('定时任务异常：%s' % str(e))
