#This program is made to take screenshots every 'x' seconds. Perfect for when you're sitting through boring Zoom meetings and you want to take screenshots of the presenters slide deck without having to PrtScr every time. 

import pyautogui
import os.path
import os
import time


file_number = 1
screenshot_folder = 'screenshot_folder\\' #! Folder you want to store your images... for the relative path.

# file_path = r'C:\Users\mjsek\Pictures\Screenshots\screenshot_'+str(file_number)+'.png' #? Creates the file path. Passing through the file_number allows it to be iterated for each screenshot doesn't overwrite eachother.  
#! This is fine for now, but may want to make a relative file path in the future. 

#? Below Create Relative file_path --> just created the relative_file path anyways. 
dirname = os.path.dirname(__file__)
file_name = os.path.join(dirname, screenshot_folder)
file_path = r''+file_name+str(file_number)+'.png'

check_directory = os.path.exists(file_name) #! Checks if directory exists. If yes = True, else False.


if check_directory == False: #! Create the directory if it does not exist.
    os.makedirs(file_name)
    print("Created: " + file_name)
    time.sleep(1)
else:
    print("This directory exists: " + file_name)

#? ^^^ End of creating a relative file_path.

def save_file():
    global file_exists
    global file_number
    global file_path
    global screenshot_folder
    
    file_exists = os.path.exists(file_path)
    # print(f"The current file_number = {file_number}") # prints current file_number
    if file_exists == True:
        # print("File Already Exists = "+ str(file_exists) +". File Number: " + str(file_number))
        file_number = file_number + 1 #! increments file_number until it finds the next one that doesn't exit. This is so that the screenshots don't overwrite themselves. 
        # print(f"New file number checking: {file_number} <--") # prints new file_number
        #? Create a absolute file_path
        # file_path = r'C:\Users\mjsek\Pictures\Screenshots\screenshot_'+str(file_number)+'.png'  #? Absolute File Path
        #? ^^^ End Create a absolute file_path
        #? Below Create Relative file_path
        dirname = os.path.dirname(__file__)
        file_name = os.path.join(dirname, screenshot_folder)
        file_path = r''+file_name+str(file_number)+'.png'
        #? ^^^ End of creating a relative file_path.
        file_exists = os.path.exists(file_path)
        save_file() #! program calls itself until it gets to new file number. Note - Probably just better to add time component or something to the variable. But this works for now. 
    elif file_exists == False:
        myScreenshot = pyautogui.screenshot()
        myScreenshot.save(file_path)
    else:
        print("Uh... Something Went Wrong Yo.")

  
while(True):
    save_file() 
    print(f"Screenshot Saved {file_number}.png")
    time.sleep(10) #? Sleeps for 'x' seconds before running again. i.e. takes a screenshot every 10 seconds. 
