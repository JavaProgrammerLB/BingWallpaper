import urllib.request
import urllib.parse
import json
import codecs
from datetime import date
import os

def main():
    url = getUrl()
    downloadPic(url)

def getUrl():
    #获取json文件
    with urllib.request.urlopen('http://www.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1&mkt=en-US') as response:
        result = response.read()
        s = result.decode()
        s = codecs.encode(s,encoding='utf-8')
        s = s.decode()
        dict = json.loads(s)
        keys = dict.keys()
        list = dict['images']
        #获取url
        url = list[0]['url']
        print(url)
        return url

def downloadPic(url):
    with urllib.request.urlopen(url) as dataValue:
        jpg = dataValue.read()
        DstDir = os.getcwd() + '\\'
        FileName1 = 'BingWallpaper'
        FileName2 = date.today().isoformat()
        FileNameEnd = '.jpg'
        FileName=FileName1+FileName2+FileNameEnd

        #下载图片并保存在当前路径
        File = open(DstDir + FileName,'wb')
        File.write(jpg)
        File.close()
        print('【请从',DstDir,'查看下载结果】')

if __name__ == '__main__':
    main()
