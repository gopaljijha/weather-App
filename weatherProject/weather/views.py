from django.shortcuts import render, redirect
from weather.key import api_key
import requests
from geopy.geocoders import Nominatim
import math
import calendar
import datetime
from datetime import date, timedelta, datetime, tzinfo
# from datetime import 
# from dateutil import tz, parser
# import pytz

# Create your views here.

def home(request):
    return render(request, "weather/home.html")


def weatherResult(request):
    if request.method == "POST":
        city_name = request.POST["city"].lower()
        # Initialize Nominatim API
        geolocator = Nominatim(user_agent="MyApp")
        location = geolocator.geocode(city_name)

        # url = f"http://api.openweathermap.org/data/2.5/forecast?q={city_name}&appid={api_key}"
        source = f"http://api.openweathermap.org/data/2.5/forecast?q={city_name}&appid={api_key}"
        
        url = f'https://api.openweathermap.org/data/2.5/weather?lat={location.latitude}&lon={location.longitude}&appid={api_key}'
 
        w_dataset = requests.get(source).json()
        response = requests.get(url).json()

        # getting the current time
        current_time_data = datetime.now()
#             # formatting the time using directives, it will take this format Day, Month Date Year, Current Time 
        # formatted_time = current_time_data.strftime("%A, %B %d %Y, %H:%M:%S %p")

        # convert int to string 
        # dStr = w_dataset['list'][0]["dt"].__str__()
        # print(type(dStr), w_dataset['list'][0]["dt"], dStr)
        currentTime = datetime.fromtimestamp(int(w_dataset['list'][0]["dt"].__str__()[:10])).strftime("%A, %B %d %Y, %H:%M:%S %p")
        #print(type(currentTime),currentTime)

        
        
        ThreeHourLaterTime = datetime.fromtimestamp(int(w_dataset['list'][1]["dt"].__str__()[:10])).strftime("%A, %B %d %Y, %H:%M:%S %p")
        SixHourLaterTime = datetime.fromtimestamp(int(w_dataset['list'][2]["dt"].__str__()[:10])).strftime("%A, %B %d %Y, %H:%M:%S %p")
        NineHourLaterTime = datetime.fromtimestamp(int(w_dataset['list'][3]["dt"].__str__()[:10])).strftime("%A, %B %d %Y, %H:%M:%S %p")
        TwelveHourLaterTime = datetime.fromtimestamp(int(w_dataset['list'][4]["dt"].__str__()[:10])).strftime("%A, %B %d %Y, %H:%M:%S %p")
        FifteenHourLaterTime = datetime.fromtimestamp(int(w_dataset['list'][5]["dt"].__str__()[:10])).strftime("%A, %B %d %Y, %H:%M:%S %p")
        EighteenHourLaterTime = datetime.fromtimestamp(int(w_dataset['list'][6]["dt"].__str__()[:10])).strftime("%A, %B %d %Y, %H:%M:%S %p")
        TwentyOneHourLaterTime = datetime.fromtimestamp(int(w_dataset['list'][7]["dt"].__str__()[:10])).strftime("%A, %B %d %Y, %H:%M:%S %p")
        TwentyFourHourLaterTime = datetime.fromtimestamp(int(w_dataset['list'][8]["dt"].__str__()[:10])).strftime("%A, %B %d %Y, %H:%M:%S %p")

        print("LiveCloud ", response["clouds"]["all"])
        print("liveIcon ", response["weather"][0]["icon"])

        print("icon ",w_dataset["list"][0]["weather"][0]["icon"])
        
        
        try:
            context = {
                ####
                'live_time': currentTime,
                'city': city_name,
                'country' : response["sys"]["country"],
                'live_weather': response["weather"][0]["main"],
                'live_temp': math.floor(response["main"]["temp"] -273.0),
                'liveTemperature_min': math.floor(response["main"]["temp_min"] -273.0),
                'liveTemperature_max': math.floor(response["main"]["temp_max"] -273.0),
                'liveIcon': response["weather"][0]["icon"],
                'liveHumidity': response["main"]["humidity"],
                'liveWind': response["wind"]["speed"],
                'liveClouds': response["clouds"]["all"],
                'liveCloudsIcon' : "03d",


                "city_name":w_dataset["city"]["name"],
                "city_country":w_dataset["city"]["country"],
                "degree":w_dataset['list'][0]['wind']['deg'],
                "status":w_dataset['list'][0]['weather'][0]['description'],
                
                # 'date':w_dataset['list'][0]["dt_txt"],
                'currentTime': currentTime,
                
                'date1':w_dataset['list'][1]["dt_txt"],
                'next_threeHour':ThreeHourLaterTime,

                'date2':w_dataset['list'][2]["dt_txt"],
                'next_sixHour': SixHourLaterTime,

                'date3':w_dataset['list'][3]["dt_txt"],
                'next_nineHour' : NineHourLaterTime,

                'date4':w_dataset['list'][4]["dt_txt"],
                'next_twelveHour':TwelveHourLaterTime,

                'date5':w_dataset['list'][5]["dt_txt"],
                'next_fifteenHour':FifteenHourLaterTime,

                'date6':w_dataset['list'][6]["dt_txt"],
                'next_eighteenHour':EighteenHourLaterTime,

                'date7':w_dataset['list'][7]["dt_txt"],
                'next_twentyOneHour':TwentyOneHourLaterTime,

                'date8':w_dataset['list'][8]["dt_txt"],
                'next_twenrtFourHour':TwentyFourHourLaterTime,

                "temp": round(w_dataset["list"][0]["main"]["temp"] -273.0),
                "temp_min1":math.floor(w_dataset["list"][1]["main"]["temp_min"] -273.0),
                "temp_max1": math.ceil(w_dataset["list"][1]["main"]["temp_max"] -273.0),
                "temp_min2":math.floor(w_dataset["list"][2]["main"]["temp_min"] -273.0),
                "temp_max2": math.ceil(w_dataset["list"][2]["main"]["temp_max"] -273.0),
                "temp_min3":math.floor(w_dataset["list"][3]["main"]["temp_min"] -273.0),
                "temp_max3": math.ceil(w_dataset["list"][3]["main"]["temp_max"] -273.0),
                "temp_min4":math.floor(w_dataset["list"][4]["main"]["temp_min"] -273.0),
                "temp_max4": math.ceil(w_dataset["list"][4]["main"]["temp_max"] -273.0),
                "temp_min5":math.floor(w_dataset["list"][5]["main"]["temp_min"] -273.0),
                "temp_max5": math.ceil(w_dataset["list"][5]["main"]["temp_max"] -273.0),
                "temp_min6":math.floor(w_dataset["list"][6]["main"]["temp_min"] -273.0),
                "temp_max6": math.ceil(w_dataset["list"][6]["main"]["temp_max"] -273.0),
                "temp_min7":math.floor(w_dataset["list"][7]["main"]["temp_min"] -273.0),
                "temp_max7": math.ceil(w_dataset["list"][7]["main"]["temp_max"] -273.0),
                "temp_min8":math.floor(w_dataset["list"][8]["main"]["temp_min"] -273.0),
                "temp_max8": math.ceil(w_dataset["list"][8]["main"]["temp_max"] -273.0),


                
                "pressure":w_dataset["list"][0]["main"]["pressure"],
                "humidity":w_dataset["list"][0]["main"]["humidity"],
                "sea_level":w_dataset["list"][0]["main"]["sea_level"],

                
                "weather":w_dataset["list"][1]["weather"][0]["main"],
                "description":w_dataset["list"][1]["weather"][0]["description"],

                "main1":w_dataset["list"][0]["weather"][0]["main"],
                "main2":w_dataset["list"][1]["weather"][0]["main"],
                "main3":w_dataset["list"][2]["weather"][0]["main"],
                "main4":w_dataset["list"][3]["weather"][0]["main"],
                "main5":w_dataset["list"][4]["weather"][0]["main"],
                "main6":w_dataset["list"][5]["weather"][0]["main"],
                "main7":w_dataset["list"][6]["weather"][0]["main"],

                "icon1":w_dataset["list"][0]["weather"][0]["icon"],
                "icon2":w_dataset["list"][1]["weather"][0]["icon"],
                "icon3":w_dataset["list"][2]["weather"][0]["icon"],
                "icon4":w_dataset["list"][3]["weather"][0]["icon"],
                "icon5":w_dataset["list"][4]["weather"][0]["icon"],
                "icon6":w_dataset["list"][5]["weather"][0]["icon"],
                "icon7":w_dataset["list"][6]["weather"][0]["icon"],
                "icon8":w_dataset["list"][7]["weather"][0]["icon"],

                "cloud":w_dataset['list'][0]['clouds']['all'],
                "cloud1":w_dataset['list'][1]['clouds']['all'],
                "cloud2":w_dataset['list'][2]['clouds']['all'],
                "cloud3":w_dataset['list'][3]['clouds']['all'],
                "cloud4":w_dataset['list'][4]['clouds']['all'],
                "cloud5":w_dataset['list'][5]['clouds']['all'],
                "cloud6":w_dataset['list'][6]['clouds']['all'],
                "cloud7":w_dataset['list'][7]['clouds']['all'],
                "cloud8":w_dataset['list'][8]['clouds']['all'],

                "wind0":w_dataset['list'][0]['wind']['speed'],
                "wind1":w_dataset['list'][1]['wind']['speed'],
                "wind2":w_dataset['list'][2]['wind']['speed'],
                "wind3":w_dataset['list'][3]['wind']['speed'],
                "wind4":w_dataset['list'][4]['wind']['speed'],
                "wind5":w_dataset['list'][5]['wind']['speed'],
                "wind6":w_dataset['list'][6]['wind']['speed'],
                "wind7":w_dataset['list'][7]['wind']['speed'],
                "wind8":w_dataset['list'][8]['wind']['speed'],

            }

            

        except:
            context = {

            "city_name":"Not Found, Check your spelling..."
        }

        return render(request, "weather/weatherResult.html", context)
    else:
    	 return render(request, "weather/home.html")



