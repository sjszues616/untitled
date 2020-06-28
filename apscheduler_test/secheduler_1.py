from apscheduler.schedulers.blocking import BlockingScheduler

scheduler = BlockingScheduler()


@scheduler.scheduled_job('cron', hour='8-23')
def request_update_status():
    print('Doing job')


scheduler.start()
