import os
import requests
import time
while True:
    time.sleep(1)
    ot = requests.get("http://quan.suning.com/getSysTime.do")
    if ot.status_code == 200:
        break
ot = eval(ot.text)["sysTime2"].split(' ')
os.system("date {}".format(ot[0].replace('-','/')))
os.system("time {}".format(ot[1]))
