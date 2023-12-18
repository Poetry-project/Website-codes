import tweepy
import datetime
from flask import Flask, render_template

from apscheduler.schedulers.background import BackgroundScheduler

app = Flask(__name__)

# Twitter API credentials
CONSUMER_KEY = 'YOUR_CONSUMER_KEY'
CONSUMER_SECRET = 'YOUR_CONSUMER_SECRET'
ACCESS_TOKEN = 'YOUR_ACCESS_TOKEN'
ACCESS_TOKEN_SECRET = 'YOUR_ACCESS_TOKEN_SECRET'

# Twitter API object
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

# Function to tweet a message
def tweet(message):
    api.update_status(message)

# Function to schedule a tweet
def schedule_tweet(message, time):
    scheduler = BackgroundScheduler()
    # scheduler.add_job(tweet, args=[message], trigger='cron', day_of_week='mon-sun', hour=time.hour, minute=time.minute)
    # Create the job
    scheduler.add_job(func=print_date_time, trigger="interval", seconds=3)
    scheduler.start()


import time
# Declaration of the task as a function.
def print_date_time():
    print(time.strftime("%A, %d. %B %Y %I:%M:%S %p"))


# Function to get the current time
def get_current_time():
    now = datetime.datetime.now()
    return now


# Main function
if __name__ == '__main__':
    # Get the current time
    now = get_current_time()
    message = 'This is your daily tweet!'
    # Schedule a tweet for 12:00 PM
    schedule_tweet('This is your daily tweet!', now.replace(hour=12, minute=0, second=0, microsecond=0))    
    # Run the Flask app
    # app.run(debug=True)
    app.run()
