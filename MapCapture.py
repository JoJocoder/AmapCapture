# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from PIL import ImageGrab
from PIL import Image
import argparse
import os

def args_parse():
    # construct the argument parse and parse the arguments
    ap = argparse.ArgumentParser()
    ap.add_argument("-p", "--path", type=str, default="G:/Datas/Pic",
                    help="path to output picture")
    args = vars(ap.parse_args()) 
    return args

args = args_parse()
filepath = args['path']
browser = webdriver.Chrome()
url = os.getcwd()+"/MapCapture.html"
browser.maximize_window() 
browser.get(url)
browser.execute_script(
"map.setZoomAndCenter(14, [118.79484,32.054227]);"
)
start=time.time()
r = browser.execute_script("return startpoint")
#s=browser.execute_script("return $('#normalMap').val();")
#s=browser.find_element_by_tag_name('#normalMap').get_attribute('value')

def findStartPoint(points):
#if browser.execute_script("return $('#normalMap').val();")=='卫星图':
	Sleeptime=1.5
	browser.execute_script("map.setZoomAndCenter(18,startpoint);")
	time.sleep(2)
	browser.execute_script("addLngLat()")
	# else:
		# Sleeptime=1.5
		# browser.execute_script("map.setZoomAndCenter(19,startpoint);")
		# browser.execute_script("addLngLat()")
	#time.sleep(3)
	countH=int(browser.execute_script("return countH")/2+1)
	countW=int(browser.execute_script("return countW")/2+1)
	toImage = Image.new('RGBA', (512*countW,512*countH))
	for h in range(countH):
		for w in range(countW):
			if h%2==0:
				im=ImageGrab.grab(bbox=(450,150,962,662))
				toImage.paste(im, (w*512, h*512))
				browser.execute_script("addLngLat()")
				browser.execute_script("map.panBy(-512,0);")
			else:
				#if w!=0:
				im=ImageGrab.grab(bbox=(450,150,962,662))
				toImage.paste(im, ((countW-w-1)*512, h*512))
				browser.execute_script("addLngLat()")
				browser.execute_script("map.panBy(512,0);")
				# else:
					# im=ImageGrab.grab(bbox=(450,150,962,662))
					# toImage.paste(im, ((countW-w)*512, h*512))
					# browser.execute_script("map.panBy(512,0);")
				# print(countW-w)
			time.sleep(Sleeptime)
		if h%2==0:
			browser.execute_script("map.panBy(512,0);")
		else:
			browser.execute_script("map.panBy(-512,0);")
			# im=ImageGrab.grab(bbox=(150,150,662,662))
			# toImage.paste(im, (w*512, h*512))
		# browser.execute_script("map.setZoomAndCenter(18,startpoint);")
		# time.sleep(1)
		# for i in range(h+1):
		browser.execute_script("map.panBy(0,-512);")
		time.sleep(Sleeptime)
	toImage.save(r'{path}\{name}.jpg'.format(path=filepath,name=time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime())))
	#listl=browser.execute_script("return lnglatpointsl")
	listl=[]
	listl.append(['LngLatData'])
	browser.execute_script("maxmin()")
	time.sleep(1)
	listl.append(browser.execute_script("return minll"))
	listl.append(browser.execute_script("return maxll"))
	listl.append(['H:{}'.format(countH),'W:{}'.format(countW)])
	#listr=browser.execute_script("return lnglatpointsr")
	f=open(r'{}\lnglat.txt'.format(filepath),'w')
	for i in listl:
		k=','.join([str(j) for j in i])
		f.write(k+"\n")
	# for m in listr:
		# s=' '.join([str(k) for k in m])
		# f.write(s+"\n")
	f.close()
print('卫星地图下载完成')
def findStartPointM(points):
	browser.find_element_by_id("normalMap").click()
	browser.find_element_by_id("roadnet").click()
#if browser.execute_script("return $('#normalMap').val();")=='卫星图':
	Sleeptime=0.5
	browser.execute_script("map.setZoomAndCenter(18,startpoint);")
	time.sleep(2)
	browser.execute_script("addLngLat()")
	# else:
		# Sleeptime=1.5
		# browser.execute_script("map.setZoomAndCenter(19,startpoint);")
		# browser.execute_script("addLngLat()")
	time.sleep(3)
	countH=int(browser.execute_script("return countH")/2+1)
	countW=int(browser.execute_script("return countW")/2+1)
	toImage = Image.new('RGBA', (512*countW,512*countH))
	for h in range(countH):
		for w in range(countW):
			if h%2==0:
				im=ImageGrab.grab(bbox=(450,150,962,662))
				toImage.paste(im, (w*512, h*512))
				browser.execute_script("addLngLat()")
				browser.execute_script("map.panBy(-512,0);")
			else:
				#if w!=0:
				im=ImageGrab.grab(bbox=(450,150,962,662))
				toImage.paste(im, ((countW-w-1)*512, h*512))
				browser.execute_script("addLngLat()")
				browser.execute_script("map.panBy(512,0);")
				# else:
					# im=ImageGrab.grab(bbox=(450,150,962,662))
					# toImage.paste(im, ((countW-w)*512, h*512))
					# browser.execute_script("map.panBy(512,0);")
				# print(countW-w)
			time.sleep(Sleeptime)
		if h%2==0:
			browser.execute_script("map.panBy(512,0);")
		else:
			browser.execute_script("map.panBy(-512,0);")
			# im=ImageGrab.grab(bbox=(150,150,662,662))
			# toImage.paste(im, (w*512, h*512))
		# browser.execute_script("map.setZoomAndCenter(18,startpoint);")
		# time.sleep(1)
		# for i in range(h+1):
		browser.execute_script("map.panBy(0,-512);")
		time.sleep(Sleeptime)
	toImage.save(r'{path}\{name}.jpg'.format(path=filepath,name=time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime())))
	# listl=browser.execute_script("return lnglatpointsl")
	# listl.append(['H:{}'.format(countH),'W:{}'.format(countW)])
	#listr=browser.execute_script("return lnglatpointsr")
	# f=open(r'{}\lnglat.txt'.format(filepath),'w')
	# for i in listl:
		# k=' '.join([str(j) for j in i])
		# f.write(k+"\n")
	# for m in listr:
		# s=' '.join([str(k) for k in m])
		# f.write(s+"\n")
	# f.close()
print('建筑底图下载完成')
while True:
	r = browser.execute_script("return startpoint")
	time.sleep(1)
	if r!=[]:
		findStartPoint(r)
		findStartPointM(r)
		break

end=time.time()
print('程序用时：' + str(end - start) + '秒')
