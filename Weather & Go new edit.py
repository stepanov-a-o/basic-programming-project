# Weather & Go
# version 1.0.0 

import urllib # urllib is a package for working with URL
	      # we used it to send a get request to AerisWeather
	
import json # JSON (JavaScript Object Notation)
	    # we used it to gather the information through AerisWeather API
	
import random # we used it to display random quotes/wisdom thoughts to a user

client_id = "&client_id=.........." #replace the dots with the client ID e.g. "&client_id=6pbp6xxxxOnByC6o"
client_secret = "&client_secret=............" #replace the dots with the client secret e.g. "&client_secret=NGU28dBl2UxxxtllMvj5"

# *** IMPORTANT ***
# the client_id=.......... & client_secret=.......... are identification parameters, 
# which you will get after the registration on AerisWeather. Please
# refer to README file for a detailed installation instructions. 

degrees = str(input("Would you like to display the temperature in degrees Celsius or Fahrenheit? Type c/f: "))

while degrees != "c" and degrees != "f":   # for when the user types something else than c or f
    degrees = str(input("Please type either c (for Celsius) or f (for Fahrenheit): "))
    if degrees == "c" or degrees == "f":
        break
	
city_country = str(input("Enter the name of the city and an ISO country code (e.g. tilburg,nl): ")) # creating a simple user interface, which allows to 
	     # enter a city and an ISO country code
url_part1 = 'https://api.aerisapi.com/observations/' # using Aeris API to create a request 
url_part2 = "?&format=json&filter=allstations&limit=1&fields=ob.tempC,ob.humidity,ob.weather,ob.feelslikeC"	
	     # splitting a hyperlink into more parts to make it more readable

# There are output parameters in the url_part2 i.e. "fields=ob.tempC,
# ob.humidity,ob.weather,ob.feelslikeC". We request a temperature in 
# Celsius (which can be changed to Fahrenheit later in the code), 
# humidity, short weather description and 'feels like' parameters.  

whole_url = url_part1 + city_country + url_part2 + client_id + client_secret # combining the url parts into one url
request = urllib.request.urlopen(whole_url) # using urllib.request function to open and read our url
response = request.read() # reading the response 
result = json.loads(response) 

# Troubleshooting
count = 0 # counting unsuccessful request attempts

while result['success'] == False:
     city_country = str(input("Oops, something went wrong. Please try again with city and ISO country code (e.g. tilburg,nl):"))
     count += 1
     whole_url = url_part1 + city_country + url_part2 + client_id + client_secret
     request = urllib.request.urlopen(whole_url)
     response = request.read()
     result = json.loads(response)
     
     if count == 2 and result['success'] == False: # if there are more than 2 unsuccessful requests attempts 
	 # the program will show the user a link to a page wiht ISO country codes
         print(" ")
         print("Please refer to https://en.wikipedia.org/wiki/List_of_ISO_3166_country_codes and try again later.")
         request.close()
         break
		
# Reading the response from AerisWeather and presenting it to a user in Celsius degrees
if result['success'] and degrees == "c": 
     result = result['response'] # removing unnecessary dictionaries (the "success: True" etc. so we can show to a user
				 # only the important part - the "response")
    
     lines = ("Temperature (C): " + str(result['ob']['tempC']), # unpacking the dictionary using keys
          "Humidity: " + str(result['ob']['humidity']) + " %",
          "Sky: " + str(result['ob']['weather']),
          "Feels like (C): " + str(result['ob']['feelslikeC']))
     print(" ") #printing an empty line for aesthetics
     for line in lines: # printing keys on separate lines
        print(line)
	
