def weather_prediction(T, H, ws):
    W = 0.5 * T**2 - 0.2 * H + 0.1 * ws - 15

    if W > 300:
        return "Sunny."
    elif 200 < W <= 300:
        return "Cloudy."
    elif 100 < W <= 200:
        return "Rainy."
    elif W <= 100:
        return "Stormy."

# Get user input for the number of sets
n = int(input("Enter the number of input sets: "))

# Get predictions for each set
for i in range(n):
    t = int(input(f"Enter temperature for set {i + 1}: "))
    h = int(input(f"Enter humidity for set {i + 1}: "))
    ws = int(input(f"Enter wind speed for set {i + 1}: "))

    result = weather_prediction(t, h, ws)
    print(f"Weather prediction for set {i + 1}: {result}")
