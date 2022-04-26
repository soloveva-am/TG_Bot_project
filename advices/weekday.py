dict_day = {'0':'Воскресенье','1':'Понедельник','2':'Вторник','3':'Среда','4':'Четверг','5':'Пятница','6':'Суббота','7':'Воскресенье'}
def WEEKDAY(my_day):
    day = int(my_day[8:])
    month = int(my_day[5:7])
    year = int(my_day[:4])
    n = (day+2*month+(3*(month+1))//5+year+(year//4))%7
    return dict_day[str(n)]




def convert_time(hour):
    # min = int(hour[:2])*60+int(hour[3:])
    b = hour.split(':')
    b1 = b[0].strip()
    b2 = b[1].strip()
    min = int(b1)*60 + int(b2)
    return min

# print(convert_time('10:25'))
