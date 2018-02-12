#!/usr/bin/python3
"""

PLEASE WRITE A MANUAL http://www.schweikhardt.net/man_page_howto.html (Date: 22 November 2017, Day: Wednesday, Time: 07:10:49)

USE THIS TO TEST my ftp site is down and will be down for a while: speedtest.tele2.net (Date: 1 September 2017, Day: Friday, Time: 14:41:46)


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
    -Script Tested on Android. Works flawlessly only a few errors that will occur on any platform need fixing. (Date: 22 January 2017, Day: Sunday, Time: 11:50:50)
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

    -License command was created. But is called copyright. (Date: 4 Febuary 2017, Day: Saturday, Time: 22:01:20)
    -Copyright command is now in use. (Date: 7 Febuary 2017, Day: Tuesday, Time: 12:53:30)
    -Invalid ip halting is fixed. Issue was there was a return but nothing was being returned so it halted. (Date: 7 Febuary 2017, Day: Tuesday, Time: 12:53:30)
    -When no command is entered program crashes. It is now fixed. (Date: 7 Febuary 2017, Day: Tuesday, Time: 12:53:30)
    -Authentication failed because password was not a global variable. So now password and username are global variables They are declared like this: global username and global password.(Date: 7 Febuary 2017, Day: Tuesday, Time: 17:25:40)
    -Tested on windows program works. Connection is successful and everything is compatible. (Date: 9 Febuary 2017, Day: Thursday, Time: 10:52:37)
    -----Released Update------- (Date: 9 Febuary 2017, Day: Thursday, Time: 10:54:24) (Version 0.6.5)
    
    -All further development is now in windows for the time being. I reinstalled windows on the 9th feb and it corrupted grub, so i could not go into ubuntu so i took backup of all scripts and deleted ubuntu. Untill i reinstall ubuntu windows will be used to develop. (Date: 10 Febuary 2017, Day: Friday, Time: 07:09:58)
    -Now authentication is not asked if connection to ftp is not open. Previously authentication will be asked regardless of an open connection to ftp. (Date: 11 Febuary 2017, Day: Saturday, Time: 21:40:55)
    -Made a delete command for dirs. Yes file deletion and dir deletion is different. (Date: 11 Febuary 2017, Day: Saturday, Time: 21:40:55)
    -Made a command that makes folders on ftp. Now user will have more accessablity to to make changes to ftp. (Date: 11 Febuary 2017, Day: Saturday, Time: 21:40:55)
    -----Released Update--------- (Date: 11 Febuary 2017, Day: Saturday, Time: 21:50:45) (Version 0.8)
    
    -Zip folder function has been fixed, the issue was that 2 unknown variables were being used. Insted of foldername filename was being used and undeclared variable extention was used. (Date: 11 Febuary 2017, Day: Satuary, Time: 22:35:05)
    -The size command has been successfully implimented. It works fine. It gives a prediction so not to be 100% trusted. (Date: 12 Febuary 2017, Day: Sunday, Time: 12:20:50)
    -The send and download functions have been modified so that they show the time it took to transfer the file. They now also give a hit that the transfer started. (Date: 12 Febuary 2017, Day: Sunday, Time: 12:20:50)
    -----Released Final---------- (Date: 12 Febuary 2017, Day: Sunday, Time: 12:20:50) (Version 1.0)

    -Development is completed. Any updates after this a to fix unknown errors. Regular updates will stop from this point onwards. (Date: 12 Febuary 2017, Day: Sunday, Time: 12:20:50)
    -Excepted ^C input. (Date: 13 Febuary 2017, Day: Monday, Time: 07:11:44)
    -Size command had an issue, it was throwing the attribute error which crashed the program. Turns out it did not care even if user did not open a connection and just moved on. So ya. fixed! (Date: 13 Febuary 2017, Day: Monday, Time: 07:23:20) 
    -The ipAddress to connect can now be passed as an argument but for some reason it is not working, check into it and fix it. (Date: 20 Febuary 2017, Day: Monday, Time: 18:12:42)
    -Just so you know, um Ubuntu has been reinstalled on the 10 Febuary 2017, I have been using ubuntu since then to develop, i have also been using windows as well. (Date: 8 March 2017, Day: Wednesday, Time: 06:24:50)
    -The download command has been fixed. The issue was that when it could not find the file specified, it crashed the program. So now it will not crash. (Date: 9 March 2017, Day: Thursday, Time: 21:58:06)
    -Now IP address can be directly entered as an argument. (Date: 9 March 2017, Day: Thursday, Time: 22:08:04)
    -Disconnect command added. To call it in shell type quit. All it will do is disconnect from the ftp. The exit command does that aswell but it will quit the program too. (Date: 21 March 2017, Day: Tuesday, Time: 13:12:03)
    -Downloading a file that does not exist caused an error that crashed the program. It has now been fixed, only inconvinience is, it will ask you to confirm password regardless. (Date: 21 March 2017, Day: Tuesday, Time: 21:27:10)
    -"An error occurs when connection to ftp fails and user quits. [BrokenPipeError] Find out why and fix." This error has been fixed. Don't know how I fixed it, don't know what caused it. (Date: 22 March 2017, Day: Wednesday, Time: 05:27:36)    
    -The function size is now split into 2 different functions. 1) getTransfSpeed and 2) getTransfTime. This will make the process simpler (Date: 22 March 2017, Day: Wednesday, Time: 08:29:34) 
    -The size function is not removed it is still in use by the size command, until i find a way to use the getTransfSpeed and getTransfTime functions with the size command. (Date: 22 March 2017, Day: Wednesday, Time: 08:37:04)
    -The connect function will now output the transfer speed between the client and host. (Date: 22 March 2017, Day: Wednesday, Time: 08:40:40)
    -Command and function size have now been renamed to ssize. Because local size or lsize is now being worked on. (Date: 22 March 2017, Day: Wednesday, Time: 10:14:47)
    -lsize is now added and tested, it works fine. Successfully implimented. (Date: 22 March 2017, Day: Wednesday, Time: 18:56:34)
    -----Released Update--------- (Date: 22 March 2017, Day: Wednesday, Time: 18:57:29) (Version 1.1)

    -Previously the lcd command could not change dir in to folder names with a space in them. Now with a few fixes to logic, it can. (Date: 23 March 2017, Day: Thursday, Time: 07:20:34)
    -Previously the scd command also coudl not change dir in to a folders with a space in their names. Now with a few fixes to logic it can. (Date: 23 March 2017, Day: Thursday, Time: 08:23:37)
    -Now the send and download commands do not split the filename into and extention and the filename. This prevented me to send or download files with names like "something.this.txt" because the dot is replaced with a space. Now it only takes what ever the user types. (Date: 23 March 2017, Day: Thursday, Time: 10:21:17)
    -----Released Update--------- (Date: 23 March 2017, Day: Wednesday, Time: 10:40:22) (Version 1.2)
    
    -Unzipper on the host side is not functioning. So i am removing the feature in function zipfile. So now zipfile will only zip a folder and then it will send it to ftp. (Date: 25 March 2017, Day: Saturday, Time: 07:06:07)
    -----Released Update--------- (Date: 25 March 2017, Day: Saturday, Time: 08:21:22)

    -There will be no more development on this program. Its finished. Not at its best state but its done. Most of the bugs are fixed, and alot of the logical errors are fixed. Since this is my personal client I know whats wrong with it and i will find ways to work around. This is the end of development on this script. Bye :). (Date: 25 March 2017, Day: Saturday, Time: 08:25:07)    

    ----------------------------- More Development On This ----------------------------------

    -Yes I am back. Gonna remove some personalized crap from this script and split it into 2 and put all functions in a class. (Date: 14 June 2017, Day: Wednesday, Time: 14:17:09) 
    -Got rid of getTransfTime because it just a simple math calculation. I just do it in getTransfSpeed. Its faster. (Date: 14 June 2017, Day: Wednesday, Time: 14:36:09)
    -Ok now it is posible for getTrasfSpeed to take in a list. (Date: 14 June 2017, Day: Wednesday, Time: 16:02:50)
    -Connect will now show the welcome message of an ftp server. (Date: 14 June 2017, Day: Wednesday, Time: 16:02:50)
    -Realised that ssize does everything getTransfSpeed does so replaced those bits with the function. (Date: 14 June 2017, Day: Wednesday, Time: 16:05:50)
    -Ok so thats all for today. The shell bit is not functional, need to fix that. I am not going to split this into multiple files atleast for now. (Date: 14 June 2017, Day: Wednesday, Time: 16:07:50)
    -It's decided that the infinite while loop in logic will be rewritten. With the help of the original that is now shifted to another file in previous versions. (Date: 14 June 2017, Day: Wednesday, Time: 16:52:57)
    -I gave cmd.Cmdloop a try. And it seems to be very s*it. So I will try to do something else. Like modify the cmd.cmdloop file and use my version. Or I will revert back to the large if stak. (Date: 15 June 2017, Day: Thursday, Time: 14:20:07)    
    -Ok this is now a seperate file, I am goning to import this in another file and use that to make a command line interface. (Date: 17 June 2017, Day: Saturday, Time: 14:53:06)
    -Now the send and download functions can transfer all files in a directory if * is passed in the commands. (Date: 27 June 2017, Day: Tuesday, Time: 08:28:55)
    -Ok all the bugs have been fixed. Regardless there are still a thousand more that I don't know of, I have tested it on android (where its meant to be used) and it works flawlessly. Anyway, this is the end of the development of this script. I will now really move on. I will use this script and if i ever come across any bugs or errors I will try to fix. (Date: 27 June 2017, Day: Tuesday, Time: 10:32:15)        
    ---------------------------- END OF DEVELOPMENT ON THIS-----------------------------------
    -lcd crashed on windows for some unknown reason, just trying to fix that. (Date: 18 July 2017, Day: Tuesday, Time: 10:17:50)
    -Turns out lcd crashes because of some tiny error, winError '' cannot be found. So fixed in some silly way. (Date: 18 July 2017, Day: Tuesday, Time: 10:20:50)
    -Adding a new function to zip and send all folders in a directory, function name = dir_zip_folder, it will take a list as its argument. (Date, 19 July 2017, Day: Wednesday, Time: 08:45:58)
    -The function dir_zip_folder has been tested and it workes fine, now if * is an argument of the command zipsend, this function will called and it will zip and send all folders in a directory useful when you need to send a heap of folders. (Date: 19 July 2017, Day: Wednesday, Time: 10:36:03)
    -Ok now the delete function can also do the * thing. So good. (Date: 20 July 2017, Day: Thursday, Time: 18:38:21)
    ----------------------------      Released Update      -----------------------------------
    -Added a tiny feature if the connect command is called without any arguments given the program will ask you to enter an ip address and a port to connect through. (Date: 26 July 2017, Day: Wednesday, Time: 11:32:31)
    -Added another tiny feature where if the send or zipsend or even the download commands are called with the * as an argument, it will calculate the total transfer size and ask the user for confermation to proceed with the transfer. (Date: 1 September 2017, Day: Friday, Time: 17:01:39)
    ----------------------------      Released Update      -----------------------------------
    
    -Added two new functions its a small feature that could be helpful. connection_history and list_connection_history these functions will store and list out any successful connections that have been made like a history. All this will be stored in a file called history in the documents folder in windows. (Date: 21 November 2017, Day: Tuesday, Time: 22:28:17)
    -Fixed zipsend command with the *. What happended was when the * was passed it would zip and send all the folders in a direcotry but for some reason this was not happending when done individually it would be fine but with the star it would create fiels of sizes greater 1GB so i fixed this by making the zip function not send anything but only make the zipped folder and made another function that does the sending. The dir_zip function will use the zip function to make to zip all the folders this fixed the issue. (Date: 22 November 2017, Day: Wednesday, Time: 08:01:28)
    -Added a progress bar. Now this program no longer uses the default ftplip file that comes with python default. I made some changes to the ftplib file which is now called ftplib_edited.py This file will come with the program when downloaded from gtihub. (Date: 5 January 2018, Day: Friday, Time: 13:51:38)
    -Made a change to the progress bar. Also tested out the zipsend * command it seems to be working fine. I am not sure what the issue was. But i think it is no longer existant. Maybe its because I split the zipsend functions up??? Who knows. (Date: 10 February 2018, Day: Saturday, Time: 14:47:15)
    -Added a rm command which removes a file on the local machine. (Date: 10 Februrary 2018, Day: Saturday, Time: 15:08:45)
    -Now Additional information is displayed when lls is executed like if its a file or directory and the size of files. (Date: 10 Febuary 2018, Day: Saturday, Time: 17:27:10)

Development Progress:
    -Script In Development 0.1v (Date: 21 January 2017, Day: Saturday, Time: 20:15:00)
    -Script In Development 0.4v (Date: 22 January 2017, Day: Sunday, Time: 11:24:50)
    -Script In Development 0.4.5v (Date: 23 January 2017, Day: Monday, Time: 09:41:40)
    -Script In Development 0.5.5v (Date: 1 Febuary 2017, Day: Wednesday, Time: 17:46:08)
    -Script In Development 0.6.5v (Date: 9 Febuary 2017, Day: Thursday, Time: 19:57:34)
    -Script In Development 0.8v (Date: 11 Febuary 2017, Day: Saturday, Time: 21:40:55)
    -Script Fully Developed 1.0v (Date: 12 Febuary 2017, Day: Sunday, Time: 12:24:50)
    -Script Fully Developed 1.1v (Date: 22 March 2017, Day: Wednesday, Time: 18:57:29)
    -Script Fully Developed 1.2v (Date: 23 March 2017, Day: Thursday, Time: 10:40:22)
    -Script Fully Developed 1.3v (Date: 25 March 2017, Day: Saturday, Time: 08:21:22)
-------------------------------NO MORE DEVELOPMENT ON THIS PROGRAM-----------------------------------------------
    -Script Over Developed v1.5 (Date: 23 June 2017, Day: Friday, Time: 13:52:11)
    -Script Over Developed v2.0 (Date: 27 June 2017, Day: Tuesday, Time: 10:33:47)
-------------------------------NO MORE OVER DEVELOPMENT ON THIS PROGRAM------------------------------------------
    -Script Over Developed v2.2 (Date: 20 July 2017, Day: Thursday, Time: 18:38:21)
    -Script Over Developed v2.3 (Date: 1 September 2017, Day: Friday, Time: 18:32:34)
    -Script Over Developed v2.4 (Date: 22 November 2017, Day: Wednesday, Time: 09:05:17)
    -Script Over Developed v2.5 (Date: 5 January 2017, Day: Friday, Time: 15:51:30)
    -Script Over Developed v2.6 (Date: 10 Februrary 2018, Day: Saturday, Time: 18:27:10) 

Planned Additions or fixes:

All that need testing:

Plan (temporary):


"""

