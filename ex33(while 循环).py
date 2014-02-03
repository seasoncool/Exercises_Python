#coding:utf-8

#while 循环

i = 0
numbers = []
while i < 6:
	print "At the top i is %d"%i
	numbers.append(i)

	i = i+1

	print "Numbers now:",numbers
	print "At bottom i is %d"%i

print "The numbners:"

for num in numbers:
	print num
