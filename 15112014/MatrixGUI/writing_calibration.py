ip = 129
lineCount = 0
x=1
y=0

f=open('calibration.txt','r+')
lines = f.readlines()

f.seek(0)

for line in lines:
    lineCount += 1
    if line != '\n' and lineCount < 60:
        currentLine = line.rstrip('\n')
        currentLine = line.split(".")
        if int(currentLine[0]) == ip:
            f.write(str(ip) + '.' + str(x) + '.' + str(y) + '\n')
            print 'updated'
        else:
            f.write(line)
        
f.close()
