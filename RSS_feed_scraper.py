
#-----Statement of Authorship----------------------------------------#
#
#  This is an individual assessment item.  By submitting this
#  code I agree that it represents my own work.  I am aware of
#  the University rule that a student must not act in a manner
#  which constitutes academic dishonesty as stated and explained
#  in QUT's Manual of Policies and Procedures, Section C/5.3
#  "Academic Integrity" and Section E/2.1 "Student Code of Conduct".
#
#    Student no: N9726471
#    Student name: Bogdan Todor
#
#  NB: Files submitted without a completed copy of this statement
#  will not be marked.  Submitted files will be subjected to
#  software plagiarism analysis using the MoSS system
#  (http://theory.stanford.edu/~aiken/moss/).
#
#--------------------------------------------------------------------#



#-----Task Description-----------------------------------------------#
#
#  News Archivist
#
#  In this task you will combine your knowledge of HTMl/XML mark-up
#  languages with your skills in Python scripting, pattern matching
#  and Graphical User Interface development to produce a useful
#  application for maintaining and displaying archived news or
#  current affairs stories on a topic of your own choice.  See the
#  instruction sheet accompanying this file for full details.
#
#--------------------------------------------------------------------#



#-----Imported Functions---------------------------------------------#
#
# Below are various import statements that were used in our sample
# solution.  You should be able to complete this assignment using
# these functions only.

# Import the function for opening a web document given its URL.
from urllib.request import urlopen

# Import the function for finding all occurrences of a pattern
# defined via a regular expression, as well as the "multiline"
# and "dotall" flags.
from re import findall, MULTILINE, DOTALL

# A function for opening an HTML document in your operating
# system's default web browser. We have called the function
# "webopen" so that it isn't confused with the "open" function
# for writing/reading local text files.
from webbrowser import open as webopen

# An operating system-specific function for getting the current
# working directory/folder.  Use this function to create the
# full path name to your HTML document.
from os import getcwd

# An operating system-specific function for 'normalising' a
# path to a file to the path-naming conventions used on this
# computer.  Apply this function to the full name of your
# HTML document so that your program will work on any
# operating system.
from os.path import normpath
    
# Import the standard Tkinter GUI functions.
from tkinter import *

# Import the SQLite functions.
from sqlite3 import *

# Import the date and time function.
from datetime import datetime

#
#--------------------------------------------------------------------#



#-----Student's Solution---------------------------------------------#
#
# Put your solution at the end of this file.
#

# Name of the folder containing your archived web documents.  When
# you submit your solution you must include the web archive along with
# this Python program. The archive must contain one week's worth of
# downloaded HTML/XML documents. It must NOT include any other files,
# especially image files.
internet_archive = 'InternetArchive'


################ PUT YOUR SOLUTION HERE #################
# Importing additional modules for the backend.
import os
import webbrowser

# Importing additional modules for the frontend.
from tkinter import *
from tkinter.ttk import Combobox
import tkinter

###-------------------------------BACK END-----------------------------------###

##-----------Section 1: Developing the extraction functionality---------------##

#

##----------------------Function 1: The RSS feed scraper----------------------##

# Creating a function that extracts the news from the xhtml files located inside
# the InternetArchive folder. This function reads the contents of the chosen
# archived file, applies regular expressions and extracts only the necessary
# information from it and stores it in a series of lists labelled from line 134
# to 138. The function then opens an empty html file, writes the fixed html
# template labelled as "Fixed_template" below then iterates over the first ten
# stories of the archived file, formats them, then inserts the information into
# the html file then closes it.

# Defining the name and the date of the files.
Day1 = ['CNET_News_12Oct2017','Thu, 12th Oct 2017']
Day2 = ['CNET_News_13Oct2017','Fri, 13th Oct 2017']
Day3 = ['CNET_News_14Oct2017','Sat, 14th Oct 2017']
Day4 = ['CNET_News_16Oct2017','Mon, 16th Oct 2017']
Day5 = ['CNET_News_17Oct2017','Tue, 17th Oct 2017']
Day6 = ['CNET_News_18Oct2017','Wed, 18th Oct 2017']
Day7 = ['CNET_News_19Oct2017','Thu, 19th Oct 2017']
Latest = ['CNET News Latest','Latest Update']

# Note: Sunday the 15th is missing due to the fact that only 5 Sunday stories
# were released. As a solution I archived an extra day and included that due
# to it having atleast 10 stories released on the day.

