from datetime import datetime
from celery_learn.tasks import send_email

# 方式一

#
# v1 = datetime(2020,6,15,22,55,00)
# v2 = datetime.utcfromtimestamp(v1.timestamp())
# result = send_email.apply_async(args=['egon'],eta=v2)

# 方式二

ctime =datetime.now()

utc_ctime = datetime.utcfromtimestamp(ctime.timestamp())
from datetime import timedelta
time_delay = timedelta(seconds=10)
task_time = utc_ctime + time_delay

# time_delay使用applay_async 设定时间
result = send_email.apply_async(args=['egon'],eta=task_time)
