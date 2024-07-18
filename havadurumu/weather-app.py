import tkinter as tk
from tkinter import messagebox
import requests

def get_weather(city):
    api_key = "a7b1712d001dce02b489742bdfe6ff3c"  # Add your OpenWeatherMap API key here
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {"q": city, "appid": api_key, "units": "metric"}
    
    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        weather_data = response.json()
        
        if weather_data["cod"] == 200:
            city_name = weather_data["name"]
            temp = weather_data["main"]["temp"]
            description = weather_data["weather"][0]["description"]
            return f"{city_name} - Temperature: {temp}°C\nWeather: {description.capitalize()}"
        else:
            return "City not found!"
    except requests.exceptions.RequestException as e:
        return f"Error: {e}"

def show_weather():
    city = city_entry.get()
    if city:
        weather = get_weather(city)
        weather_label.config(text=weather)
    else:
        messagebox.showwarning("Warning", "Please enter a city name!")

# Create the main window
root = tk.Tk()
root.title("Weather Application")

# City entry
city_label = tk.Label(root, text="City:")
city_label.pack(pady=5)

city_entry = tk.Entry(root)
city_entry.pack(pady=5)

# Show weather button
get_weather_button = tk.Button(root, text="Show Weather", command=show_weather)
get_weather_button.pack(pady=5)

# Weather label
weather_label = tk.Label(root, text="", font=("Helvetica", 12))
weather_label.pack(pady=10)

# Main loop
root.mainloop()
