#A simple Python utility to upload grade information to simple note in real time
#Author: Eden Zik

from simplenote import Simplenote
import os
from sage import get_grades
import time
from datetime import datetime


EMAIL = os.environ['SIMPLENOTE_EMAIL']         #Simplenote email
PASSWORD = os.environ['SIMPLENOTE_PASSWORD']          #Simplenote password
NOTE_NAME = os.environ['SIMPLENOTE_GRADE_NOTE_NAME'] #Simplenote note name
REFRESH_TIME = 300 #time between waits to fetch grades (seconds)

def grades_note_setup():
    simplenote = Simplenote(EMAIL,PASSWORD)
    return simplenote.add_note(NOTE_NAME)[0]['key']

def grades_note_update(note_id):
    simplenote = Simplenote(EMAIL,PASSWORD)
    grades = simplenote.get_note(note_id)[0]
    grades['content'] = NOTE_NAME + "\n" + get_grades() + "Last updated: " + str(datetime.now())
    simplenote.update_note(grades)

if __name__ == '__main__':
    note_id = grades_note_setup()
    while True:
        grades_note_update(note_id)
        time.sleep(REFRESH_TIME)

