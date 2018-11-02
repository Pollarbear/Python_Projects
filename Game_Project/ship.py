#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  ship.py
#  

import pygame

class Ship():
	""" Initialize the ship and set its starting position"""
	def __init__(self,a1_settings,screen):
		self.screen = screen
		
		#load ship image and get its rectangles
		self.image = pygame.image.load('D:\Computer_Science\Python Programming\Python Projects\Game_Project\Images\ship.bmp')
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()
		self.a1_settings = a1_settings
		
		#start new ship at the bottom center of thne screen
		self.rect.centerx = self.screen_rect.centerx
		self.rect.bottom = self.screen_rect.bottom
		
		#store decimal value for ship's center
		self.center = float(self.rect.centerx)
		
		#Movement Flag
		self.moving_right = False
		self.moving_left = False
	
	def update(self):
		"""Update ship's position based on movement flag"""
		#Update ship's center value, not the rect
		if self.moving_right and self.rect.right<self.screen_rect.right:
			self.center += self.a1_settings.ship_speed_factor
		elif self.moving_left and self.rect.left>0:
			self.center -= self.a1_settings.ship_speed_factor
		
		#Update rect objectfrom self.center
		self.rect.centerx = self.center
	
	def blitme(self):
		""" Draw the ship ta its current position"""
		self.screen.blit(self.image,self.rect)
		
