# Telstra University Challenge: __Smart Bin__

## Requirements
The program is written in Python 2 and requires
the following libraries are required for the web app to function:

* Flask
* Psycopg2

These can be installed through pypi(pip) tool using the following commands:

```sh
pip install Flask
```

and 

```sh
pip install psycopg2
```

## Instructions

To run the code to initiate the web server, go to the Main folder in the terminal and type in 

```sh
python main.py
```

This will start the web server that hosts the web app. The web app is then accessed using either localhost or the computer's IP address on port **8080**.
If you are accessing using the localhost then enter the following in your web browser

```
http://127.0.0.1:8080
```

The IP address connection to the bin is hardcoded into the code, so in order to connect to the bin the IP address in the comms.py must be modified to match the IP assigned to the bin which can vary between networks. Our default IP address currently is **192.168.1.49**.


## Acknowledgements
I would like to thank not only team members who were involved in this project for their contribution and support but also those who have supported the team in transportation and catering and a workshop for us to work in. All of this would not have been possible without everyone involved. 