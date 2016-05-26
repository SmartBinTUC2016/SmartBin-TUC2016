from multiprocessing import Process
from route import *
from comms import *
from database import *
import time

def main():
    # server_ip = raw_input('Enter server ip address: ')
    print('=================================')
    print('= Starting IOT Smart Bin Server =')
    print('=================================')
    page = {'title' : 'IOT Trash Can'}
    datalistener = Process(target=jsonListener,args=())
    userAutoUpdate = Process(target=updateUser,args=())
    datalistener.start()
    time.sleep(3)
    userAutoUpdate.start()
    app.run(host='0.0.0.0', port=8000, debug=True)
    datalistener.join()
    userAutoUpdate.join()

if __name__ == "__main__":
    main()
