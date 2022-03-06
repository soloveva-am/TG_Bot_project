import requests

url = 'http://wttr.in/dolgoprudny?format=j1'
response = requests.get (url)  # выполните HTTP-запрос
data = response.json()

data_presently = data["current_condition"]
time_presently = data_presently[0]["localObsDateTime"]
temp_presently = data_presently[0]["temp_C"]
temp_fell_presently = data_presently[0]["FeelsLikeC"]
weather_desc_presently = data_presently[0]["weatherDesc"][0]["value"]

xoviet = ""
if int(temp_fell_presently) < -10:
    xoviet = "Я рекомендую вам одеваться теплее, когда выходите на улицу"
if "rain" in weather_desc_presently:
    xoviet = "Я рекомендую вам взять с собой зонт"

content_presently = f"{time_presently}:\n температура: {temp_presently}°C \n воспринимаемая температура: {temp_fell_presently}°C \n описание погоды: {weather_desc_presently}.\n {xoviet}"

print(content_presently)

weather = data["weather"]

weather_today = weather[0]
weather_tomorrow = weather[1]
weather_after_tomorrow = weather[2]

avg_temp_0 = weather_today["avgtempC"]
avg_temp_1 = weather_tomorrow["avgtempC"]
avg_temp_2 = weather_after_tomorrow["avgtempC"]

temp_0 = []
temp_1 = []
temp_2 = []

temp_feel_0 = []
temp_feel_1 = []
temp_feel_2 = []

chanceof_rain_0 = []
chanceof_rain_1 = []
chanceof_rain_2 = []

chanceof_snow_0 = []
chanceof_snow_1 = []
chanceof_snow_2 = []

chanceof_sunshine_0 = []
chanceof_sunshine_1 = []
chanceof_sunshine_2 = []

weather_desc_0 = []
weather_desc_1 = []
weather_desc_2 = []

for hourly in weather_today["hourly"]:
    temp_0.append(hourly["tempC"])
    temp_feel_0.append(hourly["FeelsLikeC"])
    chanceof_rain_0.append(hourly["chanceofrain"])
    chanceof_snow_0.append(hourly["chanceofsnow"])
    weather_desc_0.append(hourly["weatherDesc"][0]["value"])

for hourly in weather_tomorrow["hourly"]:
    temp_1.append(hourly["tempC"])
    temp_feel_1.append(hourly["FeelsLikeC"])
    chanceof_rain_1.append(hourly["chanceofrain"])
    chanceof_snow_1.append(hourly["chanceofsnow"])
    chanceof_snow_1.append(hourly["chanceofsnow"])
    weather_desc_1.append(hourly["weatherDesc"][0]["value"])

for hourly in weather_after_tomorrow["hourly"]:
    temp_2.append(hourly["tempC"])
    temp_feel_2.append(hourly["FeelsLikeC"])
    chanceof_rain_2.append(hourly["chanceofrain"])
    chanceof_snow_2.append(hourly["chanceofsnow"])
    chanceof_snow_2.append(hourly["chanceofsnow"])
    weather_desc_2.append(hourly["weatherDesc"][0]["value"])


day_0 = [[] for _ in range(8)]
day_1 = [[] for _ in range(8)]
day_2 = [[] for _ in range(8)]
days = [day_0,day_1,day_2]

for day in range(3):
    for inter in range(8):
        days[day][inter].append(weather[day]["hourly"][inter]["tempC"])
        days[day][inter].append(weather[day]["hourly"][inter]["chanceofrain"])
        days[day][inter].append(weather[day]["hourly"][inter]["chanceofsunshine"])



