# -*- coding:utf-8 -*-
import os,time
# 下面的命令打开sh文件,运行并把结果赋值给变量time
for n in range(3):
	times = os.popen("./writeIn.sh")
	times = times.read()
	time.sleep(5)
2019年 7月14日 星期日 01时55分01秒 CST
2019年 7月14日 星期日 01时55分06秒 CST
2019年 7月14日 星期日 01时55分11秒 CST
