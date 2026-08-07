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
    
@Description: This user-defined module contains the functions necessary to run
the code in application.py.  application.py takes information from the 
NASA Near Earth Objects API and prompts users to enter a date range to 
output a list of objects that were near earth during that time. 
From that list of objects, users can enter the ID of a specific asteroid to l
earn more information like the diameter, the times it approaches earth, 
and if it is classified as potentially hazardous.
"""
########################### 
# IMPORT MODULES
###########################
import requests
from datetime import datetime
import time
import sys



########################### 
# GLOBAL VARIABLES
###########################

#valid_ids = []
#Storing API Key and URL as global variables
API_KEY = "PMDQ9G2dHAgOeblEDAJs8cD2z4l9XyMtcMKTIjLm"
BASE_URL = "https://api.nasa.gov/neo/rest/v1/feed"

########################### 
# USER-DEFINED FUNCTIONS
###########################

#Uses time function to delay the carrying out of a statement by once second 
def timeDelay(amount=1):
    time.sleep(amount)

#Prints out two new lines for legibility
def newLines():
    print("\n\n")

#Prints out message
def welcomeMessage():
    print("\n\nWelcome to Near Earth Asteroid Explorer.")
    timeDelay(2)
    
    print("\n\n\tWhen you select a date range between one and seven days,")
    timeDelay(1)
    print("\n\tthis application will pull information ")
    timeDelay(1)
    print("\n\ton all asteroids that were or will be")
    timeDelay(1)
    print("\n\tnear earth during that time.")
    timeDelay(3)
    print("\n\n\tThen, using the corresponding asteroid ID,")
    timeDelay(1)
    print("\n\tyou can find more information about the asteroids")
    timeDelay(1)
    print("\n\twe listed, including appx. diameter,")
    timeDelay(1)
    print("\n\tinformation regarding the asteroids approach time,")
    timeDelay(1)
    print("\n\tand if the asteroid has the potential to become")
    timeDelay(1)
    print("\n\thazardous.")
    timeDelay(3)
    
    print("\n\n\t\tType quit to exit at any time...")
    
    timeDelay(4)
# Prompt the user to enter the start and end date in format YYYY-MM-DD
# Return both dates as a tuple for date validation and API retrieval.
# Validate:
#   -Ensure the dates are in the correct format,
#   -The end date is not before the start date, and
#   -The date range does not exceed 7 days.
# Returns validated start and end dates as a tuple.

def getValidDateRange():

    while True:
        # Prompt user for date range
        start_date = input("Enter the start date (YYYY-MM-DD): ")
        endTool(start_date)
        timeDelay(1)
        end_date = input("Enter the end date (YYYY-MM-DD): ")
        endTool(end_date)

        try:
            # Convert strings to datetime objects
            start = datetime.strptime(start_date, "%Y-%m-%d")
            end = datetime.strptime(end_date, "%Y-%m-%d")

            # Check that end date is after start date
            if end < start:
                timeDelay(.5)
                print("Error: The end date must be after the start date.\n")
                continue

            # Check NASA API maximum date range
            if (end - start).days >= 7:
                timeDelay(.5)
                print("Error: The date range cannot exceed 7 days.\n")
                continue

            # Return valid dates
            return start_date, end_date

        except ValueError:
            timeDelay(.5)
            print("Error: Please enter dates in the format YYYY-MM-DD.\n")

def asteroidFeedInfo(start_date: str, end_date:str, valid_ids) -> bool:
    #Setup query 
    params = {"start_date": start_date, "end_date": end_date, "api_key": API_KEY}
    
    try:
        timeDelay(2)
        print(f"Fetching Asteroid Feed from {start_date} to {end_date}\n")
        response = requests.get(BASE_URL, params=params)
        
        #Raise an exception for HTTP errors
        response.raise_for_status()
        
        #Parse the JSON response
        data = response.json()
        near_earth_objects = data.get("near_earth_objects", {})

        
        #Track total asteroids
        total_asteroids = data.get("element_count", 0)
        timeDelay(4)
        print(f"Total Asteroids Found: {total_asteroids}")
        print("-" * 50)

        # If no asteroids were found, return to date range selection
        if total_asteroids == 0:
            print("No asteroids were found for this date range.")
            print("Please enter a new date range.\n")
            return False

        for date in sorted(near_earth_objects.keys()):
            timeDelay(2)
            print(f"\n DATE:{date}")
            print("=" * 30)
            
            asteroids_on_date = near_earth_objects[date]
            
            print(f"\n{'Asteroid ID':<22} {'Name'}")
            print("-" * 40)

            for asteroid in asteroids_on_date:
                asteroid_id = asteroid.get("id")
                name = asteroid.get("name")
                
                #save ID for later validation
                valid_ids.append(asteroid_id)
                
                print(f"{asteroid_id:<22} {name}")
        return True
                           
    #Error messages
    except requests.exceptions.HTTPError as http_err: 
        print(f"HTTP error occurred: {http_err}")
        return False
    except Exception as err:
        print(f"An unexpected error occurred: {err}")
        return False



def lookupAsteroid(asteroidId):
    #instantiate dictionary to store asteroid information
    data = {}
    #call API to get asteroid information
    response = requests.get(f"https://api.nasa.gov/neo/rest/v1/neo/{asteroidId}?api_key={API_KEY}")
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
        timeDelay(3)
        print("This asteroid is potentially hazardous.\n")
    else:
        timeDelay(2)
        print("This asteroid is not potentially hazardous.\n")       
    
    timeDelay(2)
    print(f"The asteroid will approach earth {numEarthApproaches} times between {minDate} and {maxDate}\n")
    
    timeDelay(4)
    print("Other information about this asteroid:\n")
    timeDelay(2)
    print(f"\tEstimated diameter: {diameterFeetMin} - {diameterFeetMax} feet.\n")

    timeDelay(2)
    print(f"\tThis asteroid was first observed on {firstObserved}"
          + f"\n\tand was most recently observed on {lastObserved}")

def nextAction():
#to ask what the user wants to do after ID information results

    while True:
        timeDelay(5)
        print("\nWhat would you like to do next?")
        print("1 - Learn about another asteroid")
        print("2 - Enter a new date range")
        print("3 - Quit")

        choice = input("\nChoice: ").strip()
        timeDelay(1.5)
        endTool(choice)

        if choice in("1", "2", "3"):
            return choice
        
        else:
            timeDelay(.5)
            print('Invalid selection. Please enter 1, 2, or 3')

def validateAsteroidId(asteroid_id, valid_ids):
    #validate that inputted asteroid ID exists in the feed results#
    return asteroid_id in valid_ids

def getAsteroidID(valid_ids):
    #asking asteroid ID input#
    timeDelay(2)
    while True:
        asteroid_id = input(
            "\nEnter an asteroid ID for more information: ").strip()
        endTool(asteroid_id)

        if asteroid_id.lower() == "quit":
            return None

        if validateAsteroidId(asteroid_id, valid_ids):
            return asteroid_id
            
        print("Invalid ID, please choose an asteroid ID from the list.")
        
    

    print(f"\tthis asteroid was first observed on {firstObserved} and was most recently observed on {lastObserved}")

def endTool (user_input):
    #establish kill switch for ending program at any point when input is required
    ''' to follow each prompted input if user wants to end game '''
    if user_input.lower() == 'quit':
        timeDelay(3)
        print ('\nThanks for trying the Asteroid Explorer! Until next time.')
        sys.exit()
