#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Class_python.py
#  
 
file_name = 'write_file.txt'

with open(file_name,'w') as file_object:
	print(file_name)
	for row in range(1,11):
	  file_object.write(str(row) +"\t")
	  
  
