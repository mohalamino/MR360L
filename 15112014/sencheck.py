import subprocess

Senprocess = subprocess.Popen(["sudo","/usr/sbin/i2cdetect -y 1"], stdout=subprocess.PIPE , stderr=subprocess.STDOUT )
stdout, stderr = Senprocess.communicate()


sen=stdout.find("68")


print(sen)
