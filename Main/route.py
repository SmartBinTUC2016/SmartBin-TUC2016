from flask import *
# import configparser
# from comms import *
import random
import json
import urllib2


app = Flask(__name__)
app.secret_key = 'hello'

page = {}
session = {}

@app.route('/')
def index():
    page['title'] = 'Overview'
    page['bins'] = '1'
    page['users'] = str(random.randint(0,100))
    return render_template('index.html', page = page)

@app.route('/capacity', methods=['GET','POST'])
def get_capacity():
    # if urllib2.Request.get_method == 'GET':
    res = urllib2.urlopen('http://192.168.1.49:80')
    res = json.loads(res.read())
    page['title'] = 'Capacity'
    level = random.randint(0,100)
    page['level'] = res['Capacity']
    page['weight'] = str(random.randint(0,10)) + ' kg'
    page['distance'] = str(random.randint(0,50)) + ' cm'
    if level > 90:
        page['status'] = 'FULL'
    else:
        page['status'] = 'OK'
    return render_template('capacity.html', page = page)

@app.route('/users')
def get_users():
    page['title'] = 'Users'
    return render_template('users.html', page = page)
