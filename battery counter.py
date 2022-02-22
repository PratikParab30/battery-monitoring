import os
import psutil as ps 
import time
import re
import datetime



def gd():
    t=datetime.datetime.now()
    dt=[]
    dt.append(t.day)
    dt.append(t.month)
    dt.append(t.year)
    return (dt[0],dt[1],dt[2])    

def gt():
    t=datetime.datetime.now()
    dt=[]
    dt.append(t.hour)
    dt.append(t.minute)
    dt.append(t.second)
    return (dt[0],dt[1],dt[2])

a="D:\\"
os.chdir(a)
path=os.listdir(a)
b="BattOP"
if b not in path:
    print("HII")
    os.mkdir(b)
os.chdir(b)

path="battery.txt"



while True:
    bat=ps.sensors_battery()
    flobj=open(path,"a")
    perc=bat.percent
    plug=bat.power_plugged
    perc=f"{perc},{plug},{re.sub(',',':',str(gt()))},{re.sub(',','/',str(gd()))}\n"
    flobj.write(perc)
    flobj.close()
    time.sleep(60)
    
