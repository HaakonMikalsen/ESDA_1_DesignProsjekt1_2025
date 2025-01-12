import codecs
import csv
import numpy as np

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

goalLow = -15
goalHigh = -6

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

minReductuinDB = 20*np.log10(max(v2HighVolt)/max(v1Volt))
maxReductuinDB = 20*np.log10(max(v2LowVolt)/max(v1Volt))

print(f"Redcution 1: {minReductuinDB}, diff form goal: {abs(minReductuinDB-goalHigh)}")
print(f"Redcution 2: {maxReductuinDB}, diff form goal: {abs(maxReductuinDB-goalLow)}")


resultFile = open("Results.txt",mode="w",encoding="utf-8")
resultFile.write(f"Redcution 1: {minReductuinDB}, diff form goal: {abs(minReductuinDB-goalHigh)}")
resultFile.write(f"\nRedcution 2: {maxReductuinDB}, diff form goal: {abs(maxReductuinDB-goalLow)}")