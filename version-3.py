def weather_prediction_from_file(filename):
    try:
        with open(r'C:\Users\user\Desktop\SONIKA\vs py\SE\wd.txt', 'r') as file:
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

    except FileNotFoundError:
        return "Error: File not found."
    except Exception as e:
        return f"Error: {str(e)}"

# Example usage:
result = weather_prediction_from_file('wd.txt')
print("Weather prediction:", result)