# Defining the scraper function.
def Scraper_function(Day):
    # Open the xhtml file to read the contents.
    CNET_file = open(normpath('InternetArchive/'+Day[0]+'.xhtml'),
                     encoding = 'UTF-8').read()
    
    # Applies regular expressions to the selected xhtml file to extract the
    # needed information.
    headline = findall("<title>([\s\S]*?)<\/title>", CNET_file)
    images = findall("<media:thumbnail url=([\s\S]*?)/>",CNET_file)
    description = findall("<description>([\s\S]*?)</description>",CNET_file)
    link = findall("<link>([\s\S]*?)</link>",CNET_file)
    dateline = findall("<pubDate>([\s\S]*?)<\/pubDate>",CNET_file)

#-------------------Notes about the positions of the lists---------------------#

# The first story title occurs at [2] - First two are permanent and non-changing
# The first story image occurs at [0] 
# The first story description occurs at [1] - First is permanent
# The first story link occurs at [2] - First two are permanent and non-changing
# The first story dateline occurs at [0]

#------------------------------------------------------------------------------#
    # Creating an empty html file to write to.
    # This file is generically named as its purpose is to be overwritten.
    CNET_file = open('CNET News.html','w', encoding ='UTF-8')    

    # Writing the fixed html template for every article into the file.
    # The below html code outlines the file type, outlines the styles used and
    # the layout of the end product.
    Fixed_html_template = """
    <!DOCTYPE html>
    <html>
      <head>
        <title>CNET News</title>
      </head>
      <style type="text/css">
      body {
        background-attachment: fixed;
      }

      h1, h2, h3, p {width: 70%; margin-left: auto; margin-right: auto;}

      #maincontainer{margin:0 auto; width: 70%}

      #content-section{background-color: white; box-shadow: 2px 2px 1px;}
      </style>
      <body background= "https://cdn.wallpapersafari.com/68/64/uG5JcC.png">
          <div id = "maincontainer">
          <section id ="content-section">
          <div class="imgElem"></div>
          <h1><font size = "10"><center>CNET News</center></font></h1>
          <h2><center> THE DATE </center></h2>
          <p style = "text-align:center"><img src =
          "https://www.cnet.com/bundles/cnetcss/images/core/redball/logo_192.png"
          alt = "CNET logo not found" style = "width: 50%"></p>
          <p><strong>Source:</strong> <a href = https://www.cnet.com/g00/3_c-8yyy.epgv.eqo_/c-8OQTGRJGWU46x24jvvrux3ax2fx2fyyy.epgv.eqox2ftuux2fpgyux2f_$/$/$/$>
          Click here </a></p>
          <p><strong> Archivist:</strong> Bogdan Todor</p>
      </body>
    """.replace('THE DATE', Day[1]) # Replaces the first arguement "THE DATE"
    # with the second which is a variable linked to the chosen dates news.
    CNET_file.write(Fixed_html_template) # Writes the template into the file.

    # Creating a for loop that iterates over the 5 lists outlined previously
    # and inserts the information from them into the html file to create the
    # first 10 stories.
    #
    # A counter is also created to keep track of the number of stories and
    # iterations completed.
    #
    # The below html code creates a the template for the 10 daily stories.
    # The code allows for different inputs by incorporating .replace().
    
    counter = 0
    for stories in range(10):
        # Inserts the story number into headline.
        story_number = '''
          <hr width = "98%" size = 6px>
          <item>
            <h3><center> INSERT STORY NUMBER HERE
        '''.replace('INSERT STORY NUMBER HERE', str(counter + 1)+'. ')
        CNET_file.write(story_number)

        # Inserts the story headline into the html file.
        story_headline ='''
            INSERT STORY HEADLINE HERE</center></h3>
        '''.replace('INSERT STORY HEADLINE HERE', headline[counter+2])
        CNET_file.write(story_headline)

        # Inserts the story image into the html file.
        story_image = '''
            <p style = "text-align:center"><img src = "INSERT IMAGE URL HERE"
            alt = "Sorry, image not found!" style = "width: 70%"></p>
        '''.replace('"INSERT IMAGE URL HERE"', images[counter+0])
        CNET_file.write(story_image)

        # Inserts the story description into the html file.
        story_description = '''
            <p> INSERT DESCRIPTION HERE</p>
        '''.replace('INSERT DESCRIPTION HERE', description[counter+1])
        CNET_file.write(story_description)

        # Inserts the link to the full story into the html file.
        story_link = '''
            <p><strong>Full Story:</strong> <a href = "URL" > URL</a></p>
        '''.replace('URL', link[counter+2])
        CNET_file.write(story_link)

        # Inserts the story dateline into the html file.
        story_dateline = '''
            <p><strong>Dateline:</strong> INSERT DATELINE HERE </p>
          </item>
          <br>
        '''.replace('INSERT DATELINE HERE',dateline[counter+0])
        CNET_file.write(story_dateline)

        # Increase counter by 1 upon each iteration.
        counter = counter + 1

    # Closing the html tag.
    CNET_file.write('''
    </html>
    ''')
    # Closing the html file.
    CNET_file.close()

