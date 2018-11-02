#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Dictionary.py
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

alien_0 = {'color': 'red', 'points': 10} 
alien_1 = {'color': 'blue', 'points': 20}
alien_2 = {'color': 'green', 'points': 30}
alien_3 = {'color': 'purple', 'points': 40}

print(str(alien_0.keys()))

my_list = [alien_0,alien_1,alien_2,alien_3 ]


alien_5 = {'one': 'ONE', 'two': [1,2],'three':[1,2,3]}
print(alien_5)

for values  in alien_5['three']:
  print("\t" + str(values))

alien_6 =  { 'number1':{'one': 1, 'two': [1,2]}, 'number2':{'three' :[1,2,3], 'four': [1,2,3,4]}}
print (alien_6['number1'].values())

user_message = 'Please input value:'
print(input(user_message))

#while loop test

i=1
user_input = ""
flag = True
while user_input!='QUIT':
	user_input = input('enter number')
	print(user_input )
	i+=1
	print (i)

while flag:
 print (flag )
 flag = False	

lists = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
new_list = []
while lists:
	print(lists)
	new_list.append(lists.pop())
	print(new_list)

print(new_list)

while 'cat' in new_list:
	new_list.remove('cat')
print (new_list)


