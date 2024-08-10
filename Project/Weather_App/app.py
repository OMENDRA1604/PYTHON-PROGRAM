from flask import Flask, render_template, request
import requests
import json
import pyttsx3

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def weather():
    if request.method == 'POST':
        city = request.form['city']
        url = f"https://api.weatherapi.com/v1/current.json?key=f183438c68b4403f91d53731242502&q={city}"
        r = requests.get(url)
        wdic = json.loads(r.text)
        temperature = wdic["current"]["temp_c"]
        condition = wdic["current"]["condition"]["text"].lower()

        if "sunny" in condition:
            background_image = 'sunny.jpeg'
        elif "cloud" in condition:
            background_image = 'cloudy.jpeg'
        elif "rain" in condition:
            background_image = 'rainy.jpeg'
        else:
            background_image = 'default.jpeg'

        engine = pyttsx3.init()
        engine.say(f"The current weather in {city} is {temperature} degrees with {condition}")
        engine.runAndWait()

        return render_template('result.html', city=city, temperature=temperature, condition=condition, background_image=background_image)
    
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
