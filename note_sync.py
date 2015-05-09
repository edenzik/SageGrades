#A simple Python utility to upload grade information to simple note in real time
#Author: Eden Zik

from simplenote import Simplenote
from datetime import datetime
from sage import get_grades


EMAIL = '???@???.com'         #Simplenote email
PASSWORD = '???????'          #Simplenote password

simplenote = Simplenote(EMAIL,PASSWORD)

GRADES_NOTE_ID = 'bf634100f62811e4a205db0538ecac0d'  #Note ID of Grades Note

grades = simplenote.get_note(GRADES_NOTE_ID)[0]

grades['content'] = "Grades\n" + get_grades() + "Last updated: " + str(datetime.now())

simplenote.update_note(grades)
