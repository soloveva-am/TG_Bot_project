def get_group_timetable(group_name, exam=False):
    with open('process_timetable_files.TimetableDB.pickle', 'rb') as f:
        TimetableDB = pickle.load(f)
    if group_name in TimetableDB.keys():
        return TimetableDB[group_name][exam]
    else: raise NameError

def get_all_timetable():
    with open('process_timetable_files.TimetableDB.pickle', 'rb') as f:
        TimetableDB = pickle.load(f)
    return TimetableDB
