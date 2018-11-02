#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  SurveyClass.py
#  


class AnonymousSurvey():
	"""This is anonymous survey class"""
	def __init__(self,question):
		self.question = question
		self.responses = []
	
	def show_question(self):
		"""Show the survey question"""
		print(self.question)
	
	def store_response(self,new_response):
		""" Store Responses"""
		self.responses.append(new_response)
	
	def show_results(self):
		"""Show all the responses given"""
		print("Survey Results:")
		for response in self.responses:
			print('- ' + response)
			
