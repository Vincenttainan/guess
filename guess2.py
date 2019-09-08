import random

x=random.randint(1,999)
count=0
while True:
	count=count+1
	num=input('Guess a number:')
	num=int(num)
	if num<x:
		print('Bigger!')
	if num>x:
		print('Smaller!')
	if num==x:
		print('Great!!')
		break
	print(count)
print('You guess ',count,' times!!')