"""
Tannishpage is the developer of this script. All rights go to Tannishpage

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
    ------Initial Released------- (Date: 22 January 2017, Day: Sunday, Time: 11:50:50) (Version 0.4)

    -Added authentication just incase someone tries to do something bad to my ftp. (Date: 23 January 2017, Day: Monday, Time: 09:41:40)
    -Now password is saved in a variable using getpass.getpass(). It is understoood that this is a security risk but if this is undone another security risk emerges. that is someone could send malicious files to an ftp on someother persons account.
        Eg: you login to your ftp and then you leave the computer to go and get a glass of wather. But then your friend uploads a malicious file on to the FTP on your name before you come back.
            If the authentication is in place then your firend cannot upload or download files from that ftp with out the password.
            But someone who gets access to the source code could make some samll changes to make it a security risk. But at this stage that is not as big of an issue.
    -Zipfolder function has been hot fixed. The issue was that an extra dot was added during opening the file in the send function. So the sending when the unzip option is selected is done speratly outside the send function.
    -Function delete() has been added. It will delete a file on the FTP when called. Function not tested (Date: 25 January 2017, Day: Wednesday, Time: 13:39:40)
    -Function delete() has been tested. It works perfectly fine. (Date: 25 January 2017, Day: Wednesday, Time: 16:19:40)
    -Function authenticate needs to be tested. (Date: 27 January 2017, Day: Friday, Time: 14:53:40)
    -Function authenticate has been tested and works fine. (Date: 27 January 2017, Day: Friday, Time: 18:05:50)
    -Function authenticate has been added to commands delete, download and send. (Date: 27 January 2017, Day: Friday, Time: 19:23:09)
    -Function Connect has been added, it takes over the connection process, it is used twice which seemed very inefficient. (It is not tested yet) (Date: 31 January 2017, Day: Tuesday, Time: 08:40:38)
    -Excepted crash when lcd/scd to a directory that does not exist. Needs testing. (Date: 1 Febuary 2017, Day: Wednesday, Time: 10:55:21)
    -Wrong ip connection has been excepted but needs testing (I did not realise that i did this was already in function connect). (Date: 1 Febuary 2017, Day: Wednesday, Time: 11:14:30)
    -Function connect has excepted incorrect/invalid ip addresses. It has been tested. And works. But when an incorrect ip is entered it halts and looks like it does not do anything
        at the moment the only way to get out is to ^C (CTRL + C). This will be fixed in the next update. (Date: 1 Febuary 2017, Day: Wednesday, Time: 17:46:08)
    -Crash with lcd/scd to an invalid directory has been tested and it works. (Date: 1 Febuary 2017, Day: Wednesday, Time: 17:46:08)
    ------Released Update------- (Date: 1 Febuary 2017, Day: Wednesday, Time: 17:46:08) (Version 0.5.5)


Development Progress:
    -Script In Development 0.1v (Date: 21 January 2017, Day: Saturday, Time: 20:15:00)
    -Script In Development 0.4v (Date: 22 January 2017, Day: Sunday, Time: 11:24:50)
    -Script In Development 0.4.5v (Date: 23 January 2017, Day: Monday, Time: 09:41:40)
    -Script In Development 0.5.5v (Date: 1 Febuary 2017, Day: Wednesday, Time: 17:46:08)

Planned Additions or fixes:
    *A make command. that Makes a folder on FTP.
    *Organize all command outputs.
    *Make a connect function
    *zipfolder function has an issue. Check and fix. 

All that need testing:
    
Function plan (temporary):

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
        file = open('%sUnzip.%s' % (filename, extention) , 'rb')#This is taken off the Send() function so that it does not cause an error. (Date: 23 January 2017, Day: Monday, Time: 15:20:03)
        ftp.storbinary('STOR %s.%s' % (filename, extention), file)
        file.close()
        print("Sent to ", ftp.pwd())
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

def delete(filename):
    try:
        ftp.delete(filename)
        print("{} has been deleted.".format(filename))
    except:
        print("Some error has been raised.")# Add the actual errors in the except.

def authenticate():# Makes things safer. Like sending or reciving files. and deleting.
    tries = 0
    while tries <= 3:
        authenticate = getpass.getpass("Password Authentication: ") 
        if password == authenticate:
            return True
            break
        tries = tries + 1
        print("Wrong Password")
    else:
        return False

def connect(ipAddress, port):
    try:
        ftp.connect(ipAddress, port)
    except:#Add the acctual error
        print("Some error occured check to see if the ip is correct.")
        return
    username = input("Username: ")
    password = getpass.getpass("Password: ")
    try:
        ftp.login(username, password)
        print("Login Passed")
    except:
        print("Login failed")
'''---------------------------------------------------------------Logic-------------------------------------------------------------------'''
os.system("clear")
print("Welcom to FTP Made with python. Type help for command list.")
help = ['lls - command to get local directory list','connect <ip or url to ftp> - command to connect to ftp via port 21','sls - command to get server directory list','exit, bye - to quit','scd <path to directory> - to change directroy on server or vew current server directory','lcd <path to directory> - to change directory on local mechine or view the current working directory.', 'send <filename> - to send file.', 'zip <filename> - to zip a folder and send it.', 'download, get, retrieve <filename> - Downloads a file from the server', 'delete, remove <filename> - Deletes a specified file on the ftp', 'clear - clear screen' , 'help - to display this list']                 
ftp = FTP()
while True:
    command = input("ftp$ ")
    command = command.split()
    command[0] = command[0].lower()
    if command[0] == "lls":
        lls()

    elif command[0] == "connect":
        try:
            connect(command[1], 21)
        except IndexError:
            connect(input("Enter ip: "), 21)            
    elif command[0] == "sls":
        try:
            sls()
        except:
            print("Some error has occurred, try to re/connect to the ftp.")

    elif command[0] == "exit" or command[0] == "bye":#Program exits regardless of connection to ftp if command is typed.
        try:        
            ftp.quit()
        except AttributeError:
            pass
        exit()

    elif command[0] == "scd":
        try:
            scd(command[1])
        except:
            try:
                print("Current server working directory: ",ftp.pwd())
                print("The directory was not found or no directory was given")
            except:
                print("Some error has occurred, try to re/connect to the ftp.")

    elif command[0] == "lcd":
        try:
            lcd(command[1])
        except:
            print("The directory was not found or no directory was given")
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
        authResult = authenticate()
        if authResult == True:
            try:
                send(filex[0], filex[1])
            except:
                print("Some error occured. Make sure that the file name is correct and that you are connected to the ftp.")
    elif command[0] == "zip":
        authResult = authenticate()
        if authResult == True:
            try:
                zipfolder(command[1], command[1])
            except:
                print("Some error occured. Make sure the folder name is correct and that you are connected to the ftp.")

    elif command[0] == "retrieve" or command[0] == "get" or command[0] == "download":
        filex = command[1].replace(".", " ")
        filex = filex.split()
        authResult = authenticate()
        if authResult == True:
            try:
                download(filex[0], filex[1])
            except:
                print("Some error occured. Make sure that the file name is correct and that you are connected to the ftp.")
        else:
            print("Authentication failed.")
        
    elif command[0] == "delete" or command[0] == "remove":
        authResult = authenticate()
        if authResult == True:
            try:
                delete(command[1])
            except IndexError:
                print("Specify a file to delete.")
        else:
            print("Authentication failed.")

    else:
        print("{} command not found. Type help for command list.".format(command[0]))

 
