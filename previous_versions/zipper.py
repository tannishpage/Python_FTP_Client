import os
import zipfile
def zipfolder(foldername, target_dir):#This function is used to Zip a folder and then send it over to the ftp    
    zipobj = zipfile.ZipFile(foldername + '.zip', 'w', zipfile.ZIP_DEFLATED)#I did not make this function for the record, i only modified it. I don't know who made it.
    rootlen = len(target_dir) + 1
    for base, dirs, files in os.walk(target_dir):
        for file in files:
            fn = os.path.join(base, file)
            zipobj.write(fn, fn[rootlen:])

for x in os.listdir(os.getcwd()):
    zipfolder(x, x)
