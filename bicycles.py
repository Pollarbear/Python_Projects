#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  bicycles.py
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

bicycles = [ 'one', 'two' , 'three' ]
print (bicycles[0].upper() + bicycles[-3].title())

message = "My list of values are " + bicycles[0]
print (message)

print(bicycles)

bicycles = bicycles + [ 'four', 'five','four']
print (bicycles)
bicycles.append('seven')
print (bicycles)

bicycles.insert(99,'zero')

del bicycles[1]
print (bicycles)

print(bicycles.remove('four'))

print (bicycles)
bicycles.sort()
print (bicycles)
bicycles.sort(reverse = False)
print (bicycles)
bicycles.sort(reverse = True)
print (bicycles)

print(sorted(bicycles,reverse = False))
print(bicycles)
bicycles.reverse()
print (bicycles)

print(len(bicycles))
print (bicycles[int(len(bicycles)/2)])





