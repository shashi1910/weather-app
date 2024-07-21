def convert_temperature(kelvin, unit='Celsius'):
    if unit == 'Celsius':
        return kelvin - 273.15
    elif unit == 'Fahrenheit':
        return (kelvin - 273.15) * 9/5 + 32
    return kelvin

def format_weather_data(data, units='metric'):
    temp = convert_temperature(data['main']['temp'], 'Celsius' if units == 'metric' else 'Fahrenheit')
    weather = data['weather'][0]['description']
    return f"Temperature: {temp:.2f}°, Weather: {weather.capitalize()}"
