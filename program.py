import os
import getpass
import shutil


_author__ = 'Jurijus Pacalovas. I have written control programs.'
describe='This program can control computer by eyes and voice.'
print(_author__)
print(describe)


newpath = r'C:\Users\Public\Documents\Program\program.py' 
if not os.path.exists(newpath):
    os.makedirs(newpath)
shutil.copyfile('program.py', 'C:\\Users\\Public\\Documents\\Program\\program.py')
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




os.system('Notepad.exe')

