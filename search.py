import requests,urllib.parse
from lxml import etree

key = urllib.parse.quote('你的名字')
print(key)
url = 'https://search.bilibili.com/video?keyword='+key
response = requests.get(url).text
selector = etree.HTML(response)
# print(response)
x = selector.xpath('//div[@class="result-wrap clearfix"]//ul[@class="video-contain clearfix"]//li[@class="video matrix"]') 
print(len(x))
for i in x:
    video_href = i.xpath('a/@href')[0]
    video_title = i.xpath('a/@title')[0]
    brief = i.xpath('div[@class="info"]/div[@class="des hide"]/text()')[0].strip()
    guankan = i.xpath('div[@class="info"]/div[@class="tags"]/span[@title="观看"]/text()')[0].strip()
    danmu = i.xpath('div[@class="info"]/div[@class="tags"]/span[@title="弹幕"]/text()')[0].strip()
    upload_time = i.xpath('div[@class="info"]/div[@class="tags"]/span[@title="上传时间"]/text()')[0].strip()
    up_zhu = i.xpath('div[@class="info"]/div[@class="tags"]/span[@title="up主"]/a/text()')[0].strip()

    print((video_href,video_title,brief,guankan,danmu,upload_time,up_zhu))