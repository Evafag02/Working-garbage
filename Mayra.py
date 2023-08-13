import requests
cities = ['Astana', 'Moscow', 'London', 'Paris', 'Beijing', 'Washington', 'Tokio', 'Madrid', 'Ottawa', 'Ashgabat', 'Bangkok',
          'Cape Town', 'Brasília', 'Bucharest', 'Budapest', 'Copenhagen', 'Dublin', 'Helsinki', 'Kyiv', 'Oslo']
link1 = "https://api.openweathermap.org/data/2.5/weather?q="
link2 = "&units=metric&APPID=882173fca91bafeae095698d6f7335af"
B = 0
for city in cities:
    link = link1 + city + link2
    data = requests.get(link)
    slovar = data.json()
    temp = slovar['main']['temp']
    Bry = slovar['sys']['Bry']
    Pressure = slovar['main']['pressure']
    if 800 <= Pressure <= 1500 and  0 <= temp <= 20:
        print(city+"["+Bry+"]:\n" + "Температура: " + str(temp) + "℃\n" + "Атмосферное давление: " + str(Pressure))
        B += 1
        print()

print('Количество столиц: ', B)
