from process_timetable_files.insert_update_group_timetable import get_group_timetable, get_all_timetable
from advices.katok import *
from advices.weath import *
from advices.weekday import *

time = {'09:00 – 10:25':0,'10:45 – 12:10':1,'12:20 – 13:45':2,'13:55 – 15:20':3,'15:30 – 16:55':4,'17:05 – 18:30':5,'18:35 – 20:00':6}
def STUDY_DAY(day,group):
    time_day = get_group_timetable(group)[day]
    rest_time = []
    study_time = []
    for keys in time_day:
        values = time_day[keys]
        if values == "😴":
            rest_time.append(keys)
        else:
            study_time.append(keys)
    return rest_time,study_time,time_day

def WATCH_STUDY(date,group):
    day = WEEKDAY(date)
    return STUDY_DAY(day,group)

def ADVICES(date,group):

    rest_time,study_time,time_day = WATCH_STUDY(date,group)
    number_rest = []
    if len(rest_time) ==7:
        return time_day
    for x in study_time:
        if ISRAINING(date,x[:5]) == True:
            time_day['Advice'] = 'Возьми зонт!'
            break
    for x in rest_time:
        number_rest.append(time[x])

    for x in number_rest:
        if x >= 2 and x <= 4:
            if number_rest[number_rest.index(x):] != list(range(number_rest.index(x),7)):
                time_day[list(time.keys())[x]] = "иди обедать!"
                number_rest.remove(x)
            break
    for x in number_rest:
        if x <= 5 and ISRAINING(date,list(time_day.keys())[x][:5]) == False:
            time_day[list(time.keys())[x]] = "иди гулять!"

    return time_day


def SKATING(group):
    advice_skat = {}
    my_ckating = dict_skating(list_skat)
    new_dict = {}
    for key in my_ckating:
        day = key.split('-')[1]
        day = day.replace(' ','').title()
        new_dict[day] = my_ckating[key]

    for day in new_dict:
        x,y = new_dict[day].split('-')
        x,y = convert_time(x),convert_time(y)
        if x >= 1200:# чтобы после 20:00 мы могли идтй кататься в любое время
            advice_skat[day] = 'Ты можешь идтй кататься в {}!'.format(new_dict[day])
            continue
        rest_time,study_time,time_day = STUDY_DAY(day,group)
        res = True
        for i in study_time:
            a,b = i.split('-')
            a,b = convert_time(a),convert_time(b)
            if a <= x <= b or a <= y <= b:
                res = False
                break
        if res == True:
            advice_skat[day] = 'Ты можешь идтй кататься в {}!'.format(new_dict[day])

    return advice_skat



print(ADVICES('2022-04-22','Б03-007'))
print(SKATING('Б03-007'))





