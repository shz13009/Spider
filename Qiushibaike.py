import requests
import sys
import re
import datetime

PAGE = 1
URL = 'http://qiushibaike.com/hot/page/' 
HEADERS = { 'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.101 Safari/537.36' }
OUTPUT_FILENAME = 'QiuShiBaiKe.txt'
FILE_OPEN_TYPE = 'w'
REGEX = '<div class="author clearfix">.*?<h2>(.*?)</h2>.*?<div class="content">(.*?)</div>(.*?)<div class="stats.*?class="number">(.*?)</i>'
PATH = '../../Jokes/'

s = requests.session()
try:
	resp = s.post(URL + str(PAGE),headers = HEADERS)
	now = datetime.datetime.now()
	f = open(PATH+str(now.year) + str(now.month) + str(now.day)+OUTPUT_FILENAME ,FILE_OPEN_TYPE)
	pattern = re.compile(REGEX,re.S)
	items = re.findall(pattern,resp.text)	
	for item in items:
		haveImg = re.search('img',item[2])
		if not haveImg:
			f.write("Author:"+item[0])
			f.write(item[1].replace('<br/>','\n'))
			f.write("Reviews:"+item[3])
			f.write("\n---------------------------------------------Divide---------------------------------------------\n")
finally:
	f.close()
