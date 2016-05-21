from route import *

def main():
    # server_ip = raw_input('Enter server ip address: ')
    page = {'title' : 'IOT Trash Can'}
    app.run(host='0.0.0.0', port=8080, debug=True)

if __name__ == "__main__":
    main()
