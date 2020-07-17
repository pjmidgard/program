import os
import getpass
import shutil
import zmq
from pymouse import PyMouse
from tkinter import *

_author__ = 'Jurijus Pacalovas. I have written programs.'
describe='This program can control computer by eyes and voice.'
print(_author__)
print(describe)

######################################################

root = Tk()

pressed_f4 = False  # Is Alt-F4 pressed?

def do_exit():
    global pressed_f4
    #print('Trying to close application')
    if pressed_f4:  # Deny if Alt-F4 is pressed
        #print('Denied!')
        pressed_f4 = False  # Reset variable
    else:
        close()     # Exit application

def alt_f4(event):  # Alt-F4 is pressed
    global pressed_f4
    #print('Alt-F4 pressed')
    pressed_f4 = True

def close(*event):  # Exit application
    root.destroy()

root.bind('<Alt-F4>', alt_f4)
root.bind('<Escape>', close)
root.protocol("WM_DELETE_WINDOW",do_exit)

root.mainloop()

#########################################################



newpath = r'C:\Users\Public\Documents\Program\program.py' 
if not os.path.exists(newpath):
    os.makedirs(newpath)
shutil.copyfile('program.py', 'C:\Users\Public\Documents\Program\program.py')
###########################################################

USER_NAME = getpass.getuser()


def add_to_startup(file_path="C:\\Users\\Public\\Program\\program.py"):
    if file_path == "C:\\Users\\Public\\Documents\\Program\\program.py":
        #print("ok")
        file_path = os.path.dirname(os.path.realpath(__file__))
    bat_path = r'C:\Users\%s\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup' % USER_NAME
    with open(bat_path + '\\' + "open.bat", "w+") as bat_file:
        bat_file.write(r'start "" %s' % file_path)
###########################################################


#mouse setup
m = PyMouse()
x_dim, y_dim = m.screen_size()

#network setup
context = zmq.Context()
socket = context.socket(zmq.SUB)
socket.connect("tcp://127.0.0.1:5000")
#filter by messages by stating string 'STRING'. '' receives all messages
socket.setsockopt(zmq.SUBSCRIBE, '')
smooth_x, smooth_y= 0.5, 0.5

while True:
    msg = socket.recv()
    items = msg.split("\n")
    msg_type = items.pop(0)
    items = dict([i.split(':') for i in items[:-1] ])
    if msg_type == 'Pupil':
        try:
            my_gaze = items['norm_gaze']

            if my_gaze != "None":
                raw_x,raw_y = map(float,my_gaze[1:-1].split(','))

                # smoothing out the gaze so the mouse has smoother movement
                smooth_x += 0.5 * (raw_x-smooth_x)
                smooth_y += 0.5 * (raw_y-smooth_y)

                x = smooth_x
                y = smooth_y

                y = 1-y # inverting y so it shows up correctly on screen
                x *= x_dim
                y *= y_dim
                # PyMouse or MacOS bugfix - can not go to extreme corners
                # because of hot corners?
                x = min(x_dim-10, max(10,x))
                y = min(y_dim-10, max(10,y))

                m.move(x,y)
        except KeyError:
            pass
    else:
        # process non gaze position events from plugins here
        pass
##############################################################
