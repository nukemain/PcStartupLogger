import time
import datetime
import calendar  
import os        
import msvcrt  
import random
import webbrowser
import datetime
import sys 
from os.path import join
from pathlib import Path

home = str(Path.home())
path_to_file = str(home) + "\\PcStartupLogger.txt"
File_Didnt_Exist_Until_Now = False
try: 
    logfile = open(path_to_file,'x') #opening a file with option x essentialy just checks if it exists
    print("flag-1")                                                                                             #flag-1
    #logfile.close() #the above function actually opens the file so we need to close it
    File_Didnt_Exist_Until_Now  = True
except FileExistsError: 
    print("FileExistsError")

logfile = open(path_to_file,'a')
if(File_Didnt_Exist_Until_Now):
    logfile.write("Pc turned on @ "+str(datetime.datetime.now())+" . Times this PC has been turned on since this files creation: 1 \n")
    logfile.close()
    time.sleep(5)
    sys.exit()
else:
    print("flag-2")
    logfile.close()
    logfile = open(path_to_file,'r')
    contents_of_the_log = logfile.readlines()
    last_line_of_the_log = contents_of_the_log[-1] # [-1] = last line
    Last_line_split_into_table = last_line_of_the_log.split(' ')
    Turned_on_counter = Last_line_split_into_table[-2]
    New_turned_on_counter = int(Turned_on_counter) + 1
    logfile.close()
    logfile = open(path_to_file,'a')
    logfile.write("Pc turned on @ "+str(datetime.datetime.now())+" . Times this PC has been turned on since this files creation: "+str(New_turned_on_counter)+" \n")
    logfile.close()
    time.sleep(5)
    sys.exit()