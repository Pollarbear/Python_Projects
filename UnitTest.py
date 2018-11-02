#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  UnitTest.py


import unittest
from name_function import get_formated_name

class NamesTestCase(unittest.TestCase):
	"""Test for name_function.py"""
	
	def test_first_last_name(self):
		formatted_name = get_formated_name('james1','wilson')
		self.assertEqual(formatted_name,'James Wilson')
		
	def test_first_last_name2(self):
		formatted_name = get_formated_name('james1','wilson12')
		self.assertEqual(formatted_name,'James1 Wilson123')
unittest.main()
