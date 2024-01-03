def weather_prediction_user_defined(T, H, ws):
    W = 0.5 * T**2 - 0.2 * H + 0.1 * ws - 15

    if W > 300:
        return "Sunny."
    elif 200 < W <= 300:
        return "Cloudy."
    elif 100 < W <= 200:
        return "Rainy."
    elif W <= 100:
        return "Stormy."

# Example usage:
temperature = float(input("Enter temperature: "))
humidity = float(input("Enter humidity: "))
wind_speed = float(input("Enter wind speed: "))

result = weather_prediction_user_defined(temperature, humidity, wind_speed)
print("Weather prediction:", result)