'''-------------------------------------------------------Libraries--------------------------------------------------'''

import os
import ftplib_edited
from ftplib_edited import FTP
import zipfile
import sys
import getpass
import datetime
import multiprocessing #This is an experiment


'''-------------------------------------------------------Classes---------------------------------------------------------------------------'''

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


'''-------------------------------------------------------Functions-------------------------------------------------------------------------'''
def zipfolder(foldername, target_dir):#This function is used to Zip a folder and then send it over to the ftp    
    zipobj = zipfile.ZipFile(foldername + '.zip', 'w', zipfile.ZIP_DEFLATED)#I did not make this function for the record, i only modified it. I don't know who made it.
    rootlen = len(target_dir) + 1
    for base, dirs, files in os.walk(target_dir):
        for file in files:
            fn = os.path.join(base, file)
            zipobj.write(fn, fn[rootlen:])

def zipsend(foldername):
    zipfolder(foldername, foldername)
    send(foldername + '.zip')

    '''query1 = input("Would you like to unzip it on the server?(y/n): ")
    if query1 == 'y':
        zipobj = zipfile.ZipFile(foldername + 'Unzip.zip', 'w', zipfile.ZIP_DEFLATED)#I did not make this function for the record
        rootlen = len(target_dir) + 1
        for base, dirs, files in os.walk(target_dir):
            for file in files:
                fn = os.path.join(base, file)
                zipobj.write(fn, fn[rootlen:])
        file = open('%sUnzip.zip' % foldername , 'rb')#This is taken off the Send() function so that it does not cause an error. (Date: 23 January 2017, Day: Monday, Time: 15:20:03)
        ftp.storbinary('STOR %sUnzip.zip' % (foldername), file)
        file.close()
        print("Sent to ", ftp.pwd())
    else:'''

