from apscheduler.schedulers.background import BackgroundScheduler
from flask import Flask


scheduler = BackgroundScheduler()

def job():
    print("Scheduled job executed")

scheduler.add_job(job, 'interval', hours=2)

scheduler.add_job(job, 'cron', hour=14)

#hour=14 means" 2 PM "

@app.before_first_request
def start_scheduler():
    scheduler.start()


@app.teardown_appcontext
def stop_scheduler(exception=None):
    scheduler.shutdown()

    