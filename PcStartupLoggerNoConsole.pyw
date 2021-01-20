import datetime
import os        
import datetime
import sys 
from pathlib import Path

home = str(Path.home())
path_to_file = str(home) + "\\PcStartupLogger.txt"
File_Didnt_Exist_Until_Now = False
try: 
    logfile = open(path_to_file,'x') #opening a file with option 'x' essentialy just checks if it exists 
    File_Didnt_Exist_Until_Now  = True
except FileExistsError: 
    File_Existed_Before = True 
    # we dont really need to do anything here but i need a single line of code here to prevent a error


logfile = open(path_to_file,'a') #opening a file with option 'a' allows us only to append new lines, which is exactly what we want

if(File_Didnt_Exist_Until_Now):# file didnt exist before so we set the count to 1 manualy
    logfile.write("Pc turned on @ "+str(datetime.datetime.now())+" . Times this PC has been turned on since this files creation: 1 \n")
    logfile.close()
    sys.exit()
else:
    logfile.close()
    logfile = open(path_to_file,'r')
    contents_of_the_log = logfile.readlines()
    last_line_of_the_log = contents_of_the_log[-1] # [-1] = last line
    Last_line_split_into_table = last_line_of_the_log.split(' ') # split the line into a table containing 
    Turned_on_counter = Last_line_split_into_table[-2] #Get the value ([-1] would be \n so we need [-2])
    New_turned_on_counter = int(Turned_on_counter) + 1
    logfile.close()  #we close the file because it is in the wrong operating mode ...
    logfile = open(path_to_file,'a')# ... and open it in the 'a' (append) mode
    logfile.write("Pc turned on @ "+str(datetime.datetime.now())+" . Times this PC has been turned on since this files creation: "+str(New_turned_on_counter)+" \n")
    logfile.close()
    sys.exit()
