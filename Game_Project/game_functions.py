#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  game_functions.py
 
import sys
import pygame
from bullet import Bullet
from alien import Alien

def get_number_aliens_x(a1_settings,alien_width):
	"""determine no of aliens that fit in a row"""
	available_space_x = a1_settings.screen_width - (2*alien_width)
	number_aliens_x = int(available_space_x/(2*alien_width))
	return number_aliens_x
	
	
def get_number_rows(a1_settings,ship_height,alien_height):
	"""determine no of rows of alien fleet that fit in the screen"""
	available_space_y = a1_settings.screen_hight - 3 * alien_height - ship_height
	number_rows = int(available_space_y/(2*alien_height))
	return number_rows
	

def create_alien(a1_settings,screen,aliens,alien_number,row_number):
	""" Create an alien and place it in the row"""
	alien = Alien(a1_settings,screen)
	alien_width = alien.rect.width
	alien.x = alien_width + 2*alien_width*alien_number
	alien.rect.x = alien.x
	alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
	aliens.add(alien)

def create_fleet(a1_settings,screen,ship,aliens):
	"""Create  full fleet of aliens"""
	alien = Alien(a1_settings,screen)
	alien_width = alien.rect.width
	number_aliens_x = get_number_aliens_x(a1_settings,alien_width)
	number_rows = get_number_rows(a1_settings,ship.rect.height,alien.rect.height)
	
	#create first row of aliens
	for row_number in range(number_rows):
		for alien_number in range(number_aliens_x):
			create_alien(a1_settings,screen,aliens,alien_number,row_number)
		
	


def fire_bullet(a1_settings,screen,ship,bullets):
	""" fire bullet if limit not reached yet"""
	#create new bullet and add it to the group
	new_bullet = Bullet(a1_settings,screen,ship)
	bullets.add(new_bullet)
	

				
def check_keydown_events(event,a1_settings,screen,ship,bullets):
	"""Respond to keypresses"""
	if event.key == pygame.K_RIGHT:
		ship.moving_right = True			
	elif event.key == pygame.K_LEFT:
		ship.moving_left = True	
	elif event.key == pygame.K_SPACE and len(bullets)<a1_settings.bullets_allowed:
		fire_bullet(a1_settings,screen,ship,bullets)
	elif event.key == pygame.K_q:
		sys.exit()

def check_keyup_events(event,ship):
	"""Respond to key releases"""
	if event.key == pygame.K_RIGHT:
		ship.moving_right = False			
	elif event.key == pygame.K_LEFT:
		ship.moving_left = False
	
def check_events(a1_settings,screen,ship,bullets):
	"""watch for kyeboard and mouse events"""
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		elif event.type == pygame.KEYDOWN:
			check_keydown_events(event,a1_settings,screen,ship,bullets)
		elif event.type ==pygame.KEYUP:
			check_keyup_events(event,ship)

	
				

def update_screen(a1_settings,screen,ship,aliens,bullets):
	"""Update images on the screen and flip to the new screen"""
	#redraw the screen during each pass through the loop
	screen.fill(a1_settings.bg_color)
	
	#redraw all bullets behind ship and aliens
	for bullet in bullets.sprites():
		bullet.draw_bullet()
		
	
	ship.blitme()
	aliens.draw(screen)
		
	#Make the most recently drawn screen visible
	pygame.display.flip()


def update_bullets(bullets):
	"""get rid of the bullets that have disappeared"""
	bullets.update()
	for bullet in bullets.copy():
		if bullet.rect.bottom <= 0:
			bullets.remove(bullet)

def check_fleet_edges(a1_settings,aliens):
	"""change direction if any aliens have reached the edge"""
	for alien in aliens.sprites():
		if alien.check_edges():
			change_fleet_direction(a1_settings,aliens)
			break

def change_fleet_direction(a1_settings,aliens):
	""" Drop the entire fleet and change the direction"""
	for alien in aliens.sprites():
		alien.rect.y += a1_settings.fleet_drop_speed
		a1_settings.fleet_direction *= -1



def update_aliens(a1_settings,aliens):
	""" update the position of all aliens in the fleet"""
	#check if the fleet is at the edge and update positions of all alliens in fleet
	check_fleet_edges(a1_settings,aliens)
	aliens.update()
