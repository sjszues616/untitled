
from celery import Celery


# 创建 celery 实例
celery_app = Celery('test1',backend='redis://localhost:6379/1',broker='redis://localhost:6379/1')

# 给 celery 添加配置
# celery_app.config_from_object('apscheduler_test.config')

# 让 celery_app 自动捕获目标地址下的任务
celery_app.autodiscover_tasks(['apscheduler_test',])