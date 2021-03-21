import json
from urllib.request import urlopen

url = 'https://cn-gdgz-fx-bcache-08.bilivideo.com/upgcxcode/08/88/129528808/129528808_nb2-1-80.flv?e=ig8euxZM2rNcNbK3hwdVhoMMnwdVhwdEto8g5X10ugNcXBlqNxHxNEVE5XREto8KqJZHUa6m5J0SqE85tZvEuENvNo8g2ENvNo8i8o859r1qXg8xNEVE5XREto8GuFGv2U7SuxI72X6fTr859r1qXg8gNEVE5XREto8z5JZC2X2gkX5L5F1eTX1jkXlsTXHeux_f2o859IB_&uipk=5&nbs=1&deadline=1605338879&gen=playurl&os=bcache&oi=3708035747&trid=cd215a88df2a4e48bfd17167f5105d4cp&platform=pc&upsig=e34bc24a9eec5e537153d681b36fa47c&uparams=e,uipk,nbs,deadline,gen,os,oi,trid,platform&cdnid=3808&mid=169568101&orderid=0,3&agrr=0&logo=80000000'

jsonreq = json.dumps({'jsonrpc': '2.0', 'id': 'qwer',
                              'method': 'aria2.addUri',
                              'params': [[url],{'referer': "https://www.bilibili.com/bangumi/play/ss22088/"}],
                              }).encode()
c = urlopen('http://47.242.145.104:6800/jsonrpc', jsonreq)