##-------------------------Function 2: The Extractor--------------------------##

# Creating a function which, when pressed, creates a html file in the same
# directory as this program with the chosen dates news. This function does that
# by linking the users drop down menu (combo box) selection to its corresponding
# archived xhtml file through the variable "Day". The function then calls the
# Scraper function (shown above) to extract the news from that particular day
# and write it to the universal html file called "CNET News"

def Extract_news():
    choice = story_dates.get()
    # If the extract button is pushed with no date selected,
    # display an error message to the user.
    if choice != story_dates:
        text_label.config(text = 'Error: Pick a date')
    # Assigns the list option to the corresponding archived file then prints a
    # message to alert the user the process is complete.
    if choice == Article_dates[0]:
        Day = Day1
        Scraper_function(Day) # Calls the function to extract the news.
        text_label.config(text = 'Extracted!') #
    if choice == Article_dates[1]:
        Day = Day2
        Scraper_function(Day)
        text_label.config(text = 'Extracted!')
    if choice == Article_dates[2]:
        Day = Day3
        Scraper_function(Day)
        text_label.config(text = 'Extracted!')
    if choice == Article_dates[3]:
        Day = Day4
        Scraper_function(Day)
        text_label.config(text = 'Extracted!')
    if choice == Article_dates[4]:
        Day = Day5
        Scraper_function(Day)
        text_label.config(text = 'Extracted!')
    if choice == Article_dates[5]:
        Day = Day6
        Scraper_function(Day)
        text_label.config(text = 'Extracted!')
    if choice == Article_dates[6]:
        Day = Day7
        Scraper_function(Day)
        text_label.config(text = 'Extracted!')
    # If the file exists, set the label text to "extracted!".
    # However if the file doesnt exist, instead of crashing due to a
    # FileNotFoundError, set the label text to "Error: Archive latest first".
    try:
        if choice == Article_dates[7]:
            Day = Latest
            Scraper_function(Day)
            text_label.config(text = 'Extracted!')
    except FileNotFoundError:
            text_label.config(text = 'Error: Archive latest first')    

    # Part B - If the checkbox is checked, open the connection to the database 
    # and create a local view, execute the necessary query which logs what 
    # command has been executed, commit the change then close the connections.
    # NOTE - this is applied to all of the button functions and operates in
    # the exact same way, therefore no additional comments will be made in
    # regards to the functionality of the code snippet below.
    global button_clicked
    button_clicked = 1 # Sets this function to button 1.
    if button_state == 1: # If the button is on.
        event_logger() # Call the function to log the event.

##------------Section 2: Developing the display functionality-----------------##

# Creating the function that opens the extracted html file in the users default
# web browser.
def Display_news():
    # If the file exists, open it in the default browser.
    if os.path.exists('CNET News.html'):
        webbrowser.open(normpath('file://' +os.path.realpath('CNET News.html')))
        text_label.config(text = 'Displaying...')
    else:
    # If the file doesn't exist, tell the user to extract the news first.
        text_label.config(text = 'Error: Extract article first')

    # Part B - writing event to SQL if event logging is active.
    global button_clicked
    button_clicked = 2 # Sets this function to button 2.
    if button_state == 1: # If the button is on.
        event_logger() # Call the function to log the event.

##-------Section 3: Developing the archive latest news functionality----------##

# Defining the "Archive latest" button function which downloads the latest
# rss feed into the InternetArchive folder.
def Archive_latest_news():
    url = 'https://www.cnet.com/rss/news/'
    web_page = urlopen(url)
    web_page_contents = web_page.read().decode('UTF-8', 'ignore')
    CNET_file = open(normpath('InternetArchive/'+'CNET News Latest.xhtml'), 'w',
                     encoding = 'UTF-8')
    CNET_file.write(web_page_contents)
    CNET_file.close()
    text_label.config(text = 'Latest news archived')

    # Part B - Writing the event to SQL if event logging is active.
    global button_clicked
    button_clicked = 3 # Sets this function to button 3.
    if button_state == 1: # If the button is on.
        event_logger() # Call the function to log the event.


##------------Section 4: Developing the logging functionality-----------------##

# Creating the checkbox button functionality. 
# In essence, when the checkbox is unchecked, nothing happens, however when it
# is checked the "button_checked" variable becomes 1. When the button is checked
# the button_state variable equals 1 and the button becomes active. This has
# been used to create a "toggle" effect. Effectively, when the button is checked
# the variable equals 1 and the event logging is enabled whereas when its
# unchecked it equals 0 and is off.When the checkbox is clicked to uncheck it, 
# the function realises this as an input and records it in SQL. Once the button
# is unchecked, no other events are recorded.

