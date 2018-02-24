import sys
import os
import hashlib

download_dir = sys.argv[1]
save_dir = "/home/lashuk/Documents/"

FileList = os.listdir(download_dir)
for File in FileList:
    #print File
    extension = ''.join(os.path.splitext(File)[1])
    name = ''.join(os.path.splitext(File)[0])
    ext = extension.strip('.')

    if os.path.isdir(download_dir + File):
        pass

    else:
        if os.path.exists(save_dir + ext + "/" + File):
            Data = open(download_dir + File, "r").read()
            m = hashlib.sha1() 
            m.update(Data) 
            h = (m.hexdigest())[0:5]
            file(save_dir + ext + "/" +name+"-"+h+"."+ext, "w").write(Data)
            os.remove(download_dir + File)

        elif os.path.exists(save_dir + ext):
            Data = open(download_dir + File, "r").read()
            file(save_dir + ext + "/" + File, "w").write(Data)
            os.remove(download_dir + File)

        if os.path.exists(save_dir + ext) != True:
            os.makedirs(save_dir + ext)
            Data = open(download_dir + File, "r").read()
            file(save_dir + ext + "/" + File, "w").write(Data)
            os.remove(download_dir + File)