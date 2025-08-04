from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_KEY = "2de8a2ec38d18fced53ee5c2fea235a8"  # Replace with your API key

@app.route("/", methods=["GET", "POST"])
def index():
    weather = None
    error = None

    if request.method == "POST":
        city = request.form["city"]
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            weather = {
                "city": city.title(),
                "temperature": data["main"]["temp"],
                "description": data["weather"][0]["description"].capitalize(),
                "icon": f"http://openweathermap.org/img/wn/{data['weather'][0]['icon']}@2x.png"
            }
        else:
            error = "City not found. Please try again."

    return render_template("index.html", weather=weather, error=error)

if __name__ == "__main__":
    app.run(debug=True)
