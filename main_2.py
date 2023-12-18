import time
import atexit

from apscheduler.schedulers.background import BackgroundScheduler

# Declaration of the task as a function.
def print_date_time():
    print(time.strftime("%A, %d. %B %Y %I:%M:%S %p"))


# Create the background scheduler
scheduler = BackgroundScheduler()
# Create the job
scheduler.add_job(func=print_date_time, trigger="interval", seconds=3)
# Start the scheduler
scheduler.start()

# /!\ IMPORTANT /!\ : Shut down the scheduler when exiting the app
atexit.register(lambda: scheduler.shutdown())
