from flask import *
import ConfigParser
from comms import *
import random

app = Flask(__name__)
app.debug = True

page = {}
session = {}

@app.route('/')
def index():
    page['title'] = 'Welcome'
    page['bins'] = '1'
    page['users'] = str(random.randint(0,100))
    return render_template('index.html', page = page)

@app.route('/capacity', methods=['POST','GET'])
def get_capacity():
    page['title'] = 'Capacity'
    level = random.randint(0,100)
    page['level'] = str(level)
    page['weight'] = str(random.randint(0,10)) + 'kg'
    page['distance'] = str(random.randint(0,50)) + 'cm'
    if level > 90:
        page['status'] = 'FULL'
    else:
        page['status'] = 'OK'
    return render_template('capacity.html', page = page)

@app.route('/users')
def get_users():
    page['title'] = 'Users'
    return render_template('users.html', page = page)
