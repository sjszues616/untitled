import time
from datetime import datetime

from celery.result import AsyncResult

from apscheduler_test.main_1 import celery_app


def a():
    print('start-a')
    result = func.delay()
    async = AsyncResult(id=result.id, app=celery_app).id

    print('ok-a')
    print(result)


# @celery_app.task(bind=True, name='ccp_send_sms_code', retry_backoff=3)
@celery_app.task(name='ccp_send_sms_code')
def func():
    with open('./file123.txt','a',encoding='utf-8') as f:
        f.write(datetime.now().strftime('\n%Y-%m-%d %H:%M:%S') +'开始执行')
if __name__ == '__main__':
    a()
