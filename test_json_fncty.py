#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  test_json_fncty.py
#    

import json

file_name = 'user_preferences.json'

with open(file_name,'r') as file_object:
	numbers=json.load(file_object)
print (numbers)	
	
