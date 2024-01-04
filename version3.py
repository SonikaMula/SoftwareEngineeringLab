def weather_prediction_from_file(filename):
    with open('weather.txt', 'r') as file:
        T, H, ws = map(float, file.readline().split(','))

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
result = weather_prediction_from_file('weather.txt')
print("Weather prediction:", result)
