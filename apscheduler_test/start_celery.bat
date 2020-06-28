celery -A apscheduler_test.main_1 worker -l info -P eventlet
# celery multi start logging/celery -A celery_tasks -l info -n bruce1 -Q app_task1
# celery beat -A celery_schedule -l info -f logging/schedule_tasks.log
# 后台运行,加参数"–detach"：
celery beat -A celery_schedule -l info -f logging/schedule_tasks.log --detach