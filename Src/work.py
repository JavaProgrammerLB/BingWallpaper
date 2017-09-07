import urllib.request
import urllib.parse
import json
import codecs
from datetime import date
import os

def main():
    #'http://www.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1&mkt=en-US'
    for i in range(20):
        address0 = 'http://www.bing.com/HPImageArchive.aspx?format=js&idx='
        address1 = str(i)
        address2 = '&n=1&mkt=en-US'
        address = address0 + address1 + address2
        response = getJsonResponse(address)
        if response.strip() == 'null':
            DstDir = os.getcwd() + os.path.sep
            print('【请从',DstDir,'查看下载结果】')
            break
        url = getUrl(response)
        #print(url)
        #print('正在下载前{}天的壁纸'.format(i))
        url = "http://www.bing.com" + url
        downloadPic(url,i)

def getJsonResponse(address):
    #获取json文件
    with urllib.request.urlopen(address) as response:
        result = response.read()
        s = result.decode()
        s = codecs.encode(s,encoding='utf-8')
        s = s.decode()
        return s

def getUrl(response):
    dict = json.loads(response)
    keys = dict.keys()
    list = dict['images']
    #获取url
    url = list[0]['url']
    #print(url)
    return url

def downloadPic(url,i):
    with urllib.request.urlopen(url) as dataValue:
        jpg = dataValue.read()
        DstDir = os.getcwd() + os.path.sep
        FileName1 = 'BingWallpaper'
        today = date.today()
        fileDate = date.fromordinal(today.toordinal() - i)
        FileName2 = fileDate.isoformat()
        FileNameEnd = '.jpg'
        FileName=FileName1+FileName2+FileNameEnd

        #下载图片并保存在当前路径
        File = open(DstDir + FileName,'wb')
        File.write(jpg)
        print('正在下载{FileName2}的壁纸'.format(FileName2 = FileName2))
        File.close()

if __name__ == '__main__':
    main()