button_state = 0 # 0 indicates the button is unchecked, 1 indicates checked.

def logger_switch():
    global button_state
    global button_clicked
    
    if button_state == 0: # If the checkbutton is off.
        button_state = button_state + 1 # Switches button on.
        button_clicked = 4
        event_logger() # Calling the function that logs the events.
    else:
        button_state = button_state - 1 # Switches button off.
        event_logger() # Calling the function that logs the events.
        

# Creating the logging function which inserts a message into the db depending
# on which button is pressed if the checkbutton is on. It also inserts a
# message into the db when the checkbutton is turned off to indicate the end
# of the logging session.

def event_logger():
    global button_state
    global button_clicked
    # Connecting to the database and establishing a local view.
    CNET_db = connect('event_log.db')
    db_view = CNET_db.cursor()

    if button_state == 0: # If the checkbox is unchecked.
        db_view.execute('''INSERT INTO Event_Log
            Values(NULL, "Event logger disabled")''')
        CNET_db.commit() # Write the query into the db.
    else:
        if button_clicked == 1: # If the extract button has been pushed.
            db_view.execute('''INSERT INTO Event_Log
            Values(NULL, "News has been extracted")''')
            CNET_db.commit() # Write the query into the db.
            
        if button_clicked == 2: # If the display button has been pushed.
            db_view.execute('''INSERT INTO Event_Log
            Values(NULL, "The selected news is displayed in the browser")''')
            CNET_db.commit() # write the query into the db.

        if button_clicked == 3: # If the archive latest button has been pushed.
            db_view.execute('''INSERT INTO Event_Log
            Values(NULL, "The latest news has been downloaded and stored")''')
            CNET_db.commit() # Write the query into the db.

        if button_clicked == 4: # If the checkbox has been checked.
            db_view.execute('''INSERT INTO Event_Log
            Values(NULL, "Event logger enabled")''')
            CNET_db.commit() # write the query into the db.

    # Closing the connections to the database.
    db_view.close()
    CNET_db.close()

    

    

###-------------------------------FRONT END----------------------------------###

##----------Section 4: Developing the GUI functionality and design------------##

# Setting up the GUI window.
CNET_GUI_window = Tk()

# Setting the GUI's title.
CNET_GUI_window.title('CNET News Archive')

# Setting the size of the GUI.
CNET_GUI_window.geometry("505x300")

# Changing the GUI's background colour. 
CNET_GUI_window.configure(background='white')

# Importing the CNET logo as an image for design purposes.
image1 = PhotoImage(file = "cnet-news_logo.gif")
image_label1 = Label(CNET_GUI_window, image=image1)

# Importing the image for the bottom border.
image2 = PhotoImage(file = "bottom_border.gif")
image_label2 = Label(CNET_GUI_window, image=image2)

##----------------------------creating the widgets----------------------------##

# Importing the label.
text_label = Label(text = 'Choose date', bg = 'white',
                   font=('Courier New ',16, 'bold'))

# Combo box list options.
Article_dates = \
['Thu, 12th Oct 2017',
'Fri, 13th Oct 2017',
'Sat, 14th Oct 2017',
'Mon, 16th Oct 2017',
'Tue, 17th Oct 2017',
'Wed, 18th Oct 2017',
'Thu, 19th Oct 2017',
'Latest Update']

# Creating the combo box drop down menu.
story_dates =Combobox(CNET_GUI_window, values = Article_dates, justify = CENTER)

# Creating the button used to extract the selected day's news.
extract_button = Button(CNET_GUI_window, text = 'Extract article',
                        command = Extract_news)

# Creating the button to display the extracted news in the default browser.
display_button = Button(CNET_GUI_window, text = 'Display article',
                        command = Display_news)

# Creating the button that archives the latest news from the RSS feed.
archive_latest_button = Button(CNET_GUI_window, text = 'Archive latest',
                               command = Archive_latest_news)

# Importing the logging Checkbutton.
logger_switch = Checkbutton(CNET_GUI_window, text = 'Event Logger'
                         ,command = logger_switch, relief = "raised")

# Packing all of the widgets into the main window.
story_dates.place(x = 345, y = 15)
extract_button.place(x=20,y = 15)
display_button.place(x=130,y= 15)
archive_latest_button.place(x = 240 , y = 15)
image_label1.place(x=0, y=50)
image_label2.place(x=-2, y = 209)
text_label.place(x=178, y=215)
logger_switch.place(x=400, y=265)

# Starting the event loop.
CNET_GUI_window.mainloop()
