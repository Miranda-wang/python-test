list=[3,1,2,5,4]
for i in range(len(list)):
	print('i=',i)
	for j in range(i,0,-1):
		print(' j=',j)
		if	list[j-1] > list[j]:
			#temp = list[j-1]
			#list[j-1] = list[j]
			#list[j] = temp
			#print('  temp = %s\n  list[j-1]=%s\n  list[j]=%s'%(temp,list[j-1],list[j]))
			list[j],list[j-1] = list[j-1],list[j]
			print('   list[j-1]=%s\n   list[j]=%s'%(list[j-1],list[j]))
		print('--------')
		break
	print('list:\n',list,'\n========')	
print(list)

