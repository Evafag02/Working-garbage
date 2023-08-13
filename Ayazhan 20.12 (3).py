from tkinter import *
from tkinter import ttk
import requests

FR_US = ["Marseille, FR", "Paris, FR", "Lyon, FR", "Tours, FR", "Nice, FR", "Nantes, FR", "Strasburg, FR", "Lille, FR", "Reims, FR", "Toulon, FR", "Grenoble, FR", "Brooklyn, US","Camden, US", "Canton, US", "Clinton, US","Houston, US", "Erie, US", "Chicago, US", "Roanoke, US", "Utica, US"]
output = []
appid = "89e2a955771344704f98b1b74551b10d"
city = 0
for j in FR_US:
        res = requests.get("http://api.openweathermap.org/data/2.5/find",
                    params={'q': j, 'type': 'like', 'units': 'metric', 'APPID': appid})
        frus = res.json()
        sunny = frus['list'][0]['weather'][0]['main']
        tmpr = frus['list'][0]['main']['temp']
        city += 1
        city_name = 'city: ' + str(j)
        output.append(city_name)
        temp_city = "temperature in the city: " + str(tmpr)
        output.append(temp_city)
        output.append("now is sunny")
        output.append("")

Cities_B = 'Cities: ' + str(city)
output.append(Cities_B)

root = Tk()
root.title("3")
root.geometry("250x200")

languages_var = StringVar(value=output)
listbox = Listbox(listvariable=languages_var)
listbox.pack(side=LEFT, fill=BOTH, expand=1)

scrollbar = ttk.Scrollbar(orient="vertical", command=listbox.yview)
scrollbar.pack(side=RIGHT, fill=Y)

listbox["yscrollcommand"] = scrollbar.set

root.mainloop()