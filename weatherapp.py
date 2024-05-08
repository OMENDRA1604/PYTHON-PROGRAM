import requests
import json
import pyttsx3

city = input("Enter the name of the city:\n ")

url = f"https://api.weatherapi.com/v1/current.json?key=f183438c68b4403f91d53731242502&q={city}"

r = requests.get(url)
# print(r.text)
wdic = json.loads(r.text)
w = wdic["current"]["temp_c"]
print(w)
if __name__ == '__main__':
    engine = pyttsx3.init()
    engine.say(f"The current weather in {city} is {w} degrees")
    engine.runAndWait()
