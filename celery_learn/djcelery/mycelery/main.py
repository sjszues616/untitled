import os

from celery import Celery
# 创建celery示例
app = Celery('djcelery')
# 把celery和django结合 识别和加载django的配置文件
os.environ.setdefault('DJANGO_SETTINGS_MODULE','celerypros.settings.dev')
# 通过app对象加载配置

app.config_from_object('mycelery.config')
#加载任务
# 参数必须是个列表 里面的每个任务都是任务的路径名称

app.autodiscover_tasks(['myceler.sms'])

# 启动celery
# 强烈建议切换到mycelery目录下启动
# celery -A mycelery.main worker --loglevel=info
