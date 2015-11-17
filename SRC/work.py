import urllib.request
import urllib.parse
import json
import codecs

def main():
    #获取json文件
    with urllib.request.urlopen('http://www.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1&mkt=en-US') as response:
        result = response.read()
        #print(result)
        s = result.decode()
        s = codecs.encode(s,encoding='utf-8')
        s = s.decode()
        dict = json.loads(s)
        #print(list)
        #print(type(dict))
        keys = dict.keys()
        #print(keys)
        #print(type(keys))
        # print(dict)
        #print(codecs.encode(dict['images'],encoding='utf-8'))
        list = dict['images']
        #print(len(list))
        url = list[0]['url']
        print(url)

        #urllib.request.urlretrieve(url,'E:/Workspace/20151117BingWallpaperWorkspace/BingWallpaper/SRC')
        with urllib.request.urlopen(url) as web:
            jpg = web.read()
            DstDir = "E:\\Workspace\\20151117BingWallpaperWorkspace\\BingWallpaper\\SRC\\"
            FileName = 'BingWallpaper.jpg'
            File = open(DstDir+FileName,'wb')
            File.write(jpg)
            File.close()
            print('end')

#获取url
#下载图片并保存在当前路径

if __name__ == '__main__':
    main()
