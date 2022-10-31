
import os
import wmi


c = wmi.WMI ()
for drive in c.Win32_LogicalDisk ():
    
    disk = drive.Caption  +"\\"
    print (disk)
    for path, subdirs, files in os.walk(disk):
        for name in files:
            print(os.path.join(path, name))