def dir_zip_folder():#This function is new, its objective is to zip all folders in a directory and start transfering all of them.
    folderlist = [x for x in os.listdir(os.getcwd()) if os.path.isdir(x)]
    foldernamezip = []
    Tfilesize = 0
    for foldername in folderlist:
        print('Zipping {}'.format(foldername))
        foldernamezip.append(foldername + '.zip')
        zipfolder(foldername, foldername)
        
    for f in foldernamezip:
        file = open(f, 'r')
        file.seek(0,2)
        Tfilesize = Tfilesize + file.tell()
        file.close()
    print('Total upload size: {} bytes'.format(Tfilesize))
    usr = input('Proceed with transfer? [y/n]')
    usr = usr.lower()
    if usr == 'n':
        print('Aborting. Removing all zip files created.')
        for name in foldernamezip:
            os.remove(name)
        else:
            print('Successfully removed')
        return False
    elif usr == 'y':
        for name in foldernamezip:
            print('Sending: %s' % name)
            send(name)
        else:
            print(colors.GREEN + 'Successfully sent all files.\nRemoving all zip files.' + colors.END)
        for name in foldernamezip:
            os.remove(name)
    else:
        print('Aborting because no clear answer was given.')
        for name in foldernamezip:
            os.remove(name)


def send(filename):#This function is used to send files or .zip files to the ftp.
    if filename == '*':#Added this so that i can send a folder of files with one command insted of the number of files i have.
        files = [x for x in os.listdir(os.getcwd()) if os.path.isfile(x)]
        Tfilesize = 0
        for f in files:
            file = open(f, 'r')
            file.seek(0,2)
            Tfilesize = Tfilesize + file.tell()
            file.close()
        print('Total transfer size: {} bytes'.format(Tfilesize))
        usr = input('Proceed with transfer? [y/n]')
        usr = usr.lower()
        if usr == 'n':
            return False
        elif usr == 'y':
            pass
        else:
            print('Aborting because no clear answer was give')
            return False
        print("Starting transfer....")
        for file in files:
            f = open('%s' % file, 'rb')
            try:
                ftp.storbinary('STOR %s' % file, f)
                print(file + ' | Transferd')
            except ftplib_edited.error_perm:
                print(file, ' | has no data. Not transfering')
                del files[files.index(file)]
        else:
            print('All files sent successfully')
        
    else:    
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

