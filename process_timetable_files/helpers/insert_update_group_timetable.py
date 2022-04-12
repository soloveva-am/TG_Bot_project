from pathlib import Path
import sys


#sys.path.append(str(Path(__file__).parent.parent.parent.parent))

#from database_queries.sync_queries import insert_group, update_group

import time
TimetableDB = {'group': {False: 'group_timetable', True:'exam_timetable'}}

#TODO: починить. пока не работает
def insert_update_group_timetable(group_name: str, timetable: dict, exam=False):
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
