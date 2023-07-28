# Import flask
from flask import Flask, request
import praw
from random import randint

# Create your app (web server)
app = Flask(__name__)


# When people visit the home page '/' use the hello_world function
@app.route('/')
def hello_world():
    return 'Hello, World!'

# You can access demobot’s greet command via <your website>/greet
# Slack can message “hi bot” via <your website>/greet
@app.route('/greet', methods=['GET', 'POST'])
def greet_person():
    # Get the value of the 'name' query parameter
    # request.values is a dictionary (cool!)
    name = request.values.get('text')
    # This bot says hi to every name it gets sent!

    return f'Hi {name} my name is ShowerBot. Nice to meet you!'

@app.route('/temp', methods=['GET', 'POST'])
def temperature():
    temp = request.values.get('text')

    try:
        if int(temp) >= 30:
            return 'It\'s so hot!'
        else:
            return f'It\'s {temp} degrees!'
    
    except:
        return 'Please give a valid temperature'

@app.route('/showerbot', methods=['GET', 'POST'])
def showerbot():
    r = praw.Reddit(username='Fuzzy_Operation',
                    password='password',
                    client_id='WyGJqOVYj6BN2A',
                    client_secret='4I7ADyN3rSW5I03JaoK0fLzHm4s',
                    user_agent='testing reddit')

    try:
        n = 20
        rand = randint(0,n-1)
        l = []
        for submissions in r.subreddit('showerthoughts').top(time_filter='hour',limit=n):
            l.append(submissions.title)

        return l[rand]

    except:
        return 'I\'m sorry that request failed'

if __name__ == '__main__':
    # Start the web server!
    app.run()