def download(filename):#This function is to retrieve or download a file from the ftp.
    if filename == '*':
        files = ftp.nlst()
        Tfilesize = 0
        for f in files:
            try:
                filesize = ftp.size(f)
            except ftplib_edited.error_perm:
                continue
            Tfilesize = Tfilesize + filesize
        print('Total transfer size: {} bytes'.format(Tfilesize))
        usr = input('Proceed with transfer? [y/n]')
        usr = usr.lower()
        if usr == 'n':
            return False
        elif usr == 'y':
            pass
        else:
            print('Aborting because no clear answer was give')
            return False
        print("Starting transfer....")
        for file in files:
            f = open('%s' % file, 'wb')
            try:
                ftp.retrbinary("RETR %s" % file, f.write, ftp.size(file))
                print(file + ' | Transferd')
            except ftplib_edited.error_perm:
                continue
        else:
            print('Successfully downloaded all files')
    else:
        file = open("%s" % filename, "wb")
        print("Starting transfer....")
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

def sls():#sls stands for Server List, it is the ls command but for server side. It lists all directories and files on the server.
    ftp.retrlines('LIST')

def lls():#lls stands for Local List, it is the ls command but on local mechine.
    directories = [x for x in os.listdir(os.getcwd()) if os.path.isdir(x)]
    files = [x for x in os.listdir(os.getcwd()) if os.path.isfile(x)]
    for x in directories:
        print(colors.BOLD + "{}: Type: Folder".format(x) + colors.END)
    for x in files:
        file = open(x, "r")
        file.seek(0,2)
        print("{}: Type: File | Size: {}KB".format(x, file.tell()/1000))
        file.close()

