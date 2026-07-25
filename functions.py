#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Created on: [date here]
@Author: [author name]
@Course: INF 6050
@University: Wayne State University
@Assignment: [assignment title]
    
@Python Version: 3.9x   
@Required Modules: [required modules]
    
@Description: [code description]
"""
########################### 
# IMPORT MODULES
###########################
import requests


########################### 
# GLOBAL VARIABLES
###########################

apiKey = "PMDQ9G2dHAgOeblEDAJs8cD2z4l9XyMtcMKTIjLm"

########################### 
# USER-DEFINED FUNCTIONS
###########################

def lookupAsteroid(asteroidId):
    #instantiate dictionary to store asteroid information
    data = {}
    response = requests.get(f"https://api.nasa.gov/neo/rest/v1/neo/{asteroidId}?api_key={apiKey}")
    data = response.json()
    return data

    