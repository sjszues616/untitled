celery worker -A celery_learn.celery_start_learn -l info -c 5
# celery 是通过模块找到 启动程序 -c 并发数

celery beat -A celery_learn.celery_start_learn

celery -B -A project worker -l info