def scd(path):#scd stands for Server Change Directory. cd command but for server.
    print("Old Server Working Directory: {}".format(ftp.pwd()))
    ftp.cwd(path)
    print("New Server Working Directory: {}".format(ftp.pwd()))

def lcd(path):#lcd stands for Local Change Directory. cd command but for local mechine.
    print("Old Local Working Directory: {}".format(os.getcwd()))
    os.chdir(path)
    print("New Local Working Directory: {}".format(os.getcwd()))

def delete(filename):
    if filename == '*':
        for file in ftp.nlst():
            try:
                ftp.delete(file)
                print(file + ' | Deleted')
            except:
                continue
    else:
        try:
            ftp.delete(filename)
            print("{} has been deleted.".format(filename))
        except Exception as e:
            print(e)# Add the actual errors in the except.  

'''def authenticate(self):# Makes things safer. Like sending or reciving files. and deleting.
    tries = 0
    while tries <= 3:
        authenticate = getpass.getpass("Password Authentication: ") 
        if password == authenticate:
            return True
        tries = tries + 1
        print("Wrong Password. Try again.")
    else:
        return False''' #It is now removed (I know its not.)

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
        #connection_history(ipAddress)
    except Exception as e:
        print(e)

def make(filename):#This function makes a folder on the server.
    try:
        ftp.mkd(filename)
    except Exception as e:
        print(e)
