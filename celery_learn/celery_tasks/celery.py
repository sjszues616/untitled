from celery import Celery


include_task =['celery_learn.celery_tasks.task01','celery_learn.celery_tasks.task02']
cel = Celery('celery_demo',
             backend='redis://127.0.0.1:6379/1',
             broker='redis://127.0.0.1:6379/2',
             include=include_task)

cel.conf.timezone = 'Asia/Shanghai'
cel.conf.enable_utc = False