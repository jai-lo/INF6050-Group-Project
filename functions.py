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

def welcomeMessage():
    print("\n\nWelcome to Near Earth Asteroid Explorer."
          + "\n\n\t\tType quit to exit at any time..."
          + "\n\n\tWhen you select a date range, this application will pull"
          + "\n\tinformation on all asteroids that were or will be"
          + "\n\tnear earth during that time."
          + "\n\n\tThen, using the corresponding asteroidID,"
          + "\n\tyou can find more information about the asteroids"
          + "\n\twe listed, including appx. diameter,"
          + "\n\tinformation regarding the asteroids approach time,"
          + "\n\tand if the asteroid has the potential to become"
          + "\n\thazardous.")

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
welcomeMessage()
printAsteroidSummary(3542519)

    