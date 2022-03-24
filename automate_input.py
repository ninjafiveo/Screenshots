from pickletools import pyunicode
import pyautogui
import time
import os

start_page = int(input("please enter the page you would like to start printing from: "))
time.sleep(.5)
num_of_pages_to_print = int(input("Please enter the number of pages to print: "))
num_of_pages_to_print = num_of_pages_to_print - 1
time.sleep(.5)
print("Process Started")
print_from_page = start_page
print_to_page = start_page + num_of_pages_to_print
file_name = f"Book_Pages_{print_from_page}_{print_to_page}"

#TODO: Check and see if folder exist, if it doesn't create one to save pages there. 
book_folder = 'book_folder\\' #! Folder you want to store your images... for the relative path.

# file_path = r'C:\Users\mjsek\Pictures\Screenshots\screenshot_'+str(file_number)+'.png' #? Creates the file path. Passing through the file_number allows it to be iterated for each screenshot doesn't overwrite eachother.  
#! This is fine for now, but may want to make a relative file path in the future. 

#? Below Create Relative file_path --> just created the relative_file path anyways. 
dirname = os.path.dirname(__file__)
book_file_name = os.path.join(dirname, book_folder)
check_directory = os.path.exists(book_file_name) #! Checks if directory exists. If yes = True, else False.

if check_directory == False: #! Create the directory if it does not exist.
    os.makedirs(book_file_name)
    print("Created: " + book_file_name)
    time.sleep(.1)
else:
    print("This directory exists: " + book_file_name)

#? ^^^ End of creating a relative file_path.
#TODO: Create while loop that runs until pages numbers are done. 

def RUN_PRINT():
    global print_from_page
    global print_to_page
    global num_of_pages_to_print
    file_name = f"Book_Pages_{print_from_page}_{print_to_page}"
    # print(pyautogui.size()) #1920 x 1080
    #! Move to 3 dots and click for dropdown menu.
    pyautogui.moveTo(1875, 120, .3) #Moves mouse to absolute position  on screen. moveTo(Pixels Left to Right, Pixels Top to Bottom, Speed)
    # pyautogui.moveTo(1875, 215, .3)
    pyautogui.click()

    #! Click to pull up print dialogue
    pyautogui.moveRel(0,95,.5) #moves mouse relative to last position.
    pyautogui.click()

    #! Move to print # of pages dialogue
    #? Print from Box
    pyautogui.moveTo(821, 595, 1)
    pyautogui.click()
    pyautogui.hotkey('ctrlleft', 'a')
    pyautogui.hotkey('del')
    pyautogui.typewrite(f'{print_from_page}')#! Need incrementing var   here

    #? Print to Box
    pyautogui.moveTo(1004, 595, .1)
    pyautogui.click()
    pyautogui.hotkey('ctrlleft', 'a')
    pyautogui.hotkey('del')
    pyautogui.typewrite(f'{print_to_page}')#! Need incrementing var here

    pyautogui.moveTo(1125, 580, .1)
    time.sleep(.3)
    pyautogui.click()
    time.sleep(15) #? Wait for print job to generate

    #! Click print pop-up
    pyautogui.moveTo(1651, 209, .1)
    pyautogui.click()
    time.sleep(1)


    #! Click print/save on actual print dialog.
    pyautogui.moveTo(1474, 900, .3)
    pyautogui.click()
    time.sleep(1)

    #TODO: Change save location to "book_folder" above
    pyautogui.moveTo(608, 65, .3)
    pyautogui.click()
    time.sleep(.1)
    pyautogui.click()
    pyautogui.hotkey('ctrlleft', 'a')
    pyautogui.hotkey('del')
    pyautogui.typewrite(book_file_name)
    pyautogui.hotkey('enter')
    
    #! Click the Save Location
    pyautogui.moveTo(410, 444, .3)
    pyautogui.click()
    time.sleep(.1)
    pyautogui.click()
    pyautogui.hotkey('ctrlleft', 'a')
    pyautogui.hotkey('del')
    pyautogui.typewrite(file_name)
    pyautogui.moveTo(789, 510, .3)
    pyautogui.click()
    time.sleep(1)
    print_from_page = print_from_page + num_of_pages_to_print
    print_to_page = print_to_page + num_of_pages_to_print
    time.sleep(1)
    RUN_PRINT()

