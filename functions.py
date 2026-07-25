# -*- coding: utf-8 -*-
"""
@Created on: 
@Author: 
@Course: INF 6050
@University: Wayne State University
@Assignment: 
    
@Python Version: 3.8x
@Required Modules: 

@Description:
"""
###########################
# IMPORT MODULES
###########################
import requests

###########################
# Global Variables
###########################
#Storing API Key and URL as global variables
API_KEY = "PMDQ9G2dHAgOeblEDAJs8cD2z4l9XyMtcMKTIjLm"
BASE_URL = "https://api.nasa.gov/neo/rest/v1/feed"
###########################
# USER-DEFINED FUNCTIONS
###########################

def asteroidFeedInfo(start_date: str, end_date:str) -> None:
    #Setup query 
    params = {"start_date": start_date, "end_date": end_date, "api_key": API_KEY}
    
    try: 
        print(f"Fetching Asteroid Feed from {start_date} to {end_date}\n")
        response = requests.get(BASE_URL, params=params)
        
        #Raise an exception for HTTP errors
        response.raise_for_status()
        
        #Parse the JSON response
        data = response.json()
        near_earth_objects = data.get("near_earth_objects", {})
        
        #Track total asteroids
        total_asteroids = data.get("element_count", 0)
        print(f"Total Asteroids Found: {total_asteroids}")
        print("-" * 50)
        
        for date in sorted(near_earth_objects.keys()):
            print(f"\n DATE:{date}")
            print("=" * 30)
            
            asteroids_on_date = near_earth_objects[date]
            
            for asteroid in asteroids_on_date:
                asteroid_id = asteroid.get("id")
                name = asteroid.get("name")
                
                print(f" Asteroid ID: {asteroid_id}")
                print(f" Name: {name}")
                
    #Error messages
    except requests.exceptions.HTTPError as http_err: 
        print(f"HTTP error occurred: {http_err}")
    except Exception as err:
        print(f"An unexpected error occurred: {err}")
        
asteroidFeedInfo("2015-09-07", "2015-09-08")