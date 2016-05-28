import psycopg2
import psycopg2.extras
import ConfigParser
import comms
import time

#####################################################
##  Database Connect
#####################################################
sessionUser = None
def database_connect():
    # Read the config file
    config = ConfigParser.ConfigParser()
    config.read('config.ini')

    # Create a connection to the database
    connection = None
    try:
        connection = psycopg2.connect(database=config.get('DATABASE','database'),
            user=config.get('DATABASE','user'),
            password=config.get('DATABASE','password'),
            host=config.get('DATABASE','host'))
    except psycopg2.OperationalError as e:
        print("""Error, you haven't updated your config.ini or you have a bad
        connection, please try again. (Update your files first, then check
        internet connection)
        """)
        print(e)
    #return the connection to use
    return connection

def get_users():
    conn = database_connect()
    if conn is None:
        print 'No Connection'
        return
    cur = conn.cursor(cursor_factory = psycopg2.extras.RealDictCursor)
    query = 'SELECT * FROM smartbin.user ORDER BY user_id'

    try:
        cur.execute(query)
        res = cur.fetchall()
        cur.close
        conn.close
        return res
    except Exception as e:
        print e
    cur.close()
    conn.close()
    return None

'''
GET NUMBER OF USERS
'''
def get_num_users():
    conn = database_connect()
    if conn is None:
        print 'No Connection'
        return
    cur = conn.cursor(cursor_factory = psycopg2.extras.RealDictCursor)
    query = 'SELECT COUNT(*) FROM smartbin.user'

    try:
        cur.execute(query)
        res = cur.fetchall()
        cur.close
        conn.close
        return res
    except Exception as e:
        print e
    cur.close()
    conn.close()
    return None
'''
UPDATE USER
'''
def updateUser(user):
    tempUser = user
    global sessionUser
    if sessionUser != tempUser:
        sessionUser = tempUser
        conn = database_connect()
        if conn is None:
            print 'No Connection'
            return
        cur = conn.cursor()
        try:
            query = 'UPDATE smartbin.user SET rubbishcount = rubbishcount + 1 WHERE user_id = %s;'
            cur.execute(query, (sessionUser,))
            conn.commit()
            cur.close()
            conn.close()
            return
        except Exception as e:
            print e
        cur.close()
        conn.close()
    return None
