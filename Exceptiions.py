#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Exceptiions.py
#  



# Try divisionbyzero error

a=10
b=20
try:
	print(int(b/a))
except:
	print('not possible tp divide by zero')
else:
	print('all is well')


def file_function(file_name):
	try:
		with open(file_name,'r') as file_object:
			f= file_object.readlines()
	except:
		pass
		
	else:
	    print(f)

file_function('abc.txt')
file_function('read_file.txt')

