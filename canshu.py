# -*- coding:utf-8 -*-
def cheng(*num):
	print(len(num))
	print(num)
	if num is None:
		return 0
	else:
		res = 1
		for n in num:
			res = res*n
		return res
#测试
'''
if cheng(5) != 5:
	print('测试失败')
elif cheng(5,6) !=30:
	print('测试失败')
elif cheng(5,6,7) !=210:
	print('测试失败')
elif cheng(5,6,7,9) !=1890:
	print('测试失败')
else:
	try:
		cheng()
		print('测试成功')
	except TypeError:
		print('测试失败')
'''

'''
对可变参数*num进行如下测试时,会发现代码出现了bug
1
([],)
cheng([])= []
'''
#cheng([])
print('cheng([])=',cheng([]))
#也就是说[]并不是None

def demo(*num):
	if  not num: # not num 是指num不是为[],None,'',0.false,{},()这类情况,如果判断只是为None的情况时,就不适用了,
		res = 1
		for n in num:
			res *=n
		return res
	else:
		return 0
print('demo([])=',demo([]))

x = []
x = ''
x = {}
x = None
print( not x) #以上结果都为true
y = []
print(x == y) #结果为false,这说明空的列表,或者元祖,字典,并不是none
print( x is None ) #结果为true
print( y is None ) #结果为false is比较的是对象id 也就是存储地址是否一致,
