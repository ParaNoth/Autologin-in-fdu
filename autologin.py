import os
import time
import requests
import getpass

Loginedin = True

username = input("input your UIS number:")
password = getpass.getpass("input your password:")
ip = input("input your ip address:")
url = 'https://****/include/auth_action.php'

data = [
  ('action', 'login'),
  ('username', username),
  ('password', password),
  ('ac_id', '1'),
  ('user_ip', ip),
  ('nas_ip', ''),
  ('user_mac', '')]
while True:
    connectted = os.system('ping 114.114.114.114 -n 1')
    if connectted !=0:
        if Loginedin == True:
            print("Trying to login...")
        Loginedin = False
    else:
        if Loginedin == False:
            print("Logined in")
        Loginedin = True

    if Loginedin == False:
        
        r =requests.post(url, data=data, verify=False)
        print(r.ok)

    time.sleep(30)