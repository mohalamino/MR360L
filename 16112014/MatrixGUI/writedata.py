x=str(1);
y=str(1);
f=open('calibration.txt','w')
for i in range(60):
    ip = i+101
    ip = str(ip)
    f.write(ip + '.' + x + '.' + y + '\n')
f.close()
