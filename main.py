import requests
import json
import pyttsx3
city=input("enter city name\n")
url=f"https://api.weatherapi.com/v1/current.json?key=2efa61a8bac24f6e96e82300231109&q={city}"
r=requests.get(url)
wdetails = json.loads(r.text)
w=(wdetails["current"]["temp_c"])
import pyttsx3
text_speech=pyttsx3.init()
text_speech.say(f"the current weather in {city} is {w} degree")
text_speech.runAndWait()