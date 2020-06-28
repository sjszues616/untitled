from datetime import timedelta

from celery import Celery
from celery.schedules import crontab

include_task =['celery_learn.celery_tasks.task01','celery_learn.celery_tasks.task02']
cel = Celery('celery_demo',
             backend='redis://127.0.0.1:6379/1',
             broker='redis://127.0.0.1:6379/2',
             include=include_task)

cel.conf.timezone = 'Asia/Shanghai'
cel.conf.enable_utc = False

cel.conf.beat_schedule = {
    'add-every-10-seconds':{
        'task':'celery_task.task01.send_email',
        # 'schedule':1.0,
        # 'schedule':crontab(minute="*/1"),
        'schedule': timedelta,
        'args': ('zhangsan')
    },
    'add-every-12-seconds':{
        'task':'celery_task.task01.send_email',
        'schedule':crontab(minute=42,hour=7,day_of_month=11,month_of_year=4),
        'args': ('wangwu')
    }
}