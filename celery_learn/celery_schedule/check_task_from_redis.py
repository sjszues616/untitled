from redis import Redis

r = Redis(db=1)
r.delete('celery')  # 删除历史遗留数据