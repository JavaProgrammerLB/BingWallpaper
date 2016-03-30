#-*-coding:utf-8
"""
	Author:Charles Lau
	Date:31/3/2016
	简单的bing首页图片爬取程序
	定时需要配置crontab来做

"""
import requests
import json
import logging
import os

seed = 'http://www.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1&mkt=en-US'

logging.basicConfig(level=logging.DEBUG,  
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',  
                    datefmt='%a, %d %b %Y %H:%M:%S',  
                    filename='log/spider.log',  
                    filemode='w') 

class BingSpider:

	def __init__(self,base_dir='bing'):
		self.base_dir = base_dir
		if not os.path.exists(base_dir):
			os.makedirs(base_dir)
	
	def download_img(self,url):
		img = requests.get(url,stream=True)
		img_name = url.split('/')[-1]
		with open(os.path.join(self.base_dir,img_name),'wb') as img_file:
			for chunk in img.iter_content(chunk_size=1024):  
            			if chunk: 
                			img_file.write(chunk)  
                			img_file.flush()  
        		img_file.close()
			
		

	def retrieve_url(self,seed_=seed):
		try:
			rep = requests.get(seed_)
			url = rep.json()['images'][0]['url']

		except:
			url = ''

		return url

	def _run(self):
		url = self.retrieve_url()
		if url:
			logging.debug(u'图片地址为'+url)
			self.download_img(url)
		else:
			logging.debug(u'获取图片地址失败')

		
	def run(self):
		self._run()


if __name__=='__main__':
	spider = BingSpider()
	spider.run()

