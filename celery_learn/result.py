from celery.result import AsyncResult

from celery_learn.tasks import cel

async_result = AsyncResult(id='123',app=cel)
if async_result.successful():
    result = async_result.get()
    print(result)
elif async_result.failed():
    print('任务执行失败')
elif async_result.status == 'PENDING':
    print('任务正在执行')
elif async_result.status == 'started':
    print('任务已经执行')
elif async_result.status == 'RETRY':
    print('任务异常后正在重试')