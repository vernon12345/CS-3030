#!/usr/bin/python
# Vernon Brighton
# Lab 6 - Filemaker
# CS 3030 - Scripting Languages
import random
import shlex
import sys

if len(sys.argv) != 4:
    print("Usage: ./filemaker INPUTCOMMANDFILE OUTPUTFILE RECORDCOUNT")
    exit(1)
    
inpcomm = sys.argv[1]
outp = sys.argv[2]
count = (sys.argv[3])

try:
    count = int(count)
except:
    print("Error with the count")
    exit(1)

try:
    inpcomm = open(inpcomm, 'r')
except:
    print("Error with opening input file")
    exit(1)

try:
    outp = open(outp , 'w')

except:
    print("Error with opening output file")
    exit(1)
cmdL = inpcomm.readlines()
header = shlex.split(cmdL[0])

randomFiles = {}

if header[0] == "HEADER":
    outp .write(header[1].decode('string_escape'))

for i in range(len(cmdL)):
    cmd = shlex.split(cmdL[i])
    if cmd[0] == "FILEWORD":
        inpf = open(cmd[2], 'r')
        randomFiles[cmd[2]] = inpf.readlines()
inpf.close()



randomData = {}
for i in range(count):
    randomData = {}
    for c in range(len(cmdL)):
        cmd = shlex.split(cmdL[c])
        if cmd[0] == "STRING":
            outp .write(cmd[1].decode('string_escape'))
        if cmd[0] == "FILEWORD":
            labl = cmd[1]
            if labl in randomData:
                print("Error key exists")
                exit(1)
            else:
                randstr = randomFiles[cmd[2]][random.randint(0, len(randomFiles[cmd[2]]) - 1)]
                randstr =  randstr .rstrip()
                randomData[cmd[1]] =  randstr
                outp .write(randomData[cmd[1]])
        if cmd[0] == "NUMBER":
            labl = cmd[1]
            snum= int(cmd[2])
            lNum = int(cmd[3])
            if labl in randomData:
                print("Error key exists")
                exit(1)
            else:
                randNum = random.randint(snum, lNum)
                randomData[cmd[1]] = str(randNum)
                outp.write(randomData[cmd[1]])
        if cmd[0] == "REFER":
            labl = cmd[1]
            outp .write(randomData[labl])
exit(0)




