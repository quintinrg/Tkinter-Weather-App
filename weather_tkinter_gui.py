# On Github/quintinrg@gmail.com

import tkinter as tk
from tkinter import font
import requests

HEIGHT = 500
WIDTH = 600

def test_function(entry):
    print("This is the entry:", entry)


def get_weather(city):
    weather_key = '' #Please replace empty string with Open Weather Map key
    url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {'APPID': weather_key, 'q': city, 'units': 'Imperial'}
    response = requests.get(url, params = params)
    weather = response.json()

    label['text'] = format_response(weather)

def format_response(weather):
    try:
        name = weather['name']
        desc = weather['weather'][0]['description']
        temp = weather['main']['temp']

        final_str = 'City: %s \n Conditions: %s \n Temperature (°F): %s' %(name, desc, temp)
    
    except:
        final_str = 'There was a problem retrieving that information'
    
    return final_str

root = tk.Tk()

canvas = tk.Canvas(root, height = HEIGHT, width = WIDTH)
canvas.pack()

background_image = tk.PhotoImage(file = 'image.png')
background_label = tk.Label(root, image = background_image)
background_label.place(relwidth = 1, relheight = 1)

frame = tk.Frame(root, bg = '#60c1aa', bd = 5)
frame.place(relx = 0.5, rely = 0.1, relwidth = 0.75, relheight = 0.1, anchor = 'n')

entry = tk.Entry(frame, font = ('Courier', 16))
entry.place(relwidth = 0.65, relheight = 1)

button = tk.Button(frame, text = "Get Weather", bg = '#80c1df', font = ('Courier', 12), command = lambda: get_weather(entry.get()))
button.place(relx = 0.7, relheight = 1, relwidth = 0.3)

lower_frame = tk.Frame(root, bg = '#60c1aa', bd = 10)
lower_frame.place(relx = 0.5, rely = 0.25, relwidth = 0.75, relheight = 0.6, anchor = 'n')

label = tk.Label(lower_frame, font = ('Courier', 18))
label.place(relwidth = 1, relheight = 1)

root.mainloop()

  