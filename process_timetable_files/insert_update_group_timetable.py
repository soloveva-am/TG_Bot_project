#from pathlib import Path
#import sys
TimetableDB = {'group': {False: 'group_timetable', True:'exam_timetable'}}
import pickle
import os.path
if not os.path.exists('TimetableDB.pickle'):
    with open('TimetableDB.pickle', 'wb') as f:
        pickle.dump(TimetableDB, f, pickle.HIGHEST_PROTOCOL)
else:
    with open('TimetableDB.pickle', 'rb') as f:
        TimetableDB = pickle.load(f)

#sys.path.append(str(Path(__file__).parent.parent.parent.parent))

#from database_queries.sync_queries import insert_group, update_group

import time


def insert_update_group_timetable(group_name: str, timetable: dict, exam=False):
    with open('TimetableDB.pickle', 'rb') as f:
        TimetableDB = pickle.load(f)
    if group_name in TimetableDB.keys():
        TimetableDB[group_name][exam]=timetable
    else: TimetableDB[group_name]={exam:timetable, not exam: None}
    with open('check_timetable.txt', 'a') as logfile:
        print('/n/n/n', file=logfile)
        for group in TimetableDB.keys():
            if group != 'group':
                for exam in [False, True]:
                    print(group, file=logfile)
                    if TimetableDB[group][exam]==None: print('N/A', file=logfile)
                    else: print(*TimetableDB[group][exam], file=logfile)
    with open('TimetableDB.pickle', 'wb') as f:
        pickle.dump(TimetableDB, f, pickle.HIGHEST_PROTOCOL)

def get_group_timetable(group_name, exam=False):
    with open('TimetableDB.pickle', 'rb') as f:
        TimetableDB = pickle.load(f)
    if group_name in TimetableDB.keys():
        return TimetableDB[group_name][exam]
    else: raise NameError
