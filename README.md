Python FTP Client:

This is a simple FTP client made from python. Like any program this one contains bugs, I will fix them when I find them
as a user your responsibility is to report any bugs to me either here on git or send an email to tannishpage1@gmail.com
I will acknowledge your report and fix it as soon as I can.


Now that out of the way. Using the program is very simple.
Here is a list of commands:

-----Navigation-----
lls                   Local list
sls                   Server list
scd <dir>             Change directory (server)
lcd <dir>             Change directory (local)

-----File Manipulation-----
del <filename>        Deletes filename on server
make <foldername>     Makes a folder on server
rmdir <foldername>    Deletes a folder on server

-----File Transfer-----
get <filename>        Downloads file from server
send <filename>       Sends file to server
zipsend <foldername>  Zips a folder and sends it to server

-----connection-----
connect <ipAddress>   Connects to passed ip address
lsize <filename>      Gives an estimate for time to send
ssize <filename>      Gives an estimate for time to download
quit                  Closes connection to server

-----Misc-----
clear                 Clears the screen
history               will print out previously visited ipaddresses
exit                  Quits the program
help                  Prints this help message

The same list will appear if the help command is entered into the program. If you have ever used the command line these
commands should sound familiar to you. But if you are still unsure here's a like to a tutorial video: <LINK TO VIDEO>



If you would like to contribute to this project with any bug fixes, new features or would like to work with me in a
colaboration contact me at tannishpage1@gmail.com and I will get back to you as soon as I can. Now go on enjoy the
wonders of the world. :)
