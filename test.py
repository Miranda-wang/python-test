#!/usr/bin/env Python 
#coding:utf-8

# python执行shell的三种方式,执行 shell的echo命令
import os
name = "whl"
os.environ['name'] = str(name) #如果后续使用变量,必须将变量添加到os的环境中,否则不能使用
r = os.system("echo  love $name") #使用os.system 执行结果如果成功,下面的print 将返回0,如果不成功,例如将echo改为p,则会有zh:p:不存在此命令的提示 
print (r)

#方法二: os.popen 读取一个shell脚本文件
f = os.popen("./ech.sh") #在ech.sh文件中命令为echo("I love whl") 
print (f.read()) #执行成功,输出读取的ech文件结果,如果不成功会显示错误原因

#方法三:commands.getstatusoutput 此方法python3已经不可用了,python2尚能使用
#import commands
#(status,output)  = commands.getstatusoutput("./ech.sh") #既输出了执行状态,又输出了结果,成功为0
#print(status,output) 

#方法四:subprocess模块 适用python3,效果同commands
import subprocess
print(subprocess.getstatusoutput("./ech.sh")) #既输出了执行状态,又输出了结果,执行成功为0
