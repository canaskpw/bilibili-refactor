import hashlib
import urllib.parse

# appkey = "1d8b6e7d45233436"
# actionKey = "appkey"
# build = "520001"
# device = "android"
# mobi_app = "android"
# platform = "android"
# app_secret = "560c52ccd288fed045859ed18bffd973"
# s = urllib.parse.quote('厨二病')
# print(s)
# str = 'appkey=1d8b6e7d45233436&keyword=%E5%8E%A8%E4%BA%8C%E7%97%85'+app_secret
# sign = hashlib.md5(str.encode('utf-8')).hexdigest()
# print(sign)
import time

timeStamp = 1536114084
timeArray = time.localtime(timeStamp)
pbdatetime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
print(otherStyleTime)