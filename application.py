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
    
@Description: [code description]
"""
########################### 
# IMPORT MODULES
###########################

import functions

########################### 
# GLOBAL VARIABLES
###########################
valid_ids = []


########################### 
# RUN SCRIPT
###########################

functions.welcomeMessage()
functions.newLines()

while True:   
    # Continue asking for dates until valid range is entered
    start_date, end_date = functions.getValidDateRange()
    
    #can this be added to the getValidDateRange function?
    print("\nDate range accepted.")
    print(f"Searching from {start_date} to {end_date}")
    
    functions.asteroidFeedInfo(start_date, end_date, valid_ids)
    functions.newLines()
    
    
    while True:

        asteroidId = functions.getAsteroidID(valid_ids)
        
        functions.printAsteroidSummary(asteroidId)

        choice = functions.nextAction()
        
        if choice == "1":
            continue
        if choice == "2":
            #returns date range prompt
            break
        else:
            break
        
    if choice == "3":
        print("Thanks a lot for using the Asteroid Explorer! Goodbye!")
        break

    


#functions.getValidDateRange