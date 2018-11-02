#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Setting.py
#   


class Settings():
	"""A class to store all settings for Alien Invasion"""
	def __init__(self):
		""" iniitialize all screen settings here"""
		self.screen_width = 1350
		self.screen_hight = 650
		self.bg_color = (230,230,230)
		#Ship settings
		self.ship_speed_factor = 1.5
		self.alien_speed_factor = 1
		self.fleet_drop_speed = 10
		#fleet direction of 1 respresents right; -1 represents left
		self.fleet_direction =1
		
		#Bullet Settings
		self.bullet_speed_factor =1
		self.bullet_width = 3
		self.bullet_height = 15
		self.bullet_color = (60,60,60)
		self.bullets_allowed = 3
