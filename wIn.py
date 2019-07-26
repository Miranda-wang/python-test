# -*- coding:utf-8 -*-
import os,time
# 下面的命令打开sh文件,运行并把结果赋值给变量time
for n in range(3):
	times = os.popen("./writeIn.sh")
	times = times.read()
	time.sleep(5)
2019年 7月14日 星期日 02时15分39秒 CST
2019年 7月14日 星期日 02时15分44秒 CST
2019年 7月14日 星期日 02时15分49秒 CST
