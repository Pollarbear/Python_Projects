#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  alien_invasion.py
#  

import pygame
from Setting import Settings
from ship import *
import game_functions as gf
from pygame.sprite import Group
from bullet import *


def run_game():
	"""Initialize game and create a screen object"""
	pygame.init()
	
	a1_settings=Settings()
	
	screen = pygame.display.set_mode(
	 (a1_settings.screen_width,a1_settings.screen_hight))
	

	pygame.display.set_caption("Alien Invasion")
	
	#Make the Ship, a group of bullets, and a fleet of aliens
	ship = Ship(a1_settings,screen)	
	bullets = Group()
	aliens = Group()
	
	#Create the fleet of aliens
	gf.create_fleet(a1_settings,screen,ship,aliens)
	
   
	
	#start the main loop for the game
	while True:
		
		#watch for kyeboard and mouse events
		gf.check_events(a1_settings,screen,ship,bullets)
		ship.update()
		gf.update_bullets(bullets)
		gf.update_aliens(a1_settings,aliens)		
		gf.update_screen(a1_settings,screen,ship,aliens,bullets)
	
run_game()
