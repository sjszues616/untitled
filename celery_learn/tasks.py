"""
user 生产者
broker 消息中间件 redis rabitterMQ
worker 任务的消费者
flower

"""

import celery
import time

# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

backend = 'redis://127.0.0.1:6379/1'
broker = 'redis://127.0.0.1:6379/2'

cel=celery.Celery('test',backend=backend,broker=broker)


@cel.task
def send_email(name):
    print('xiang%s发送短信....'%name
          )
    time.sleep(2)
    print('向%s发送短信完成'%name)
    return 'OK'