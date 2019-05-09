def remainder(list):
	remainders=[]
	for n in list:
		x=n%3
		remainders.append(x)
	print(remainder)

def sorted(a,b,c):
	d=(a+b+c)
	print(d)

def divisible_by_three(n):
	x=range(1,n)
	for y in x:
	  if n/3==0:
	  	print(n)

def combine(newlist):
	x = [[1,2],[3,4],[5,6]]
	newlist=[ ]
	for sublist in x:
		for y in sublist:
			newlist.append(y)
			print(newlist)

def smallest(list):
	print(min(number))	

def letters(mylist):
	mylist = list(dict.fromkeys(mylist))
	mylist.sort()
	print(mylist)

def squares():
	my_dict=dict()
	for x in range(149, 159):
		my_dict[x]=x/3
		print(my_dict)

def student(age,name):
	for student in students:
		message ="hello {}, you were born in year {}"  .format((2019-age),name)
		print(message) 