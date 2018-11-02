#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  looping.py
#  
#  Copyright 2018 Chris <Chris@DESKTOP-9HVDH8J>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  


my_list = ['james', 'wilson', 'fernandes', 'none']
my_new_list = []
for names in my_list:
 print (names) 
 if names == 'none' or 1==2:
  my_new_list.append(names)
 else:
  my_new_list.append('done!')
print(my_new_list)

mname = 'wilson1'
if mname not in my_list:
	print('YES')
else:
	print('NO')

x = True
y = False
print (x)
print (y)

for num in range(1,4):
 if 1==3 and 2==2:
  print("if condition step 1")
  print("if condition step 2")
  print("if condition step 3")
 elif 31==3:
  print("if condition step 9")
  print("if condition step 10")
 else:
   if 9==9:
    print("if condition step 901")
   else:
    print("if condition step 1801")	 


dict_list = {1:'james', '2':'wilson','3':'fernandes'}
print(dict_list['2'])

dict_list1 = {}
print(dict_list1)

dict_list1['first'] = 'number1'
dict_list1['second'] = 'number2'
dict_list1['third'] = 'number3'
dict_list1['fourth'] = 'number4'

print(dict_list1)

for key in dict_list1.keys():
 print (key + ':')

for values in dict_list1.values():
 print (values + ':')