def rmdir(filename):#There is a delete function but this one only deletes folders the other one does not.
    try:
        ftp.rmd(filename)
    except Exception as e:
        print(e)

def ssize(filename):#This function returns the name, size, speed of the connection, and the estimated download time of the file.
    transfspeed, transfTime = getTransfSpeed(filename)
    filesize = ftp.size(filename)
    print(colors.GREEN + "\nFile Name: {0}\nFile Size: {1} bytes\nAvg Transfer Speed: {2} bytes/seconds\nAvg time of transfer: {3} seconds".format(filename, filesize, transfspeed, transfTime) + colors.END)
    #return trasfspeed

def lsize(filename):
    transfSpeed, time = getTransfSpeed(ftp.nlst())
    try:
        file = open("%s" % filename,"r")
    except FileNotFoundError as e:
        print(e)
        return False
    file.seek(0,2)
    filesize = file.tell()
    try:
        transfTime = filesize / float(transfSpeed)
    except ValueError:
        print("Cannot Calculate")
        return False
    print(colors.GREEN + "\nFile Name: {0}\nFile Size: {1} bytes\nAvg Transfer Speed: {2} bytes/seconds\nAvg time of transfer: {3} seconds".format(filename, filesize, transfSpeed, transfTime) + colors.END)
    file.close()

def getTransfSpeed(filename):#Gets the connection speed between client and the server
    if type(filename) == type(list()):
        for file in filename:
            try:
                startime = datetime.datetime.now()
                filesize = ftp.size(file)
                endtime = datetime.datetime.now()
                break
            except:
                continue
        else:
            return "Cannot Calculate", "Cannot Calculate"
    else:
        startime = datetime.datetime.now()
        filesize = ftp.size(filename)
        endtime = datetime.datetime.now()    
    stringsize = len(str(filesize))
    transfspeed = stringsize / ((((endtime - startime)).total_seconds())/2)
    return str(transfspeed), str(filesize/transfspeed)

def help():
    cmdlst = colors.YELLOW + '-----Navigation-----\nlls                   Local list\nsls                   Server list\nscd <dir>             Change directory (server)\nlcd <dir>             Change directory (local)\n\n-----File Manipulation-----\ndel <filename>        Deletes filename on server\nmake <foldername>     Makes a folder on server\nrmdir <foldername>    Deletes a folder on server\n\n-----File Transfer-----\nget <filename>        Downloads file from server\nsend <filename>       Sends file to server\nzipsend <foldername>  Zips a folder and sends it to server\n\n-----connection-----\nconnect <ipAddress>   Connects to passed ip address\nlsize <filename>      Gives an estimate for time to send\nssize <filename>      Gives an estimate for time to download\nquit                  Closes connection to server\n\n-----Misc-----\nclear                 Clears the screen\nhistory               will print out previously visited ipaddresses\nexit                  Quits the program\nhelp                  Prints this help message' + colors.END
    print("command list: ")
    print(cmdlst)

