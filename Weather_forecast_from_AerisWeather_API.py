#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 24 12:56:28 2018

@author: antonstepanov
"""

# The code below allows to get the current weather for a given location (Berlin 
# in this case). To specify the location, you will need to enter a city name and the
# country code after "/observations/" in the hyperlink ("request" variable). 

# There are some output parameters in the hyperlink  
# i.e. "fields=ob.tempC,ob.humidity,ob.weather,ob.feelslikeC".
# In this example I am asking to show me a temperature in Celsius, humidity, 
# short weather description and feels like parameters.  

# At the end of the link there are client_id=HT1y9PRAteZS5cNGUrPxt & 
# client_secret=AgwadVnqbT1VPY3q4lXddR3iafqvdk4e3Grzz9wz - my identification 
# parameters (you will get them after the registration on AerisWeather). 

import urllib
import json

user_input = str(input("Enter city and country code (e.g. tilburg,nl):"))	
url_part1 = 'https://api.aerisapi.com/observations/'
url_part2 = '?&format=json&filter=allstations&limit=1&fields=ob.tempC,ob.humidity,ob.weather,ob.feelslikeC&client_id=6pbp6hjlWDJXf4OnByC6o&client_secret=NGU28dBl2UxX6c11od9gecDLXFBE2S5vutllMvj5'	
#I changed the client_id and client_secret from Anton's to my own, you can adjust that accordingly

request = urllib.request.urlopen(url_part1 + user_input + url_part2) #combining the url_part1 and 2 and the user_input together into a single url

response = request.read()
result = json.loads(response) #I changed the previous 'json' to 'result' so it doesn't get mixed with the json. module

if result['success']: 
    result = result['response'] #this basically removes the unnecessary dictionaries (the 'success': True etc. so we can print just the important part i.e. the 'response')
    
    lines = ("Temperature (C): " + str(result['ob']['tempC']), #unpacking the dictionary, using the keys
          "Humidity: " + str(result['ob']['humidity']) + " %",
          "Sky: " + str(result['ob']['weather']),
          "Feels like (C): " + str(result['ob']['feelslikeC']))
    for line in lines: #to print them in separate lines
        print(line)
else:
	print("An error occurred: %s" % (json['error']['description']))
	request.close()

if str(result['ob']['weather']) == "Mostly Cloudy":
    print("Whatever the clouds plan to do; always trust in the sun which never fails to come out.")
if str(result['ob']['weather']) == "Cloudy":
    print("Behind the clouds, the sun is still shining!")
    #"Partly Cloudy", "Mostly Sunny", "Mostly Clear", "Sunny", "Clear", "Fog" --> still to be added (I'm also not sure if this is complete)





# This code allows to get a 7 days forecast for Milan. ----> This has not been edited
import urllib
import json
		
request = urllib.request.urlopen('https://api.aerisapi.com/forecasts/milan,it?&format=json&filter=daynight&limit=7&fields=periods.maxTempC,periods.minTempC,periods.pop,periods.weather&client_id=6pbp6hjlWDJXf4OnByC6o&client_secret=NGU28dBl2UxX6c11od9gecDLXFBE2S5vutllMvj5')
response = request.read()
json = json.loads(response)
if json['success']:
	print(json)
else:
	print("An error occurred: %s" % (json['error']['description']))
	request.close()