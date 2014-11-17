import subprocess
import os

#Senprocess = subprocess.Popen(["sudo"," /usr/sbin/i2cdetect"," -y"," 1"], stdout=subprocess.PIPE , stderr=subprocess.STDOUT )

i2cCMD = "sudo /usr/sbin/i2cdetect -y 1"

print i2cCMD

Senprocess = subprocess.Popen([i2cCMD], stdout=subprocess.PIPE , stderr=subprocess.STDOUT ,shell=True)
stdout, stderr = Senprocess.communicate()

print(stdout)

sen=stdout.find("68")

#sen = os.system("sudo /usr/sbin/i2cdetect -y 1")

print(sen)
