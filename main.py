# -*- coding: utf-8 -*-
import os
import sys
import time
import subprocess
import random
from auto_adb import auto_adb
adb=auto_adb()
def random_number():
	global number1
	global number2
	number1=random.randint(1,15)
	number2=random.randint(1,20)
def change_postion(x1,y1):
	random_number()#生成随机数,防止被封
	cmd='shell input tap {x1} {y1}'.format(x1=x1+number1,y1=y1+number2)#点击"搜索""
	print('{}'.format(cmd))
	adb.run(cmd)
def input_text(content):
	cmd='shell am broadcast -a ADB_INPUT_TEXT --es msg \'{content}\''.format(content=content.decode("unicode_escape"))
	print('{}'.format(cmd))
	adb.run(cmd)
def clean_text():
	t=0
	cmd='shell input keyevent 67'#清空验证信息
	while (t<10):
		print('{}'.format(cmd))
		adb.run(cmd)
		t+=1
def pull_screenshot():
    process = subprocess.Popen('adb shell screencap -p', shell=True, stdout=subprocess.PIPE)
    screenshot = process.stdout.read()
    if sys.platform == 'win32':
        screenshot = screenshot.replace(b'\r\n', b'\n')
    f = open('wechat.png', 'wb')
    f.write(screenshot)
    f.close()
def add_friend():
	change_postion(978,144)#点击"+"号
	change_postion(660,426)#点击"添加朋友"
	change_postion(170,360)#点击输入栏
	input_text('123456')#输入对方手机/微信号
	change_postion(340,311)#点击"搜索""
	time.sleep(0.5)#延迟0.5s,防止没加载出来
	change_postion(517,1224)#点击"添加到微信通信录""
	time.sleep(0.5)#延迟0.5s,防止没加载出来
	clean_text()#清除验证信息
	time.sleep(0.5)#延迟0.5s
	input_text('CoelWu')#输入验证信息
	time.sleep(0.5)#延迟0.5s
	change_postion(393,700)#切换至备注
	clean_text()#清除验证信息
	time.sleep(0.5)#延迟0.5s
	input_text('Mr.Ye')#输入好友备注
	change_postion(975,141)#发送请求
	change_postion(51,137)#回退
	change_postion(51,137)#回退
	change_postion(51,137)#回退
#pull_screenshot()
#add_friend()