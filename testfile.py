#!/usr/bin/env python
'''
	File: TextStatResults.py
	Version: 1.0
	Date: March 2018
	Author: Lynsay A. Shepherd
	Description: Take piece of text and print out results for all tests.
	#Requires TextStat- https://github.com/shivam5992/textstat	
'''


#import stuff
from textstat.textstat import textstat


#main script
if __name__ == '__main__':

	print "TextStat Comparison Script"
	print "--------------------------"
	
	#read in text from the command line
	#This needs to be fixed to deal/escape special characters
	textToCheck = raw_input("Please enter the text you would like to analyse: ") 
	
	#read in text from a file- but what format?
	
	print "\n\n"
	print "Results"
	print "=============================================="
	print "==============================================\n"
	
	print "Syllable Count: " + str(textstat.syllable_count(textToCheck))
	print "Lexicon Count: " + str(textstat.lexicon_count(textToCheck)) #TRUE is default and removes punctuation before counting
	print "Sentence Count: " + str(textstat.sentence_count(textToCheck))
	print "Flesch Reading Ease formula: " + str(textstat.flesch_reading_ease(textToCheck))
	print "Flesch-Kincaid Grade Level: " + str(textstat.flesch_kincaid_grade(textToCheck))
	print "Fog Scale (Gunning FOG Formula): " + str(textstat.gunning_fog(textToCheck))
	print "SMOG Index: " + str(textstat.smog_index(textToCheck))
	print "Automated Readability Index: " + str(textstat.automated_readability_index(textToCheck))
	print "Coleman-Liau Index: " + str(textstat.coleman_liau_index(textToCheck))
	print "Linsear Write Formula: " + str(textstat.linsear_write_formula(textToCheck))
	print "Dale-Chall Readability Score: " + str(textstat.dale_chall_readability_score(textToCheck))
	print "--------------------------------------------------------------"
	print "Readability Consensus based upon all the above tests: " + str(textstat.text_standard(textToCheck))
	print "\n\n"