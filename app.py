import sqlite3
import os
import tweepy
from flask import Flask
from flask import request, render_template 
from generate_text  import GenerateText
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func
import datetime
from apscheduler.schedulers.background import BackgroundScheduler
import csv

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] =\
    'sqlite:///' + os.path.join(basedir, 'arabicPoetry.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Data(db.Model):
    # __table__ = db.Model.metadata.tables['data']
    id = db.Column(db.Integer, primary_key=True)
    poem_id = db.Column(db.Integer)
    poet_name = db.Column(db.String(256))
    poem_title = db.Column(db.String(100))
    poem_text = db.Column(db.Text)
    era = db.Column(db.String(256))
    country = db.Column(db.String(100))
    poem_style = db.Column(db.String(100))

    def __str__(self):
        return f'{self.poem_text}'
    

# Consumer keys and access tokens, used for OAuth 
CONSUMER_KEY = 'FxNZlsT4WoX6Ixhzkn18XgCs9'
CONSUMER_SECRET = 'UUmZ4fu0Vi6XKusN72jwOphlCDnyB6euiXQQaPDNf5aUFrdPKu'
ACCESS_KEY = '1710730988236443648-jcBeYvsnAPzfbiyWqHCkxpXowr54EW'
ACCESS_SECRET = 'tidb5vFB1Eo014yHEVFinx9rdhakK9dXJLByzHxrJ7Gnk'
      

@app.route('/', methods=['GET', 'POST'])
def main():
    if request.method == 'POST':
        # generate = []
        phrase = request.form["txt_generate"]
        # generate.append(phrase)
        # if phrase 
        # output = obj.predict(seed_text=phrase, seq_length=1000)
        output = obj.predict(seed_text= phrase , seq_length=1000)
        return render_template('result.html', result=output)
    return render_template('index.html')

@app.route('/features', methods=['GET', 'POST'])
def features():
    return (render_template('features.html'))

# background process happening without any refreshing
@app.route('/GenerateCustom', methods=['POST', 'GET'])
def GenerateCustom():
   if request.method == "POST":
        phrase = request.form['txtGenerate'] 
        # print (phrase)
        # print (' '.join(phrase))
        # phrase = 'واستباح'
        output = obj.predict(seed_text=' '.join(phrase), seq_length=100)     
        print (output)
        return output

@app.route('/PoetryTwitter', methods=['POST', 'GET'])
def PoetryTwitter():
    if request.method == "POST":
       # generate = []
       # tweet = request.form["txt_generate"] 
       phrase = request.form['txtGenerate'] 
       print (phrase)        
       output = obj.predict(seed_text=' '.join(phrase), seq_length=100)     
       output = obj.predict(seed_text= phrase, seq_length=100)  
       print (output)
       # Authenticate to Twitter
       client = tweepy.Client(
           consumer_key=CONSUMER_KEY,
           consumer_secret=CONSUMER_SECRET,
           access_token=ACCESS_KEY,
           access_token_secret=ACCESS_SECRET
       )
       # Post Tweet
       post_tweet = client.create_tweet(text=output)
       print (post_tweet)
       return  output

# background process happening without any refreshing
@app.route('/GenerateAi', methods=['POST', 'GET'])
def GenerateAi():    
    row = Data.query.order_by(func.random()).first()
    # print(row)
    phrase = str(row).split()[:3]
    print (phrase)
    print (' '.join(phrase))
    # print (phrase)
    # print (' '.join(phrase))  
    # phrase = 'واستباح'
    output = obj.predict(seed_text=' '.join(phrase), seq_length=100)     
    return output

@app.route('/login', methods=['GET', 'POST'])
def login():
    return (render_template('login.html'))

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    return (render_template('signup.html'))

@app.route('/about', methods=['GET'])
def about():
    return (render_template('about.html'))

def createDb():
    PATH_TO_CSV = 'dataset/new_dataset.csv'    
    # url = 'https://drive.google.com/file/d/1CJ6vIcgtw84qJeelklolsSBKbEg7RpX1/view?usp=drive_link'
    
    if not os.path.exists('arabicPoetry.db'):
        # if os.path.exists(PATH_TO_CSV):
        # Connecting to the geeks database
        connection = sqlite3.connect('arabicPoetry.db')
        # Creating a cursor object to execute
        # SQL queries on a database table
        cursor = connection.cursor()
        # Table Definition
        # poem_id,poet_name,poem_title,poem_text,era,country,poem_style
        create_table = '''CREATE TABLE if not exists data(
                                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                                            poem_id  INTEGER NOT NULL,
                                            poet_name TEXT NOT NULL,
                                            poem_title TEXT NOT NULL,
                                            poem_text TEXT NOT NULL,
                                            era TEXT NOT NULL,
                                            country TEXT NOT NULL,
                                            poem_style TEXT NOT NULL
                                        ); '''

        # Creating the table into our
        # database
        cursor.execute(create_table)
        # Opening the person-records.csv file
        file = open(PATH_TO_CSV, encoding='utf-8-sig')
        # Reading the contents of the
        # person-records.csv file
        contents = csv.reader(file )
        # contents = pd.read_csv(file , encoding='utf-8-sig' , nrows=1000)
        # SQL query to insert data into the
        # person table
        insert_records = "INSERT INTO data (poem_id,poet_name,poem_title,poem_text,era,country,poem_style) VALUES(?, ?, ?, ?, ?, ?, ?)"
        # # Importing the contents of the file
        # # into our person table
        # cursor.executemany(insert_records, contents)
        row_count = 0
        for row in contents:
           row_count += 1
           cursor.execute(insert_records,row)
           if row_count == 10000:
              break
        # # Committing the changes
        connection.commit()
        # # closing the database connection
        connection.close()
    else:
        print("Pleas load the dataset file csv")


import time
# Declaration of the task as a function.
def print_date_time():
    print(time.strftime("%A, %d. %B %Y %I:%M:%S %p"))

# Function to get the current time
def get_current_time():
    now = datetime.datetime.now()
    return now

# Function to tweet a message
def tweet(): 
    with app.app_context():
        row = Data.query.order_by(func.random()).first()       
        print (row)
        phrase = str(row).split()[:3]
        print (phrase)
        message = obj.predict(seed_text=' '.join(phrase), seq_length=100)       
        # Authenticate to Twitter
        client = tweepy.Client(
            consumer_key=CONSUMER_KEY,
            consumer_secret=CONSUMER_SECRET,
            access_token=ACCESS_KEY,
            access_token_secret=ACCESS_SECRET
        )
        # Post Tweet
        client.create_tweet(text=message)


scheduler = BackgroundScheduler()
#scheduler.add_job(update_data, 'interval', hours=1) # for hour
scheduler.add_job(tweet, 'interval', seconds= 120) # for two mimute 2x60
scheduler.start()



if __name__ == '__main__':     
    # Get the current time  
    createDb()
    obj = GenerateText()        
    app.secret_key = "123456"    
    app.run() 
    