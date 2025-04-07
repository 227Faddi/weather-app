from flask import Flask, render_template, request
from weather import get_current_weather
from waitress import serve


app = Flask(__name__)
port = 8000

@app.route('/')

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/weather')
def get_weather():
    city = request.args.get('city')

    if not bool(city.strip()):
        city = 'Montreal'

    weather_data = get_current_weather(city)

    if not weather_data['cod'] == 200:
        return render_template(
            'notfound.html',
            city=city
        )

    return render_template(
        'weather.html',
        title = weather_data['name'],
        status = weather_data['weather'][0]['description'].capitalize(),
        temp = f'{weather_data['main']['temp']:.1f}',
        feels_like = f'{weather_data['main']['feels_like']:.1f}',
    )
        


if __name__ == '__main__':
    print(f'Server live on port: {port}')
    serve(app, host='0.0.0.0', port=port)