'''def connection_history(ipAddress): #This function will store a history of all the SUCCESSFUL CONNECTIONS ONLY
    date = str(datetime.datetime.now()).split()[0]
    try:
        file = open('{}\\history'.format(os.path.expandvars('%userprofile%\\Documents')), 'a')
    except FileNotFoundError:
        file = open('{}\\history'.format(os.path.expandvars('%userprofile%\\Documents')), 'w+')
    file.seek(0,2)
    file.write('[{}] {}\n'.format(date,ipAddress))
    file.close()

def list_connection_history(): #This function will return the history of all the SUCCESSFUL CONNECTIONS ONLY that have been stored by connection_history function
    try:
        file = open('{}\\history'.format(os.path.expandvars('%userprofile%\\Documents')), 'r')
    except FileNotFoundError:
        print(colors.RED + 'history file has not been created, connect successfully to an ip to make a history file' + colors.END)
        return False
    addresses = file.read()
    print(addresses)
    file.close()'''
'''-------------------------------------------- Logic -------------------------------------------------------------------'''

while True:
    try:
        usr_input = input(colors.CYAN + "ftp$ " + colors.END + colors.PURPLE)
        if usr_input == "":
            continue
    except KeyboardInterrupt:
        print()
        continue
    command = "".join(usr_input.split()[0:1:]).lower()
    try:
        arguments = " ".join(usr_input.split()[1::])
    except Exception as e:
        pass



#======================Navigation======================    
    if command == "lls":
        lls()

    elif command == "sls":
        try:
            sls()
        except NameError:
            print(colors.RED + "Err run connect first" + colors.END)
        except ConnectionResetError:
            print(colors.RED + "Reconnect to server" + colors.END)
        except Exception as e:
            print(colors.RED + '{}'.format(e) + colors.END)

    elif command == "scd":
        try:
            scd(arguments)
        except NameError:
            print(colors.RED + "Err run connect first" + colors.END)
        except ConnectionResetError:
            print(colors.RED + "Reconnect to server" + colors.END)
        except Exception as e:
            print(colors.RED + '{}'.format(e) + colors.END)

    elif command == "lcd":
        try:
            lcd(arguments)
        except (TypeError, FileNotFoundError) as e:
            print(colors.RED + '{}'.format(e) + colors.END)
        except Exception as e:
            print(colors.RED + '{}'.format(e) + colors.END)
#===================End Navigation====================



#=====================File Manipulation===============
    elif command == "del":
        delete(arguments)
    
    elif command == "make":
        make(arguments)

    elif command == "rmdir":
        rmdir(arguments)

    elif command == "rm":
        try:
            os.remove(arguments)
        except PermissionError:
            print(colors.RED + "Err Permission Denied to remove: {}".format(arguments) + colors.END)
#=================End File Manipulation===============



#====================File Transfer====================
    elif command == "get":
        download(arguments)

    elif command == "send":
        try:
            send(arguments)
        except NameError:
            print(colors.RED + "Err run connect first" + colors.END)

    elif command == "zipsend":
        if arguments == '*':
            dir_zip_folder()
            continue
        try:
            zipsend(arguments)
        except Exception as e:
            print(colors.RED + '{}'.format(e) + colors.END)
#================End File Transfer====================



#====================Connection=======================
    elif command == "connect":
        if arguments == '':
            connect(input("Enter Server IP: "), int(input("Enter port: ")))
        else:
            connect(arguments)

    elif command == "lsize":
        try:
            lsize(arguments)
        except Exception as e:
            print(colors.RED + '{}'.format(e) + colors.END)
    
    elif command == "ssize":
        try:
            ssize(arguments)
        except Exception as e:
            print(colors.RED + '{}'.format(e) + colors.END)

    elif command == "quit":
        try:
            ftp.quit()
            del ftp
        except NameError:
            print(colors.RED + "Err run connect to disconnect" + colors.END)
#================End Connection=======================



#========================Misc=========================
    elif command == "clear":
        os.system("cls" if os.name == "nt" else "clear")
    
    elif command == "exit":
        exit()

    elif command == "help":
        help()

#====================End Misc=========================

    else:
        print(colors.RED + "{} not found, type help for command list".format(command) + colors.END)
