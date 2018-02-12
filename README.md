# Python FTP Client:

This is a simple FTP client made from python. Like any program this one contains bugs, I will fix them when I find them
as a user your responsibility is to report any bugs to me either here on git or send an email to tannishpage1@gmail.com
I will acknowledge your report and fix it as soon as I can.


Now that out of the way. Using the program is very simple.
Here is a list of commands:

## Nvigation

| Command     | Despcription              |
| ----------- | ------------------------- |
| `lls`       | Local list                |
| `sls`       | Server list               |
| `scd <dir>` | Change directory (server) |
| `lcd <dir>` | Changer directory (local) |

## File Manipulation

| Command                | Description                    |
| ---------------------- | ------------------------------ |
| `del <file_name>`      | Deletes filename on server     |
| `make <folder_name>`   | Makes a folder on server       |
| `rmdir <folder_name> ` | Deletes a folder on the server |

## File Transfer 

| Command                 | Description                              |
| ----------------------- | ---------------------------------------- |
| `get <file_name>`       | Download file from server                |
| `send <file_name>`      | Sends file to server                     |
| `zipsend <folder_name>` | Zips a folder and sends it to the server |

## Connection

| Command                | Description                            |
| ---------------------- | -------------------------------------- |
| `connect <ip_Address>` | Connects to passed ip address          |
| `lsize <file_name>`    | GIves an estimate for the time to send |
| `ssize <file_name>`    | Gives an estimate for time to send     |
| `quit`                 | Closes connection to the server        |

## Misc.

| Comman    | Description                                    |
| --------- | ---------------------------------------------- |
| `clear`   | Clears the screen                              |
| `hisotry` | Will print out previously visited ip addresses |
| `exit`    | Quits the program                              |
| `help`    | Prints this help message                       |

The list shown above will appear if the `help` command is entered into the program. If you have ever used a `UNIX` based OS's `cli` before these commands should sound familiar to you. But if you are still unsure here's a linke to a tutorial video: <LINK TO VIDEO>

If you would like to contribute to this project with any bug fixes, new features or would like to work with me in a
colaboration contact me at  tannishpage1@gmail.com and I will get back to you as soon as I can. Now go on enjoy the wonders of the world. :)
