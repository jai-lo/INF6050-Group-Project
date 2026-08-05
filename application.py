#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Created on: 7/26/2026
@Author: Kevin, Nyeri, Vivian, Lexi, Jaimie
@Course: INF 6050
@University: Wayne State University
@Assignment: Group Project - Final Assignment
    
@Python Version: 3.9x   
@Required Modules: functions.py
    
@Description: This program takes information from the NASA Near Earth Objects 
API and prompts users to enter a date range to output a list of objects that
were near earth during that time. Fromt aht list of objects, users can enter
the ID of a specific asteroid to learn more information like the diamater, the
times it approaches earth, and if it is classified as potentially hazardous.
"""
########################### 
# IMPORT MODULES
###########################

import functions

########################### 
# GLOBAL VARIABLES
###########################
#Global variable that allows for data validation of asteroid ids
valid_ids = []


########################### 
# RUN SCRIPT
###########################


#Prints out introductory information about the program to user
functions.welcomeMessage()
#Prints out new lines for legibility
functions.newLines()

#While loop that continues prompting the user for input until they quit
while True:   
    #Continue asking for dates until valid range is entered
    start_date, end_date = functions.getValidDateRange()
    
    #can this be added to the getValidDateRange function?
    print("\nDate range accepted.")
    print(f"Searching from {start_date} to {end_date}")
    
    #Taking user input into function to get asteroids from the dates entered
    functions.asteroidFeedInfo(start_date, end_date, valid_ids)
    functions.newLines()
    
    #Nested while loop that allows user to continue inputting and retrieving
    #asteroid information until they choose to exit the loop, returning to the
    #beginning of the loop or exiting the program entirely.
    while True:
        #prompting user to choose an asteroid id out of a list of retrieved
        #id information, validating that it exists, and either outputting an 
        #error message or searching for that id in the list of valid ids
        #available
        asteroidId = functions.getAsteroidID(valid_ids)
        #Printing out information about the asteroid
        functions.printAsteroidSummary(asteroidId)
        #prompting user to input another asteroid id, choose another date range
        #or exit the loop entirely
        choice = functions.nextAction()
        
        if choice == "1":
            continue
        if choice == "2":
            #returns date range prompt
            break
        else:
            break
    #Exit/goodbye statement to exit progra  m
    if choice == "3":
        print("Thanks a lot for using the Asteroid Explorer! Goodbye!")
        break
