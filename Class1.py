#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Class1.py
#  


class Dog():
	"""This is for Class Dog Documentation"""
	def __init__(self,name,age):
		"""Initialize name and age!"""
		self.name = name.title()
		self.age = int(age)
		self.breed = 'Retriever'
		print("Name:" + str(self.name) + " Age:" + str(self.age) )
	
	def sit(self):
		print('Invoked function Class Dog')
		print('Breed:'+ self.breed)
		
	def test_override(self):
	 print('From Dog - you cant override a Dog!')

class Cat():
	""" some cat class attributes and methods"""
	def __init1__(self,arg1):
	 self.variable1 = arg1
	 print(self.variable1)
	
	def test_override(self):
	 print('From Cat - you cant override a cat!' )


class my_native_dog(Dog,Cat):
	def __init__(self,name,age,city,country,location= 'MDR'):
		super().__init__(name,age)
		Cat().__init1__(location)
		self.country = country
		self.city = city
		self.location = location
		print('city:'+ self.city + ' location:'+ self.location)
	def test_override(self):
	 print('Native Dog!  can\'t override me')
	 


dog1 = my_native_dog('labbie','5','NY','USA')
dog1.Cat.test_override()

	
	

