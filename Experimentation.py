import os
import ftplib_edited
from ftplib_edited import FTP
import zipfile
import sys
import getpass
import datetime
import multiprocessing #This is an experiment

class colors: #Has a list of colors that are used by the program.
    BLUE = '\033[34m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    PURPLE = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[39m'
    HEADER = '\033[95m'
    BLUE_2 = '\033[94m'
    GREEN_2 = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    END = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def send(filename):
    try:
        file = open('%s' % filename , 'rb')
    except FileNotFoundError as e:
        print(e)
        return False
    print("Starting transfer....")
    startime = datetime.datetime.now()
    ftp.storbinary('STOR %s' % filename, file)
    endtime = datetime.datetime.now()
    time = (endtime-startime).total_seconds()
    file.close()
    print("\nSent to ", ftp.pwd(), " In ", time)

def download(filename): 
    file = open("%s" % filename, "wb")
    startime = datetime.datetime.now()
    try:#Added this, because when downloading a file that does not exist program crashes. (Date: 7 March 2017, Day: Tuesday, Time: 14:42:28)
        ftp.retrbinary("RETR %s" % filename, file.write, ftp.size(filename))
    except Exception as e:
        print(e)
        file.close
        os.remove(filename)#The created file was still there, so this deletes the file.
        return False
    endtime = datetime.datetime.now()
    time = (endtime-startime).total_seconds()
    file.close()
    print("\nDownloaded to ", os.getcwd(), " In ", time)

def connect(ipAddress, port=21): # The connect code was being repeted twice, so i made a function.
    global ftp
    ftp = FTP()
    try:
        ftp.connect(ipAddress, port)
    except Exception as e:#Add the acctual error
        print(e)
        return False
    username = input(colors.FAIL + "Username: ")
    password = getpass.getpass("Password: " + colors.END)
    try:
        ftp.login(username, password)
        bytes, time = getTransfSpeed(ftp.nlst()) #Will list all files on ftp and try to get speed of one of them.
        welcome = ftp.getwelcome() #Now prints out welcome message.
        print(colors.GREEN + "Login Successful.\nConnected to: %s\nConnection Speed: %s b/s\nWelcome Message: %s" % (ipAddress,bytes,welcome) + colors.END) # This line is fixed. (Date: 22 March 2017, Day: Wednesday, Time: 08:27:35)
        connection_history(ipAddress)
    except Exception as e:
        print(e)







