import requests
import re
import os
is_ep = False
is_ep = True

headers = {
"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537.36 Core/1.63.6726.400 QQBrowser/10.2.2265.400",
"Cookie":"CURRENT_QUALITY=64; DedeUserID=227050458; "
}
url = 'https://www.bilibili.com/bangumi/play/ep131738'
# url = "https://www.bilibili.com/bangumi/play/ep232520"
# url = "https://www.bilibili.com/bangumi/play/ep77693"
# url = "https://www.bilibili.com/video/av15478453"
# url = "https://www.bilibili.com/bangumi/play/ep131738"
response = requests.get(url,headers=headers)
# print(response.text)
if is_ep:
	zz = '''"epList":(\[\{.*?\}\]),"newestEp":'''
else:
	zz = '''"pages":(\[\{.*?\}\]),"embedPlayer"'''
result = re.findall(zz,response.text)
all_list = eval(result[0])

for i in all_list:
	f = os.popen('node index_ep.js %s'%i['cid']).read()
	print(f)

