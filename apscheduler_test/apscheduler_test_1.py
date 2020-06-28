# coding=utf-8
"""
Demonstrates how to use the background scheduler to schedule a job that executes on 3 second
intervals.
"""

from datetime import datetime
import time
import os

from apscheduler.schedulers.background import BackgroundScheduler


def tick():
    print('Tick! The time is: %s' % datetime.now())


from apscheduler.schedulers.background import BackgroundScheduler


def isp_sync():
    print('isp_sync')


def kafka_sync():
    print('kafka_sync')


def workflow():
    print('workflow')


def detect_isp_access():
    print('isp_sync')


def mass_report():
    print('isp_sync')


def initialize_cron():
    apsched = BackgroundScheduler()
    apsched.add_job(isp_sync, 'cron', kwargs={}, hour=2, minute=10)
    apsched.add_job(kafka_sync, 'cron', hour=6, minute=10)
    apsched.add_job(workflow, 'cron', minute='*/10')
    apsched.add_job(detect_isp_access, 'cron', hour='*')
    apsched.add_job(mass_report, 'cron', minute='*/5')
    apsched.start()




if __name__ == '__main__':
    scheduler = BackgroundScheduler()
    scheduler.add_job(tick, 'cron', minute='*/30') # 间隔3秒钟执行一次
    scheduler.start()  # 这里的调度任务是独立的一个线程
    print('Press Ctrl+{0} to exit'.format('Break' if os.name == 'nt' else 'C'))

    try:
        # This is here to simulate application activity (which keeps the main thread alive).
        while True:
            time.sleep(2)  # 其他任务是独立的线程执行
            print('sleep!')
    except (KeyboardInterrupt, SystemExit):
        # Not strictly necessary if daemonic mode is enabled but should be done if possible
        scheduler.shutdown()
        print('Exit The Job!')