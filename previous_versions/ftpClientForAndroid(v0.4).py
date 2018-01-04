"""
Purpose:
    A useless project. This project is a simple ftp client. 
    opps i just realised Android has no default way to connect to FTP, so this script will be used as a ftp client on android in the android terminal. (SL4A or Scripting Layer for Android)

Basic Functions:
    *Upload Files
    *Download Files
    *List all files and folders on the server and in local directory
    *Change directory on server and local

Update Notes:
    -All basic functions have been completed (Date: 21 January 2017, Day: Saturday, Time: 17:19:20)
    -Logic Part is still in development. (Date: 21 January 2017, Day: Saturday, Time: 20:15:00)
    -Added 2 new commands help and clear. Self explaiatory. (Date: 22 January 2017, Day: Sunday, Time: 09:06:30)
    -Added 3 new commands send, download, zip. Send will send files, download will get files from FTP and zip will zip a folder and then send that to ftp. (Date: 22 January 2017, Day: Sunday, Time: 11:24:50)
    -Script Tested on Android. Works flawlessly only a few errors that will occur or any platform need fixing. (Date: 22 January 2017, Day: Sunday, Time: 11:50:50)

Development Progress:
    -Script In development 0.1v (Date: 21 January 2017, Day: Saturday, Time: 20:15:00)
    -Script In development 0.4v (Date: 22 January 2017, Day: Sunday, Time: 11:24:50)

Planned Additions:
    *A delete command. Delete any file/folder on FTP
    *A make command. Make a folder on FTP.
    *Organize all command outputs.
    *Except error when connecting to an ip that is not available. OSError
    *Except error when lcd/scd to a directory that does not exist.
"""

'''-------------------------------------------------------Libraries--------------------------------------------------'''

import os
from ftplib import FTP
import zipfile
import sys
import getpass

'''-------------------------------------------------------Functions-------------------------------------------------------------------------'''

def zipfolder(foldername, target_dir):#This function is used to Zip a folder and then send it over to the ftp
    query1 = input("Would you like to unzip it on the server?(y/n): ")
    if query1 == 'y':            
        zipobj = zipfile.ZipFile(foldername + 'Unzip.zip', 'w', zipfile.ZIP_DEFLATED)#I did not make this function for the record
        rootlen = len(target_dir) + 1
        for base, dirs, files in os.walk(target_dir):
            for file in files:
                fn = os.path.join(base, file)
                zipobj.write(fn, fn[rootlen:])
        send(foldername, "Unzip.zip")
    else:
        zipobj = zipfile.ZipFile(foldername + '.zip', 'w', zipfile.ZIP_DEFLATED)#I did not make this function for the record
        rootlen = len(target_dir) + 1
        for base, dirs, files in os.walk(target_dir):
            for file in files:
                fn = os.path.join(base, file)
                zipobj.write(fn, fn[rootlen:])
        send(foldername, "zip")
        

def send(filename, extention):#This function is used to send files or .zip files to the ftp.
    file = open('%s.%s' % (filename, extention) , 'rb')
    ftp.storbinary('STOR %s.%s' % (filename, extention), file)
    file.close()
    print("Sent to ", ftp.pwd())

def download(filename, extention):#This function is to retrieve or download a file from the ftp.
    file = open("%s.%s" % (filename, extention), "wb")
    ftp.retrbinary("RETR %s.%s" % (filename, extention), file.write)
    file.close()
    print("Downloaded to ", os.getcwd())

def sls():#sls stands for Server List, it is the ls command but for server side. It lists all directories and files on the server.
    serverList = ftp.nlst()
    print("\n".rstrip())
    for fileN in serverList:
        print(fileN)
    print("\n".rstrip())

def lls():#lls stands for Local List, it is the ls command but on local mechine.
    localList = os.listdir(os.getcwd())
    print("\n".rstrip())
    for fileN in localList:
        print(fileN)
    print("\n".rstrip())

def scd(path):#scd stands for Server Change Directory. cd command but for server.
    print("Old Server Working Directory: {}".format(ftp.pwd()))
    ftp.cwd(path)
    print("New Server Working Directory: {}".format(ftp.pwd()))

def lcd(path):#lcd stands for Local Change Directory. cd command but for local mechine.
    print("Old Local Working Directory: {}".format(os.getcwd()))
    os.chdir(path)
    print("New Local Working Directory: {}".format(os.getcwd()))

'''---------------------------------------------------------------Logic-------------------------------------------------------------------'''
print("Welcom to FTP Made with python. Type help for command list.")
help = ['lls - command to get local directory list','connect - command to connect to ftp via port 21','sls - command to get server ','exit, bye - to quit','scd - to change directroy on server','lcd - to change directory on local mechine', 'send - to send file.', 'zip - to zip a folder and send it.', 'download, get, retrieve - Downloads a file from the server']                 
ftp = FTP()
while True:
    command = input("ftp$ ")
    command = command.split()
    command[0] = command[0].lower()
    if command[0] == "lls":
        lls()
    elif command[0] == "connect":
        try:
            ftp.connect(command[1], 21)
            result = ftp.login(input("Enter Username: "), getpass.getpass("Enter Password: "))#Username and password are not stored.  
            if result == "230 User logged in.":
                print("Login success.")
            else:
                print(x)
                print("Login failed check username and password.")          
        except IndexError:
            ftp.connect(input("Enter Server IP: "), 21)
            result =    ftp.login(input("Enter Username: "), getpass.getpass("Enter Password: "))#Username and password are not stored.
            if result == "230 User logged in.":
                print("Login success.")
            else:
                print(x)
                print("Login failed check username and password.")            
    elif command[0] == "sls":
        try:
            sls()
        except:
            print("Some error has occurred, try to re/connect to the ftp.")
    elif command[0] == "exit" or command[0] == "bye":#Program exits regardless of connection to ftp if command is typed.
        exit()
    elif command[0] == "scd":
        try:
            scd(command[1])
        except IndexError:
            try:
                print("Current server working directory: ",ftp.pwd())
            except:
                print("Some error has occurred, try to re/connect to the ftp.")
    elif command[0] == "lcd":
        try:
            lcd(command[1])
        except IndexError:
            print("Current local working directory: ", os.getcwd())
    elif command[0] == "clear":
        os.system("clear")
    elif command[0] == "help":
        print("\n".rstrip())
        for cm in help:
            print(cm)
        print("\n".rstrip())
    elif command[0] == "send":
        filex = command[1].replace(".", " ")
        filex = filex.split()
        print(filex)
        try:
            send(filex[0], filex[1])
        except FileNotFoundError:
            print("The file was not found.")
    elif command[0] == "zip":
        zipfolder(command[1], command[1])
    elif command[0] == "retrieve" or command[0] == "get" or command[0] == "download":
        filex = command[1].replace(".", " ")
        filex = filex.split()
        try:
            download(filex[0], filex[1])
        except:
            print("Something went wrong, make sure the file name is correct.")
    else:
        print("{} command not found. Type help for command list.".format(command[0]))

 
