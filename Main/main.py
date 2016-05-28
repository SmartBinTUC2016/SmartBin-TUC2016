from multiprocessing import Process
import Queue
from route import *
from database import *
from comms import *
import time


def main():
    # server_ip = raw_input('Enter server ip address: ')
    page = {'title' : 'IOT Trash Can'}
    datalistener = Process(target=jsonListener,args=())
    datalistener.start()
    app.run(host='0.0.0.0', port=8080, debug=True)
    datalistener.join()

if __name__ == "__main__":
    main()