RUN_PRINT()
#!!!!!
# Additional Function
#?pyautogui.dragTo() # This is left click and hold where you want to move the mouse to.
#?pyautogui.dragRel()
#?pyautogui.scroll(-200) #scrolling -down +up

# pyautogui.typewrite('You this is the text that is going in.') #Type keys
# pyautogui.write('Hello world!')                 # prints out "Hello world!" instantly
# pyautogui.write('Hello world!', interval=0.25)  # prints out "Hello world!" with a quarter second delay after each character
# pyautogui.hotkey('ctrlleft', 'a')#hotkeys = CTRL-C, CTRL-V... Key down presses - This is for select all.

#pyautogui.press('enter')  # press the Enter key
#pyautogui.press('f1')     # press the F1 key
#pyautogui.press('left')   # press the left arrow key
#pyautogui.keyDown('shift')  # hold down the shift key
#pyautogui.press('left')     # press the left arrow key
#pyautogui.keyUp('shift')    # release the shift key
#pyautogui.press(['left', 'left', 'left'])
#pyautogui.press('left', presses=3)
# with pyautogui.hold('shift'): #Hold shift while you press left.
#         pyautogui.press(['left', 'left', 'left'])
# pyautogui.hotkey('ctrl', 'shift', 'esc') #same thing as press down then press up.

#! Keyboard Keys
# ['\t', '\n', '\r', ' ', '!', '"', '#', '$', '%', '&', "'", '(',
# ')', '*', '+', ',', '-', '.', '/', '0', '1', '2', '3', '4', '5', '6', '7',
# '8', '9', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`',
# 'a', 'b', 'c', 'd', 'e','f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
# 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '{', '|', '}', '~',
# 'accept', 'add', 'alt', 'altleft', 'altright', 'apps', 'backspace',
# 'browserback', 'browserfavorites', 'browserforward', 'browserhome',
# 'browserrefresh', 'browsersearch', 'browserstop', 'capslock', 'clear',
# 'convert', 'ctrl', 'ctrlleft', 'ctrlright', 'decimal', 'del', 'delete',
# 'divide', 'down', 'end', 'enter', 'esc', 'escape', 'execute', 'f1', 'f10',
# 'f11', 'f12', 'f13', 'f14', 'f15', 'f16', 'f17', 'f18', 'f19', 'f2', 'f20',
# 'f21', 'f22', 'f23', 'f24', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f9',
# 'final', 'fn', 'hanguel', 'hangul', 'hanja', 'help', 'home', 'insert', 'junja',
# 'kana', 'kanji', 'launchapp1', 'launchapp2', 'launchmail',
# 'launchmediaselect', 'left', 'modechange', 'multiply', 'nexttrack',
# 'nonconvert', 'num0', 'num1', 'num2', 'num3', 'num4', 'num5', 'num6',
# 'num7', 'num8', 'num9', 'numlock', 'pagedown', 'pageup', 'pause', 'pgdn',
# 'pgup', 'playpause', 'prevtrack', 'print', 'printscreen', 'prntscrn',
# 'prtsc', 'prtscr', 'return', 'right', 'scrolllock', 'select', 'separator',
# 'shift', 'shiftleft', 'shiftright', 'sleep', 'space', 'stop', 'subtract', 'tab',
# 'up', 'volumedown', 'volumemute', 'volumeup', 'win', 'winleft', 'winright', 'yen',
# 'command', 'option', 'optionleft', 'optionright']

#? Window Handling Features 
# pyautogui.getWindows() # returns a dict of window titles mapped to window IDs
# pyautogui.getWindow(str_title_or_int_id) # returns a “Win” object
# win.move(x, y)
# win.resize(width, height)
# win.maximize()
# win.minimize()
# win.restore()
# win.close()
# win.position() # returns (x, y) of top-left corner
# win.moveRel(x=0, y=0) # moves relative to the x, y of top-left corner of the window
# win.clickRel(x=0, y=0, clicks=1, interval=0.0, button=’left’) # click relative to the x, y of top-left corner of the window
# Additions to screenshot functionality so that it can capture specific windows instead of full screen.


#! Help: https://www.youtube.com/watch?v=2VkJhtDAKIc&t=234s
#! https://www.codegrepper.com/code-examples/python/pyautogui+delete
#! Notes: https://pyautogui.readthedocs.io/en/latest/keyboard.html



