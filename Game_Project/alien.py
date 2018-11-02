#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  alien.py
 

import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
	""" A class to represent single Alien fleet""" 
	def __init__(self,a1_settings,screen):
		"""Initialize alien and set its starting position"""
		super().__init__()
		self.screen = screen
		self.a1_settings = a1_settings
		
		#Load alien image and set its starting position
		#self.image = pygame.image.load('D:\Computer_Science\Python Programming\Python Projects\Game_Project\Images\alien.bmp')
		self.image = pygame.image.load('D:\Computer_Science\Python Programming\Python Projects\Game_Project\Images\Allien.bmp')
		self.rect = self.image.get_rect()
		
		#start each alien near the left top of the screen
		self.rect.x = self.rect.width
		self.rect.y = self.rect.height
		
		#store aleine image in exact position
		self.x = float(self.rect.x)
		
	def check_edges(self):
		"""Return True if alien is at edge of screen"""
		screen_rect = self.screen.get_rect()
		if self.rect.right >= screen_rect.right:
			return True
		elif self.rect.left <=0:
			return True
	
	def update(self):
		"""Move the alien right"""
		self.x += (self.a1_settings.alien_speed_factor * self.a1_settings.fleet_direction)
		self.rect.x = self.x
		
		
	def blitme(self):
		"""Draw the alient in it's current position"""
		self.screen.blit(self.image,self.rect)

