def weather_prediction_static():
    T = 20  # Static temperature
    H = 80  # Static humidity
    ws = 10  # Static wind speed

    W = 0.5 * T**2 - 0.2 * H + 0.1 * ws - 15

    if W > 300:
        return "Sunny."
    elif 200 < W <= 300:
        return "Cloudy."
    elif 100 < W <= 200:
        return "Rainy."
    elif W <= 100:
        return "Stormy."

result = weather_prediction_static()
print("Weather prediction:", result)
