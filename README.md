# SageGrades
A simple Python script to get grades from Oracle PeopleSoft / Brandeis Sage

The SAGE website is located at https://sage.brandeis.edu and is used to display grades and other information.

However, the number of clicks to get to your grades usually exceeds four, and can be very laggy. 

To make it easy to see this semester's grades, I made a script that quickly goes to the right place.

This script uses Selenium, which is a python module for automatic page traversal. Simple DOM traversal is not possible, as a lot of Javascript is executed to display the grades (non-static pages).

To use this script, simply place your Brandeis credentials as the `BRANDEIS_ID` and `BRANDEIS_PASSWORD` as environment variables:

        export BRANDEIS_ID=johndoe
        export BRANDEIS_PASSWORD=thisismypassword

Before running, make sure you have Selenium installed:

    pip install selenium

Afterwards, you can simply execute this script with:

    python sage.py

After about a minute, your grades will be printed: 


	COSI 30A - INTRO THEORY COMPUTATION                          : ?
	COSI 105B - SOFTWARE ENGINEERING TO SCALE                    : ?
	COSI 132A - INFORMATION RETRIEVAL                            : ?
	COSI 146A - PRINC. OF COMP. SYSTEM DESIGN                    : ?
	THA 15B - PUBLIC SPEAKING                                    : ?

By default, these are the grades for the most recent semester on your "Class Schedule". However, you can retrieve earlier grades by changing the `SEMESTER` constant to a larger one in the source file. For seniors in their last semester -> 0, else 1.

- 0 = newest semester (if !senior, the one you finished registering for)
- 1 = most recent completed semester (probably the one you have new grades for)

## Run headless

To run this without having it open your browser, or altenrtively, to run it in a machine without a screen through a termianl, I referred to [this](http://elementalselenium.com/tips/38-headless) tutorial. The gist is that you need to install the `xvfb` utility, on Apt:

    sudo apt-get install xvfb
    
This can be followed by exeucting the script in the python environment using `xvfb`:
    
    xvfb-run python sage.py
    
Which should work without opening a Firefox window.

## Upload to Simplenote

If you use [Simplenote](http://www.simplenote.com), as I do, you can use note_sync to periodically (every 5 min by default) sync your current grades to your notes, which syncs with the notes on your phone / computer. 

To run, simply set the following environment variables:

        export EMAIL=your_simplenote_email@somehwere.com
        export PASSWORD=mypassword
        export NOTE_NAME=grades_2015

Then run `note_sync.py`. It will run forever, and check every 5 min.

