import time

from celery_learn.celery_tasks.celery import cel



@cel.task
def send_email(name):
    print('xiang%s发送短信....' % name)
    time.sleep(2)
    print('向%s发送短信完成' % name)
    return 'OK2'