import logging
import time

log = logging.getLogger('django')

@app.task
def send_sms(mobile):
    print(f'向手机号{mobile}发送短信成功')
    time.sleep(5)
    return 'send_sms OK'
