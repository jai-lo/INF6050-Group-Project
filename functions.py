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
    #call API to get asteroid information
    response = requests.get(f"https://api.nasa.gov/neo/rest/v1/neo/{asteroidId}?api_key={apiKey}")
    #store asteroid information in dictionary and return it
    data = response.json()
    return data

def printAsteroidSummary(asteroidId):

    asteroid = lookupAsteroid(asteroidId)
    
    #Critical asteroid info
    #####################################
    
    #get information about how hazardous the asteroid is
    isPotentiallyHazardous = asteroid["is_potentially_hazardous_asteroid"]
    
    #get information about how many times this asteroid has/will closely approach Earth
    closeApproaches = asteroid["close_approach_data"]
    #since the API also returns close approaches to other orbiting bodies we should filter down to just close approaches to earth
    earthApproaches = [
      approach for approach in closeApproaches 
      if approach["orbiting_body"].lower() == "earth"
      ]
    numEarthApproaches = len(earthApproaches)
    #get dates of all Earth approaches
    dates = [approach["close_approach_date"] for approach in earthApproaches]
    minDate = dates[0]
    maxDate = dates[(len(dates)-1)]
    
    #Other asteroid info
    #####################################
    
    #get asteroid diameter
    diameterFeetMin =  asteroid["estimated_diameter"]["feet"]["estimated_diameter_min"]
    diameterFeetMax = asteroid["estimated_diameter"]["feet"]["estimated_diameter_max"]
    
    #get observation dates
    firstObserved = asteroid["orbital_data"]["first_observation_date"]
    lastObserved = asteroid["orbital_data"]["last_observation_date"]

    #Print summary
    #############################
    print ("-----------------------------------")
    print(f"Asteroid: {asteroidId}")
    print ("-----------------------------------\n")
    
    if isPotentiallyHazardous:
        print("This asteroid is potentially hazardous.\n")
    else:
        print("This asteroid is not potentially hazardous.\n")       
    
    print(f"The asteroid will approach earth {numEarthApproaches} times between {minDate} and {maxDate}\n")
    
    
    print("Other information about this asteroid:\n")
    print(f"\tEstimated diameter: {diameterFeetMin} - {diameterFeetMax} feet.\n")
    
    print(f"\tthis asteroid was first observed on {firstObserved} and was most recently observed on {lastObserved}")
    

#######Testing
printAsteroidSummary(3542519)

    