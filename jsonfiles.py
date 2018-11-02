#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  jsonfiles.py
 
import json

file_name = 'user_preferences.json'

with open(file_name,'a') as file_object:
	for numbers in range(1,10):
		json.dump(numbers,file_object)


	
	
