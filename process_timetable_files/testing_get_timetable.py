from insert_update_group_timetable import get_group_timetable
group = 'Б05-878'
import pickle
#print (get_group_timetable(group))
with open('TimetableDB.pickle', 'rb') as f:
    TimetableDB = pickle.load(f)
print(TimetableDB)