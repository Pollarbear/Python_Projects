#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  magicians.py
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
i = 0
my_list = []
magicians = ['alice', 'david', 'carolina']
print (magicians)
for name in magicians:
	i=i+1
	print (i)
	print (name)

for values in range(5,9):
	my_list.append(values)
print (my_list)

my_new_list = list(range(1,10,2))
print(my_new_list)

mylist = [num for num in range(25,35)]
print (mylist)

#slicing of the list

my_sliced_list = mylist[-3:]
print (my_sliced_list)

new_list1 = mylist[:]
print (mylist)
print (new_list1)

mylist.append(111)
print (mylist)
print (new_list1)

new_list1.pop()
print (mylist)
print (new_list1)


my_list11 = ['james', 'wilson', "fernandes"]
var = my_list11[:1]
print(var)


my_tuple1 = ('james', 'wilson', "fernandes")
print(my_tuple1[:1])

my_tuple1.append('new_value')
print(my_tuple1)








 


