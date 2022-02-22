import matplotlib.pyplot as plt
import os

while True:
    pathh=input("Enter Full File Path: ")
    if os.path.isfile(pathh):
        break
    else:
        print("File not Found")
path1=pathh.split("\\")
path2=""
for i in range(0,len(path1)):
    if (i==0):
        path2=path1[i]
    elif(i<(len(path1)-1)):
        path2=path2+"\\"+path1[i]
        
flobj=open(pathh,"r")
flnl=flobj.read().split("\n")
flobj.close()
ap=[]
ab=[]
for j in flnl:
    if j.strip() != "":
        ap.append(j.split(",")[0])
        ab.append(j.split(",")[1])
  
apbc=[]
apbd=[]
apbct=[]
apbdt=[]
for i in range(0,len(ap)):
    if eval(ab[i]):
        apbc.append(ap[i])
        apbct.append(i)
    else:
        apbd.append(ap[i])
        apbdt.append(i)

plt.plot(apbct,apbc,marker="o",color="g")
plt.plot(apbdt,apbd,marker="*",color="r")

plt.xlabel("Time in Min")
plt.ylabel("Battery in Percent")

os.chdir(path2)
plt.savefig("myf.png")
plt.show()

