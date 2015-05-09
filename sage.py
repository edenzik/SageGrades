#A simple python utility to extract grades out of Brandeis Sage
#Author: Eden Zik

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

BRANDEIS_ID = '????' #Your Brandeis username (keep safe!)
BRANDEIS_PASSWORD = '?????'     #Your Brandeis password (keep safe!)
SEMESTER = 1                            #Semester count from the most recent (0th semester is the most recent one after registration, 1st is the one before that, etc.)
SPEED_CONSTANT = 5                      #Number of seconds to wait for page redirection

def get_grades():
    #Setup

    browser = webdriver.Firefox()

    #Sage Login Page

    browser.get('https://www.brandeis.edu/sage/')

    #Acquiring Signin Elements

    userid = browser.find_element_by_id('userid')

    pwd = browser.find_element_by_id('pwd')

    #Signing In

    userid.send_keys(BRANDEIS_ID)

    pwd.send_keys(BRANDEIS_PASSWORD + Keys.RETURN)

    #Waiting for SAGE to load

    time.sleep(SPEED_CONSTANT)

    #Getting "class schedule" element

    try:

        schdl = browser.find_element_by_id('DERIVED_SSS_SCR_SSS_LINK_ANCHOR2')

        #Going to schedule
        schdl.click()

    except:
        print "Page failed to load, try increasing your speed constant"
        return

    #Frame switch to context frame


    browser.switch_to_frame('TargetContent')

    #Gets semester list of inputs

    term = browser.find_elements_by_id('SSR_DUMMY_RECV1$sels$0')

    #Clicks on the current semester

    term[SEMESTER].click()

    #Finds continue button

    cont = browser.find_element_by_id('DERIVED_SSS_SCT_SSR_PB_GO')

    #Continues to grades page

    cont.click()

    #Waits for page to load

    time.sleep(SPEED_CONSTANT)

    #Gets table of course titles

    grade_string = ''

    try:

        courses = browser.find_elements_by_class_name('PAGROUPDIVIDER')

        #Iterates and print every course and its grade

        for idx, val in enumerate(courses):
            course = val.text
            grade = browser.find_element_by_id('DERIVED_REGFRM1_CRSE_GRADE_OFF$'+str(idx)).text
            grade_string+= '{0:60} : {1}\n'.format(course,grade)

    except:
        print "Page failed to load, try increasing your speed constant"
        return


    return grade_string

if __name__ == '__main__':
    print get_grades()
