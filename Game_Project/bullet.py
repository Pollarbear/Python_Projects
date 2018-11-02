#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  bullet.py


import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
	"""A class to manage bullets fired from the ship"""
	
	def __init__(self,a1_settings,screen,ship):
		""" create bullet object at the ship's current position"""
		super().__init__()
		self.screen = screen
		
		#create bullet (0,0) position and then set the correct position
		self.rect = pygame.Rect(0,0,a1_settings.bullet_width,a1_settings.bullet_height)
		self.rect.centerx = ship.rect.centerx
		self.rect.top = ship.rect.top
		
		#store the bullet's position as decimal value
		self.y = float(self.rect.y)
		
		self.color = a1_settings.bullet_color
		self.speed_factor = a1_settings.bullet_speed_factor
	
	def update(self):
		"""Move the bullet up the screen"""
		self.y -= self.speed_factor
		self.rect.y = self.y
	
	def draw_bullet(self):
		"""Draw the bullet on the screen"""
		pygame.draw.rect(self.screen,self.color,self.rect)
		
