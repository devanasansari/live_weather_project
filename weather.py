import requests
from datetime import datetime

api_key = 'e0fe3923ac5588b9bde88ab707fb82a2'
location = input("Enter your city name: ")
api_link = requests.get("https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+api_key)
api_data = api_link.json()

temp_city = ((api_data['main']['temp']) - 273.15)
weather_desc = api_data['weather'][0]['description']
hmdt = api_data['main']['humidity']
wind_spd = api_data['wind']['speed']
date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")

print ("Weather Stats for  {}  || {}".format(location.upper(), date_time))
print ("Temperature is: {:.2f} deg C".format(temp_city))
print ("weather desc  :",weather_desc)
print ("Humidity      :",hmdt, '%')
print ("wind speed    :",wind_spd ,'kmph')

a = ("Weather Stats for  {}  || {}".format(location.upper(), date_time))
b = ("Temperature is: {:.2f} deg C".format(temp_city))
c = ("weather desc  :" + str(weather_desc))
d = ("Humidity      :" + str(hmdt) + '%')
e = ("wind speed    :" + str(wind_spd) + 'kmph')



report = [a, b, c, d, e]
f = open ('recent_report.txt','w')
for line in report:
    f.write(line +'\n')
f.close()


    
