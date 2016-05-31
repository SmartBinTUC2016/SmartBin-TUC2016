from flask import *
import database
import comms
import random
import json
import urllib2

# Initialise Flask App
app = Flask(__name__)
app.secret_key = 'hello'

# Declare global variables
page = {}
session = {}

'''
Index Page
'''
@app.route('/')
def index():
    page['title'] = 'Overview'
    page['bins'] = '1'
    num_users = database.get_num_users()
    return render_template('index.html', page = page, num_users = num_users)

'''
Capacity Page
'''
@app.route('/capacity', methods=['GET','POST'])
def get_capacity():
    res = comms.get_data() # Retrieve data

    page['title'] = 'Capacity'
    # Data assignment to page variables
    if res['level'] != '?': # Check whether there was data received
        page['capacity'] = (res['weight']/1000 + res['level'])/2 # Calculate total current capacity
    else:
        page['capacity'] = '?'
    page['level'] = res['level']
    page['user'] = res['user']
    page['weight'] = res['weight']

    # Capacity Checking
    if page['capacity'] == '?':
        page['status'] = 'Connection error'
    elif page['capacity'] < 90:
        page['status'] = 'OK'
    elif page['capacity'] >= 90:
        page['status'] = 'FULL'
    return render_template('capacity.html', page = page)

'''
Users Page
'''
@app.route('/users')
def get_users():
    page['title'] = 'Users'
    users = database.get_users()
    return render_template('users.html', page = page, users = users)
