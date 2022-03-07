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
date_0 = weather_today["date"]

day_1 = [[] for _ in range(8)]
date_1 = weather_tomorrow["date"]

day_2 = [[] for _ in range(8)]
date_2 = weather_after_tomorrow["date"]

days = {date_0: day_0,date_1:day_1,date_2:day_2}

for ind,day in enumerate(days):
    for inter in range(8):
        days[day][inter].append(weather[ind]["hourly"][inter]["tempC"])
        days[day][inter].append(weather[ind]["hourly"][inter]["chanceofrain"])
        days[day][inter].append(weather[ind]["hourly"][inter]["chanceofsunshine"])

# print(days)


def ISRAINING(date,time):
    try:
        hour = int(time[0:2])
        min = int(time[3:])
        rain = None
        if min > 30:
            hour += 1
        ind_hour = hour // 3
        percent_rain = int(days[date][ind_hour][1])
        if percent_rain < 40:
            rain = False
        else:
            rain = True
    except ValueError:
        rain = "Вы ввели недопустимые символы."
    except IndexError:
        rain = "Вы ввели недопустимые символы."
    return rain



def RECOMENDATIONS(date,time):
    try:
        hour = int(time[0:2])
        min = int(time[3:])
        if min > 30:
            hour += 1
        ind_hour = hour // 3
        temp = int(days[date][ind_hour][0])
        comment = ""
        if ISRAINING(date,time) == False:
            if int(temp) > -5 :
                comment = "Иди гулять!!!"
        else:
            comment = "Возьми зонт!!!"

    except ValueError:
        comment = "Вы ввели недопустимые символы."
    except IndexError:
        comment = "Вы ввели недопустимые символы."
    return comment

date = input("date:")
time = input("time:")
print(ISRAINING(date,time))
print(RECOMENDATIONS(date,time))


