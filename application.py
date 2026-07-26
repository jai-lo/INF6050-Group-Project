#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Created on: 7/26/2026
@Author: Kevin, Nyeri, Vivian, Lexi, Jaimie
@Course: INF 6050
@University: Wayne State University
@Assignment: Group Project - Final Assignment
    
@Python Version: 3.9x   
@Required Modules: [required modules]
    
@Description: [code description]
- Combine get date function and validate date function 
"""
########################### 
# IMPORT MODULES
###########################

#import functions.py


########################### 
# GLOBAL VARIABLES
###########################

#global variable of start date and end date



########################### 
# USER-DEFINED FUNCTIONS
###########################


########################### 
# RUN SCRIPT
###########################

#welcomeMessage()
welcomeMessage()

# Continue asking for dates until valid range is entered
while True:

    start_date, end_date = getDateRange()

    if validateDateRange(start_date, end_date):
        break

    print("\nInvalid date range. Please try again.\n")

print("\nDate range accepted.")
print(f"Searching from {start_date} to {end_date}")
