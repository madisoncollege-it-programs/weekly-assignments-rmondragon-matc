#!/usr/bin/env python3

import sys
import requests,bs4
import argparse
import json
import socket

web_url  = "http://172.31.29.252/q2"
web_header = "http://172.31.29.252/q3"
web_values = "http://172.31.29.252/q4"
def get_response(myVar):
    get_response = requests.get("http://172.31.29.252/q1")
    print(get_response.text)


def parse_string(myVar):
    res = requests.get(web_url)
    res.raise_for_status()
    HTML = bs4.BeautifulSoup(res.text,features="html.parser")
    StripHTML = HTML.find_all(["h3"])
    Convert = str(StripHTML)
    print(f"ANSWER: {Convert[9]}{Convert[11]}{Convert[13]}{Convert[15]}{Convert[17]}{Convert[19]}{Convert[21]}{Convert[23]}{Convert[25]} Ryley Mondragon")
def parse_header(myVar):
    print(f"Function{myVar}")
    parser.add_argument('-f', '--function', dest='varFunction', default= '3', type=int, help="Function 3")
    print("Ryley Mondragon")
    print(f"http://{((parser.parse_args()).varString)}/q{((parser.parse_args()).varFunction)}")
    response = requests.get("http://172.31.29.252/q3")
    print(f"ANSWER:  {response.headers['MATC-HEADER']}")

def parse_json(myVar):
     webvalues = requests.get(f"http://172.31.29.252/q4")
     jsonVariable = json.loads(webvalues.text)
     jsonVariable2 = str(jsonVariable)
     for value in jsonVariable2:
         #jsonVariable3 = jsonVariable2.replace("{","").replace("}","").replace("]","").replace("[","")
         #print(jsonVariable3)
         jsonVariable3 = jsonVariable2.split("{")
         #print(jsonVariable4)
     for value in jsonVariable3:
         if "The Shining" in str(value):
             #print(value)
             jsonVariable5 = value.split(",")
             #print(jsonVariable5[1])
             jsonVariable6 = str(jsonVariable5[1])
             jsonVariable7 = jsonVariable6.replace("}","")
             #print(jsonVariable7)
             jsonVariable8 = jsonVariable7.split(":")
             #print(jsonVariable8[1])
             jsonVariable9 = str(jsonVariable8[1])
             #print(jsonVariable9)
             jsonVariable10 = jsonVariable9.replace("'","").replace(" ","")
             print("Ryley Mondragon")
             print(f"http://{((parser.parse_args()).varString)}/q{((parser.parse_args()).varFunction)}")
             print(f"ANSWER: {jsonVariable10}")
             


def socket_client(myVar):
    C_SOCK = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server = '172.31.29.253'
    for port in range(5000,6000):
        try:
             C_SOCK.connect((server,port))
             #print("The connection is successful")
             SND_DATA = "secret"
             RCV_DATA = ""
             C_SOCK.send(bytearray(SND_DATA, "UTF-8"))
             RCV_DATA = C_SOCK.recv(1024)
             print("Ryley Mondragon")
             print(f"http://{((parser.parse_args()).varString)}/q{((parser.parse_args()).varFunction)}")
             print(f"ANSWER: {RCV_DATA.decode()}")
             C_SOCK.close()
        except:
            pass

parser = argparse.ArgumentParser()
parser.add_argument('-i','--ipaddress',dest='varString', type=str,default='172.31.29.252', help='ip address')

Function = input("Which function number?")

if Function == "1":
    parser.add_argument('-f', '--function', dest='varFunction', default= '1', type=int, help= "Function number 1")
    print("Ryley Mondragon")
    print(f"http://{((parser.parse_args()).varString)}/q{((parser.parse_args()).varFunction)}")
    get_response("http://172.31.29.252/q1")
elif Function == "2":
    parser.add_argument('-f', '--function', dest='varFunction', default= '2', type=int, help="Function number 2")
    print("Ryley Mondragon")
    print(f"http://{((parser.parse_args()).varString)}/q{((parser.parse_args()).varFunction)}")
    res = requests.get(web_url)
    res.raise_for_status()
    HTML = bs4.BeautifulSoup(res.text,features="html.parser")
    StripHTML = HTML.find_all(["h3"])
    Convert = str(StripHTML)
    print(f"ANSWER: {Convert[9]}{Convert[11]}{Convert[13]}{Convert[15]}{Convert[17]}{Convert[19]}{Convert[21]}{Convert[23]}{Convert[25]} Ryley Mondragon")
elif Function == "3":
    parser.add_argument('-f', '--function', dest='varFunction', default= '3', type=int, help="Function 3")
    print("Ryley Mondragon")
    print(f"http://{((parser.parse_args()).varString)}/q{((parser.parse_args()).varFunction)}")
    response = requests.get("http://172.31.29.252/q3")
    print(f"ANSWER:  {response.headers['MATC-HEADER']}")
    

elif Function == "4":
    parser.add_argument('-f', '--function', dest='varFunction', default= '4', type=int, help="Function 4")
    webvalues = requests.get(f"http://172.31.29.252/q4")
    jsonVariable = json.loads(webvalues.text)
    jsonVariable2 = str(jsonVariable)
    for value in jsonVariable2:
        #jsonVariable3 = jsonVariable2.replace("{","").replace("}","").replace("]","").replace("[","")
        #print(jsonVariable3)
        jsonVariable3 = jsonVariable2.split("{")
        #print(jsonVariable4)
    for value in jsonVariable3:
        if "The Shining" in str(value):
            #print(value)
            jsonVariable5 = value.split(",")
            #print(jsonVariable5[1])
            jsonVariable6 = str(jsonVariable5[1])
            jsonVariable7 = jsonVariable6.replace("}","")
            #print(jsonVariable7)
            jsonVariable8 = jsonVariable7.split(":")
            #print(jsonVariable8[1])
            jsonVariable9 = str(jsonVariable8[1])
            #print(jsonVariable9)
            jsonVariable10 = jsonVariable9.replace("'","").replace(" ","")
            print("Ryley Mondragon")
            print(f"http://{((parser.parse_args()).varString)}/q{((parser.parse_args()).varFunction)}")
            print(f"ANSWER: {jsonVariable10}")
            
   

elif Function == "5":
    parser.add_argument('-f', '--function', dest='varFunction', default= '5', type=int, help="Function 5")
    C_SOCK = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server = '172.31.29.253'
    for port in range(5000,6000):
        try:
            C_SOCK.connect((server,port))
            #print("The connection is successful")
            SND_DATA = "secret"
            RCV_DATA = ""
            C_SOCK.send(bytearray(SND_DATA, "UTF-8"))
            RCV_DATA = C_SOCK.recv(1024)
            print("Ryley Mondragon")
            print(f"http://{((parser.parse_args()).varString)}/q{((parser.parse_args()).varFunction)}")
            print(f"ANSWER: {RCV_DATA.decode()}")
            C_SOCK.close()
        except:
            pass
            
args = parser.parse_args()

