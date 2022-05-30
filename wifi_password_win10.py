"""  
Import modules
"""
import subprocess
import re
from time import sleep
from art import *
""" 
Say greetting
"""
def hello():
    tprint("CISCO_DEV")
    print("\n****************************************************************")
    print("\n* Copyright of Francis ALAPHIA, 2022                              *")
    print("\n* francisalaphia5@gmail.com                                  *")
    print("\n* https://www.youtube.com/cisco_dev                          *")
    print("\n****************************************************************")
    print("SSID\t\t\t\tPASSWORD\t\t\tSTATUT")
    print("_________________________________________________________")

""" 
Get password from machine
"""
def getPassword():
    command_output = subprocess.run(["netsh", "wlan", "show", "profiles"], capture_output = True).stdout.decode('utf-8',errors='ignore')
    splitArr =command_output.splitlines()
    writable = []

    for x in splitArr:
        if x !="" and re.findall("Profil Tous",x):
            wifi_ssid = x.split(":")[1]
            find_wifi_info = subprocess.run(["netsh","wlan","show", "profile",f'{wifi_ssid.strip()}'],capture_output=True).stdout.decode('utf-8',errors='ignore')
            has_key = re.search('Cl de scurit: Prsent', find_wifi_info)
            if(has_key!=None):
                find_wifi_key = subprocess.run(["netsh","wlan","show", "profile",f'{wifi_ssid.strip()}', "key=clear"],capture_output=True).stdout.decode('utf-8',errors='ignore')
                wifi_key = re.findall("Contenu de la cl (.*):(.*)\r",find_wifi_key)[0]

                result = f'{wifi_ssid} ===> {wifi_key[1]}'
                writable.append(result)
                print(f"{wifi_ssid}\t\t\t{wifi_key[1]}\t\t\tcracké")

    with open("wifi_code.txt","w+") as file:
        for w in writable:
            file.writelines(w+'\n')

if __name__ == "__main__":
    hello()
    sleep(2)
    getPassword()