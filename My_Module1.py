#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  My_Module1.py
# my first module
  


def list_funct(list1):
	""" this function modifies the list """
	print(list1)
	list1.append('boom!')
	print("list_funct: " + str(list1))
 
def tup_test(my_name,**tuples):
	""" this function takes any number of arguments"""
	print(tuples)
	print("arg1: " + str(my_name))
 





