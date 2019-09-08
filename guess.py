import random

x=random.randint(1,999)
while True:
	num=input('Guess a number:')
	num=int(num)
	if num<x:
		print('Bigger!')
	if num>x:
		print('Smaller!')
	if num==x:
		print('Great!!')
		break