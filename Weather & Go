# Weather & Go

import urllib # urllib is a package for working with URL 
              # (https://docs.python.org/3/library/urllib.html)
import json # JSON (JavaScript Object Notation)
import random

user_input = str(input("Enter city and country code (e.g. tilburg,nl): "))	
url_part1 = 'https://api.aerisapi.com/observations/'
url_part2 = '?&format=json&filter=allstations&limit=1&fields=ob.tempC,ob.humidity,ob.weather,ob.feelslikeC&client_id=..........&client_secret=..........'	

# There are output parameters in the hyperlink i.e. "fields=ob.tempC,ob.humidity,
# ob.weather,ob.feelslikeC". So we ask to show a temperature in Celsius, 
# humidity, short weather description and feels like parameters.  

# *** IMPORTANT ***
# At the end of the url_part2 there are client_id=HT1x1XXXxxZZ5xXXXXXxx & 
# client_secret=AgxxxVaaaT1XXX3q4lXddR3ixxxxx4e3Gxxx9wz - identification 
# parameters, which you will get after the registration on AerisWeather.
# Please register on AerisWeather and update client_id and client_secret in 
# the hyperlink (url_part2) accordingly. 

request = urllib.request.urlopen(url_part1 + user_input + url_part2) 
# using urllib.request function to open and read a URL
# combining the url_part1, url_part2 and the user_input together into one URL

response = request.read()
result = json.loads(response) 

count = 0
while result['success'] == False:
     user_input = str(input("Oops, something went wrong. Please try again with city and iso country code (e.g. tilburg,nl):"))
     count += 1
     request = urllib.request.urlopen(url_part1 + user_input + url_part2)
     response = request.read()
     result = json.loads(response)
     
     if count == 2 and result['success'] == False:
         print(" ")
         print("Please refer to https://en.wikipedia.org/wiki/List_of_ISO_3166_country_codes and try again later.")
         request.close()
         break
               
if result['success']: 
     result = result['response'] #this basically removes the unnecessary dictionaries (the 'success': True etc. so we can print just the important part i.e. the 'response')
    
     lines = ("Temperature (C): " + str(result['ob']['tempC']), #unpacking the dictionary, using the keys
          "Humidity: " + str(result['ob']['humidity']) + " %",
          "Sky: " + str(result['ob']['weather']),
          "Feels like (C): " + str(result['ob']['feelslikeC']))
     print(" ")
     for line in lines: #to print them in separate lines
        print(line)

  
     group_clear = ["Keep your face to the sunshine and you cannot see a shadow! (Hellen Keller)", "A day without sunshine is like, you know, night. (Steve Martin)", "I don't complain when it's sunny. (Tim Howard)", "Change, like sunshine, can be a friend or a foe, a blessing or a curse, a dawn or a dusk. (William Artur Ward)"]
     group_cloudy = ["Whatever the clouds plan to do; always trust in the sun which never fails to come out. (Munia Khan)","Behind the clouds, the sun is still shining! (Henry Wadsworth Longfellow)", "Who cares about the clouds when we're together? Just sing a song and bring the sunny weather! (Dale Evans)", "Our mind is like a cloudy sky: in essence clear and pure, but overcast by clouds of delusions. Just as the thickest clouds can disperse, so, too, even the heaviest delusions can be removed from our mind. (Kelsang Gyatso)"]
     group_hail = ["Joy descends gently upon us like the evening dew, and does not patter down like a hailstorm. (Jean Paul)", "Life is a hailstorm of distractions. It's not the monster that stops us but the mosquito. (Robert G. Allen)"]
     group_fog = ["All action takes place, so to speak, in a kind of twilight, which like a fog or moonlight, often tends to make things seem grotesque and larger than they really are. (Carl von Clausewitz)", "Most consequential choices involve shades of gray, and some fog is often useful in getting things done. (Timothy Geithner)", "It is not the clear-sighted who rule the world. Great achievements are accomplished in a blessed, warm fog. (Joseph Conrad)", "Writing is like driving at night in the fog. You can only see as far as your headlights, but you can make the whole trip that way. (E. L. Doctorow)"]
     group_frost = ["Life is only a flicker of melted ice. (Dejan Stojanovic)", "It is the life of the crystal, the architect of the flake, the fire of the frost, the soul of the sunbeam. This crisp winter air is full of it. (John Burroughs)", "Frost is the greatest artist in our clime - he paints in nature and describes in rime. (Thomas Hood)", "The frost makes a flower, the dew makes a star. (Sylvia Plath)"]
     group_rain = ["The way I see it, if you want the rainbow, you gotta put up with the rain. (Dolly Parton)", "The best thing one can do when it's raining is to let it rain. (Henry Wadsworth Longfellow)", "If the rain spoils our picnic, but saves a farmer's crop, who are we to say it shouldn't rain? (Tom Barrett)", "Into each life some rain must fall. (Henry Wadsworth Longfellow)"]
     group_snow = ["The Eskimos had fifty-two names for snow because it was important to them: there ought to be as many for love. (Margaret Atwood)", "Snow and adolescence are the only problems that disappear if you ignore them long enough. (Earl Wilson)", "Advice is like snow - the softer it falls, the longer it dwells upon, and the deeper it sinks into the mind. (Samuel Taylor Coleridge)", "Courtesies cannot be borrowed like snow shovels; you must have some of your own. (John Wanamaker)"]
     group_thunderstorm = ["After every storm the sun will smile; for every problem there is a solution, and the soul's indefeasible duty is to be of good cheer. (William R. Alger)", "The fishermen know that the sea is dangerous and the storm terrible, but they have never found these dangers sufficient reason for remaining ashore. (Vincent Van Gogh)", "After a storm comes a calm. (Matthew Henry)", "The more violent the storm, the quicker it passes. (Paulo Cohelo)"]

     code_clear = ["Clear", "Fair", "Fair/Mostly Sunny", "Mostly Sunny", "Sunny", "Mostly Clear"]
     code_cloud = ["Cloudy", "Partly Cloudy", "Mostly Cloudy", "Overcast", "Cloudy/Overcast", "Mostly Cloudy with Mist and Fog", "Cloudy with Mist and Fog"]
     code_fog = ["Fog", "Ice Fog", "Haze", "Mist", "Freezing Fog"]
     code_rain = ["Rain", "Drizzle", "Rain showers", "Freezing drizzle", "Freezing rain", "Mostly Cloudy with Light Rain", "Mostly Cloudy with Drizzle", "Mostly Cloudy with Heavy Drizzle"]
     code_frost = ["Frost", "Ice Pellets", "Ice Pellets/Sleet", "Ice Crystals"]
     code_snow = ["Snow", "Rain/snow mix", "Snow/sleet mix", "Wintry mix (snow, sleet, rain)", "Snow showers", "Cloudy with Light Snow"]
    
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
