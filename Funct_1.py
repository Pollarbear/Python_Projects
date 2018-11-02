#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Funct_1.py
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

def greet_user(username, address, location,country = ''):
	"""Display a simple greeting."""
	print("hello " + str(len(country)))
	print(country)
	if not country:
	 new_country = 'MADAGASKAR'
	else:
	 new_country = country
	
	list1 = [username,address,location,new_country]
	dict1 = {1:username,2:address,3:location,4:new_country,5:country}
	
	return dict1.items()


	
		
#greet_user2(address,location,country,new_country)

def greet_user2(address,location,country,username): 
	""" Here is the actual greeting!"""
	return country.title()
	

new_country = greet_user(username ='James Wilson Fernandes', address = 'Street 189', location = "NLD")
print (" here we go! " + str(new_country))
