#Sets up initial "grades" note. Paste the note ID returned by this method into the note_sync file.
#Author: Eden Zik

from simplenote import Simplenote


EMAIL = '???@???.com'         #Simplenote email
PASSWORD = '??????'          #Simplenote password

def grades_note_setup:
    simplenote = Simplenote(EMAIL,PASSWORD)
    simplenote.add_note("Grades")

if __name__ == '__main__':
    print grades_note_setup()