# Creating wisdom thought categories covering most common weather conditions 
     group_clear = ["Keep your face to the sunshine and you cannot see a shadow! (Hellen Keller)", "A day without sunshine is like, you know, night. (Steve Martin)", "I don't complain when it's sunny. (Tim Howard)", "Change, like sunshine, can be a friend or a foe, a blessing or a curse, a dawn or a dusk. (William Artur Ward)"]
     group_cloudy = ["Whatever the clouds plan to do; always trust in the sun which never fails to come out. (Munia Khan)","Behind the clouds, the sun is still shining! (Henry Wadsworth Longfellow)", "Who cares about the clouds when we're together? Just sing a song and bring the sunny weather! (Dale Evans)", "Our mind is like a cloudy sky: in essence clear and pure, but overcast by clouds of delusions. Just as the thickest clouds can disperse, so, too, even the heaviest delusions can be removed from our mind. (Kelsang Gyatso)"]
     group_hail = ["Joy descends gently upon us like the evening dew, and does not patter down like a hailstorm. (Jean Paul)", "Life is a hailstorm of distractions. It's not the monster that stops us but the mosquito. (Robert G. Allen)"]
     group_fog = ["All action takes place, so to speak, in a kind of twilight, which like a fog or moonlight, often tends to make things seem grotesque and larger than they really are. (Carl von Clausewitz)", "Most consequential choices involve shades of gray, and some fog is often useful in getting things done. (Timothy Geithner)", "It is not the clear-sighted who rule the world. Great achievements are accomplished in a blessed, warm fog. (Joseph Conrad)", "Writing is like driving at night in the fog. You can only see as far as your headlights, but you can make the whole trip that way. (E. L. Doctorow)"]
     group_frost = ["Life is only a flicker of melted ice. (Dejan Stojanovic)", "It is the life of the crystal, the architect of the flake, the fire of the frost, the soul of the sunbeam. This crisp winter air is full of it. (John Burroughs)", "Frost is the greatest artist in our clime - he paints in nature and describes in rime. (Thomas Hood)", "The frost makes a flower, the dew makes a star. (Sylvia Plath)"]
     group_rain = ["The way I see it, if you want the rainbow, you gotta put up with the rain. (Dolly Parton)", "The best thing one can do when it's raining is to let it rain. (Henry Wadsworth Longfellow)", "If the rain spoils our picnic, but saves a farmer's crop, who are we to say it shouldn't rain? (Tom Barrett)", "Into each life some rain must fall. (Henry Wadsworth Longfellow)"]
     group_snow = ["The Eskimos had fifty-two names for snow because it was important to them: there ought to be as many for love. (Margaret Atwood)", "Snow and adolescence are the only problems that disappear if you ignore them long enough. (Earl Wilson)", "Advice is like snow - the softer it falls, the longer it dwells upon, and the deeper it sinks into the mind. (Samuel Taylor Coleridge)", "Courtesies cannot be borrowed like snow shovels; you must have some of your own. (John Wanamaker)"]
     group_thunderstorm = ["After every storm the sun will smile; for every problem there is a solution, and the soul's indefeasible duty is to be of good cheer. (William R. Alger)", "The fishermen know that the sea is dangerous and the storm terrible, but they have never found these dangers sufficient reason for remaining ashore. (Vincent Van Gogh)", "After a storm comes a calm. (Matthew Henry)", "The more violent the storm, the quicker it passes. (Paulo Cohelo)"]

# Creating sky description categories  
     code_clear = ["Clear", "Fair", "Fair/Mostly Sunny", "Mostly Sunny", "Sunny", "Mostly Clear"]
     code_cloud = ["Cloudy", "Partly Cloudy", "Mostly Cloudy", "Overcast", "Cloudy/Overcast", "Mostly Cloudy with Mist and Fog", "Cloudy with Mist and Fog", "Cloudy with Blowing"]
     code_fog = ["Fog", "Ice Fog", "Haze","Hazy", "Mist", "Freezing Fog", "Cloudy with Areas of Fog", "Mostly Clear with Mist and Fog"]
     code_rain = ["Rain", "Drizzle", "Rain showers", "Freezing drizzle", "Freezing rain", "Mostly Cloudy with Light Rain","Mostly Cloudy with Heavy Rain", "Mostly Cloudy with Drizzle", "Mostly Cloudy with Heavy Drizzle", "Cloudy with Drizzle","Cloudy with Heavy Drizzle", "Cloudy with Light Drizzle", "Mostly Cloudy with Light Drizzle", "Cloudy with Light Rain", "Cloudy with Heavy Rain"]
     code_frost = ["Frost", "Ice Pellets", "Ice Pellets/Sleet", "Ice Crystals"]
     code_snow = ["Snow", "Rain/snow mix", "Snow/sleet mix", "Wintry mix (snow, sleet, rain)", "Snow showers", "Cloudy with Light Snow", "Mostly Cloudy with Scattered Snow Showers"]

