import codecs
import csv
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.ticker as mticker  

fileHigh = codecs.open(r"./data/målong 4 5 v.csv", encoding="utf-8", errors="ignore")
fileLow = codecs.open(r"./data/målong 5 5 v.csv", encoding="utf-8", errors="ignore")

high5V = csv.reader(fileHigh.readlines())
low5V = csv.reader(fileLow.readlines())
fileHigh.flush()
fileHigh.close()
fileLow.flush()
fileLow.close()

tSecond:list =[]
tMovedMilliSecond:list =[]
v1Volt:list = []
v2HighVolt: list = []
v2LowVolt: list = []

skipLines:int = 20

for line in high5V:
    if skipLines==0:
        tSecond.append(float(line[0]))
        v1Volt.append(float(line[1]))
        v2HighVolt.append(float(line[2]))
    else:
         skipLines-=1

skipLines = 20
for line in low5V:
    if skipLines==0:
        v2LowVolt.append(float(line[2]))
    else:
         skipLines-=1




startIndex: int  = 0
endIndex: int  = -1

while True:
    if (v1Volt[startIndex]>0) and (v1Volt[startIndex+1]<0):
        break
    else:
        startIndex+=1

while True:
    if (v1Volt[endIndex]<0) and (v1Volt[endIndex-1]>0):
        break
    else:
        endIndex-=1



def sinFunc(t):
    t = np.array(t)
    return np.sin(t*2*np.pi*1000)

v1Volt = v1Volt[startIndex:endIndex]
tSecond = tSecond[startIndex:endIndex]
v2HighVolt = v2HighVolt[startIndex:endIndex]
v2LowVolt = v2LowVolt[startIndex:endIndex]



for t in tSecond:
    tMovedMilliSecond.append((t+abs(tSecond[0]))*1000)

goalHigh = sinFunc(tSecond)*5*0.501187
goalLow = sinFunc(tSecond)*5*0.1778279

plt.style.use("seaborn-v0_8-dark")
# plt.style.use("seaborn-v0_8-poster")
# plt.style.use("seaborn-v0_8-talk")
plt.axhline(y = 0,color="black",linestyle="--")
plt.axvline(x=0, color="black",linestyle="--")
plt.plot(tMovedMilliSecond,v1Volt,label="V1(t)")
plt.plot(tMovedMilliSecond,v2HighVolt,label="V2(t)(minst demping)")
plt.plot(tMovedMilliSecond,v2LowVolt,label="V2(t)(maks demping)")
# plt.plot(tMovedMilliSecond,goalHigh,linestyle="dotted")
# plt.plot(tMovedMilliSecond,goalLow,linestyle="dotted",marker='o',markersize=0.5)

plt.grid()
plt.yticks(np.linspace(-5,5,11))
plt.gca().yaxis.set_major_formatter(mticker.FormatStrFormatter('%.1f V'))
plt.gca().xaxis.set_major_formatter(mticker.FormatStrFormatter('%.1f ms'))
plt.title("Måling av V1(t) sammen med ytterpunktene for V2(t)")
plt.xlabel("Tid[ms]")
plt.ylabel("Spenning[V]")
plt.legend(frameon=True,edgecolor="dimgray",facecolor="lavender")
plt.savefig(fname="Plot 1", dpi=1000) 
plt.show()