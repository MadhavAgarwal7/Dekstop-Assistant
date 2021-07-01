import requests, json 
import David
api_key = "b73770542be8e14c0c9fb12173dd6198"

def weather():
        David.speak("Enter City")
        city_name=David.takecommand()
        complete_url="http://api.openweathermap.org/data/2.5/weather?q="+city_name+"&APPID="+api_key
        response=requests.get(complete_url)
        x=response.json()
        if x['cod'] != '404':
                y=x["main"]
                z=x["weather"]
                current_temperature = y["temp"]
                current_humidity = y["humidity"]
                weather_description = z[0]["description"]
                David.speak("there is "+weather_description+" in "+city_name)
                David.speak("the average temprature is "+str(int(current_temperature-273.15))+" degree celsius")
                David.speak("the humidity is "+str(current_humidity)+" per cent")
        else:
                David.speak("City not found!!!!")