# Setting up scenarios to display a random wisdom thought corresponding to sky description categories
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
	
     if (str(result['ob']['weather']) not in code_clear) and (str(result['ob']['weather']) not in code_cloud) and (str(result['ob']['weather']) not in code_fog) and (str(result['ob']['weather']) not in code_rain) and (str(result['ob']['weather']) not in code_frost) and (str(result['ob']['weather']) not in code_snow) and (str(result['ob']['weather']) != "Hail") and (str(result['ob']['weather']) != "Thunderstorm"):
         print("The quote for this kind of weather is still in development :)")
    
     from twilio.rest import Client # importing the Twilio Python helper library
			       # we used it to send SMS messages from Python
			       # this is an external library, which you need to install separately 
			       # for installation instructions please refer to README file  

     sms = str(lines) # this variable is our SMS message
		 # to keep SMS messages readable and to save some SMS traffic 
	 	 # our SMS messages only include weather conditions (without wisdom thought) 
	
# the following line needs your Twilio Account SID and Auth Token
# if you do not know where to find your Twilio Account SID and Auth Token please refer to README file 
     account_sid = "....." 
     auth_token = "....."   # replace the dots with the Account SID and Auth Token
     client = Client(account_sid, auth_token)
   
# change the "from_" number to your Twilio number and the "to" number
# to the phone number you signed up for Twilio (during the registration)
     client.messages.create(to="+31..........", 
                       from_="+31..........",
                       body = sms)

        
# Creating scenario for weather report in Fahrenheit        
elif result['success'] and degrees == "f": 
    result = result['response'] 
    
    temperature_fahrenheit = round(int(result['ob']['tempC']) * 1.8 + 32)
    feels_like_fahrenheit = round(int(result['ob']['feelslikeC']) * 1.8 + 32) #using the formula to compute Celsius to Fahrenheit
    
    lines = ("Temperature (F): " + str(temperature_fahrenheit), 
          "Humidity: " + str(result['ob']['humidity']) + " %",
          "Sky: " + str(result['ob']['weather']),
          "Feels like (F): " + str(feels_like_fahrenheit))
    print(" ")
    for line in lines: 
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
    code_rain = ["Rain", "Drizzle", "Rain showers", "Freezing drizzle", "Freezing rain", "Mostly Cloudy with Light Rain","Mostly Cloudy with Heavy Rain", "Mostly Cloudy with Drizzle", "Mostly Cloudy with Heavy Drizzle", "Cloudy with Drizzle","Cloudy with Heavy Drizzle", "Cloudy with Light Drizzle", "Mostly Cloudy with Light Drizzle", "Cloudy with Light Rain", "Cloudy with Heavy Rain"]
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
     
    if (str(result['ob']['weather']) not in code_clear) and (str(result['ob']['weather']) not in code_cloud) and (str(result['ob']['weather']) not in code_fog) and (str(result['ob']['weather']) not in code_rain) and (str(result['ob']['weather']) not in code_frost) and (str(result['ob']['weather']) not in code_snow) and (str(result['ob']['weather']) != "Hail") and (str(result['ob']['weather']) != "Thunderstorm"):
         print("The quote for this kind of weather is still in development :)")
       	

    from twilio.rest import Client # importing the Twilio Python helper library
			       # we used it to send SMS messages from Python
			       # this is an external library, which you need to install separately 
			       # for installation instructions please refer to README file  

    sms = str(lines) # this variable is our SMS message
		 # to keep SMS messages readable and to save some SMS traffic 
	 	 # our SMS messages only include weather conditions (without wisdom thought) 
	
# the following line needs your Twilio Account SID and Auth Token
# if you do not know where to find your Twilio Account SID and Auth Token please refer to README file 
    account_sid = "....." 
    auth_token = "....."   # replace the dots with the Account SID and Auth Token
    client = Client(account_sid, auth_token)
   
# change the "from_" number to your Twilio number and the "to" number
# to the phone number you signed up for Twilio (during the registration)
    client.messages.create(to="+31..........", 
                       from_="+31..........",
                       body = sms)
