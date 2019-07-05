#list = [3,1,5,4,2,0,1]
list = [1,2,3,4]
length = len(list)
for i in range(length-1):
	print('i=',i)
	for j in range(i+1,length):
		print(' j=',j)
		if list[i] > list[j]:
			temp = list[i]
			list[i] = list[j]
			list[j] =temp
			#print('  list[i]=',list[i],'\n  list[j]=',list[j],'\n  temp=',temp,'\n')
			print('  list[i]=%s\n  list[j]=%s\n  temp=%s'%(list[i],list[j],temp),'\n')
		print('--------')
	print('list:\n',list,'\n========')
print(list)

