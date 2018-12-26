#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 24 12:56:28 2018

@author: antonstepanov
"""
# Weather Forecast from AerisWeather API

# The code below allows to check current weather in any location.

# To run the code, you will need:
# 1. Python 3.6 installed in your OS
# 2. AerisWeather client_id and client_secret. You can obtain your own here: 
#    https://www.aerisweather.com/signup/developer/

import urllib # urllib is a package for working with URL 
              # (https://docs.python.org/3/library/urllib.html)
import json # JSON (JavaScript Object Notation)

user_input = str(input("Enter city and country code (e.g. tilburg,nl): "))	
url_part1 = 'https://api.aerisapi.com/observations/'
url_part2 = '?&format=json&filter=allstations&limit=1&fields=ob.tempC,ob.humidity,ob.weather,ob.feelslikeC&client_id=..........&client_secret=..........'	

# There are output parameters in the hyperlink i.e. "fields=ob.tempC,ob.humidity,
# ob.weather,ob.feelslikeC". So we ask to show a temperature in Celsius, 
# humidity, short weather description and feels like parameters.  

# *** IMPORTANT ***
# At the end of the link there are client_id=HT1x1XXXxxZZ5xXXXXXxx & 
# client_secret=AgxxxVaaaT1XXX3q4lXddR3ixxxxx4e3Gxxx9wz - identification 
# parameters, which you will get after the registration on AerisWeather.
# Please register on AerisWeather and update client_id and client_secret in 
# the hyperlink (url_part2) accordingly. 

request = urllib.request.urlopen(url_part1 + user_input + url_part2) 
# using urllib.request function to open and read a URL
# combining the url_part1, url_part2 and the user_input together into one URL

response = request.read()
result = json.loads(response) 

if result['success']: 
    result = result['response'] # this basically removes the unnecessary dictionaries (the 'success': True etc. so we can print just the important part i.e. the 'response')
    
    lines = ("Temperature (C): " + str(result['ob']['tempC']), # using keys to unpack the dictionary 
          "Humidity: " + str(result['ob']['humidity']) + " %",
          "Sky: " + str(result['ob']['weather']),
          "Feels like (C): " + str(result['ob']['feelslikeC']))
    for line in lines: # to print them in separate lines
        print(line)
else:
	print("An error occurred: %s" % (json['error']['description']))
	request.close()
    
    # AREA OF IMPROVEMENT

    # What if there is an error message? => Need to provide the error description. 
    # Validate the user input. If the input does not meet requirements, then ask 
    # the user to try again and show the input example (e.g. tilburg, nl). 
    
    # If a user does not know/did not enter the country code, then provide 
    # a link with the information about country codes 
    # e.g. https://www.worldatlas.com/aatlas/ctycodes.htm (perhaps we can store 
    # it a separate file).
	
group_clear = ["Keep your face to the sunshine and you cannot see a shadow!", "A day without sunshine is like, you know, night.", "I don't complain when it's sunny.", "Change, like sunshine, can be a friend or a foe, a blessing or a curse, a dawn or a dusk."]
group_cloudy = ["Whatever the clouds plan to do; always trust in the sun which never fails to come out.","Behind the clouds, the sun is still shining!", "Who cares about the clouds when we're together? Just sing a song and bring the sunny weather!", "Our mind is like a cloudy sky: in essence clear and pure, but overcast by clouds of delusions. Just as the thickest clouds can disperse, so, too, even the heaviest delusions can be removed from our mind."]
group_hail = ["Joy descends gently upon us like the evening dew, and does not patter down like a hailstorm.", "Life is a hailstorm of distractions. It's not the monster that stops us but the mosquito."]
group_fog = ["All action takes place, so to speak, in a kind of twilight, which like a fog or moonlight, often tends to make things seem grotesque and larger than they really are.", "Most consequential choices involve shades of gray, and some fog is often useful in getting things done.", "It is not the clear-sighted who rule the world. Great achievements are accomplished in a blessed, warm fog.", "Writing is like driving at night in the fog. You can only see as far as your headlights, but you can make the whole trip that way."]
group_frost = ["Life is only a flicker of melted ice.", "It is the life of the crystal, the architect of the flake, the fire of the frost, the soul of the sunbeam. This crisp winter air is full of it.", "Frost is the greatest artist in our clime - he paints in nature and describes in rime.", "The frost makes a flower, the dew makes a star."]
group_rain = ["The way I see it, if you want the rainbow, you gotta put up with the rain.", "The best thing one can do when it's raining is to let it rain.", "If the rain spoils our picnic, but saves a farmer's crop, who are we to say it shouldn't rain?", "Into each life some rain must fall."]
group_snow = ["The Eskimos had fifty-two names for snow because it was important to them: there ought to be as many for love.", "Snow and adolescence are the only problems that disappear if you ignore them long enough.", "Advice is like snow - the softer it falls, the longer it dwells upon, and the deeper it sinks into the mind.", "Courtesies cannot be borrowed like snow shovels; you must have some of your own."]
group_thunderstorm = ["After every storm the sun will smile; for every problem there is a solution, and the soul's indefeasible duty is to be of good cheer.", "The fishermen know that the sea is dangerous and the storm terrible, but they have never found these dangers sufficient reason for remaining ashore.", "After a storm comes a calm.", "The more violent the storm, the quicker it passes."]

code_clear = ["Clear", "Fair", "Fair/Mostly Sunny", "Mostly Sunny", "Sunny", "Mostly Clear"]
code_cloud = ["Cloudy", "Partly Cloudy", "Mostly Cloudy", "Overcast", "Cloudy/Overcast", "Mostly Cloudy with Mist and Fog","Cloudy with Mist and Fog"]
code_fog = ["Fog", "Ice Fog", "Haze", "Mist", "Freezing Fog"]
code_rain = ["Rain", "Drizzle", "Rain showers", "Freezing drizzle", "Freezing rain", "Mostly Cloudy with Light Rain"]
code_frost = ["Frost", "Ice Pellets", "Ice Pellets/Sleet", "Ice Crystals"]
code_snow = ["Snow", "Rain/snow mix", "Snow/sleet mix", "Wintry mix (snow, sleet, rain)", "Snow showers", "Cloudy with Light Snow"]

import random 

if str(result['ob']['weather']) in code_clear:
    choose_quote = random.choice(group_clear)
    print(choose_quote)

if str(result['ob']['weather']) in code_cloud:
    choose_quote = random.choice(group_cloudy)
    print(choose_quote)

if str(result['ob']['weather']) in code_fog:
    choose_quote = random.choice(group_fog)
    print(choose_quote)

if str(result['ob']['weather']) in code_rain:
    choose_quote = random.choice(group_rain)
    print(choose_quote)

if str(result['ob']['weather']) in code_frost:
    choose_quote = random.choice(group_frost)
    print(choose_quote)

if str(result['ob']['weather']) in code_snow:
    choose_quote = random.choice(group_snow)
    print(choose_quote)

if str(result['ob']['weather']) == "Hail":
    choose_quote = random.choice(group_hail)
    print(choose_quote)

if str(result['ob']['weather']) == "Thunderstorm":
    choose_quote = random.choice(group_thunderstorm)
    print(choose_quote)
	
	
# Sending text messages with Python 
    
# You will need:
# 1. virtualenv, enter "pip install virtualenv" in the terminal 
# If it does not work refer to https://virtualenv.pypa.io/en/latest/installation/ 
# there are alternative approaches for installation. I used this source: 
# https://www.fullstackpython.com/blog/python-3-flask-green-unicorn-ubuntu-1604-xenial-xerus.html.
    
# 2. a free Twilio account to use their SMS web API
# Go to https://www.twilio.com/try-twilio and create a free trial account. 
# The Twilio trial account allows you to send text messages to your own phone 
# number. In order to do that you will need to validate your phone number and 
# get a free trial number. 
    
# Note: after the registration you will get some free credits. Each text message
# will reduce your free credits balance, so use messages wisely. 

# 3. Twilio Python helper library 
# Install the Twilio Python helper library by entering "pip install twilio"
# in the terminal. For screenshots and more detailed instructions, please refer
# to https://pypi.org/project/twilio/.
    
# If anything in the above instruction is unclear or does not work, please refer 
# to the original article. The link is below. 
# https://www.fullstackpython.com/blog/send-sms-text-messages-python.html
    
from twilio.rest import Client # we import the Twilio client from the dependency we just installed

sms = str(lines) # this variable is our text message

# the following line needs your Twilio Account SID and Auth Token
# you can find this information in the main Dashboard
client = Client("YOUR Twilio ACCOUNT SID", "YOUR Twilio AUTH TOKEN")

# change the "from_" number to your Twilio number and the "to" number
# to the phone number you signed up for Twilio with, or upgrade your
# account to send SMS to any phone number
client.messages.create(to="+31..........", 
                       from_="+31..........",
                       body = sms)

# AREA OF IMPROVEMENT

# We can set up sms for warning/emergency situations notifications and WhatsApp
# messages for regular weather forecasts.