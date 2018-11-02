#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Class_UnitTest.py
#  
  

import unittest
from SurveyClass import AnonymousSurvey


class TestAnonymousSurvey(unittest.TestCase):
	""" Description"""
	
	
	def test_store_single_responses(self):
		""" Definition """
		question = 'How many languages do you speak?'
		my_survey = AnonymousSurvey(question)
		my_survey.store_response('5')
		self.assertIn('5',my_survey.responses)

unittest.main()
