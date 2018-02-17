import subprocess
import os
from functools import wraps
import errno
import signal

print('................Welcome..................')
print('.                                       .')
print(". Let's get your django project set up! .")
print('.         First things first            .')
print('.........................................')
print('\n')

cwd = os.getcwd()
print("Let's decide where you would like to store the project...")
print('If you do not enter anything, we will create the project in the ' +
      'current directory!')
print('By the way, this is your current directory: {0}'.format(cwd))

path = ''
invalid_path = True
while invalid_path:
    path = input('Enter the absolute path to the directory where you want the project: ')
    path = path.lstrip()

    if path is '\n':
        print("what is this...........")
        path = os.getcwd

    if not os.path.exists(path):
        print("Oops... Looks like that directory does not exist. Let's try again with a directory that already exists.")
        continue

    try:
        os.chdir(path)
        invalid_path = False
    except:
        print('Oops... Looks like you entered an invalid directory')
        print("If you don't know what absolute path you want, reference your " +
              " curent directory for an example!")
        print("(In case you forgot, it's {0})".format(cwd))

print('\n')

dir = input('What should we call the directory that contains your project? ')

print('Cool! Your directory is located at ~/{0}'.format(dir))
print("You can find it by running the command 'cd ~/{0}'".format(dir))
print("Don't worry about it... We'll go there now!")
print('\n')

# ----------------------------- Make the directory -----------------------------
bashCommand = "sudo mkdir {0}".format(dir)
process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
output = process.communicate()[0]

# ----------------------------- Go to the directory -----------------------------
end = len(path) - 1
if path[end] == '/':
    path += dir
else:
    path += "/" + dir
os.chdir(path)

# ----------------------------- Set up virtual environment -----------------------------
bashCommand = 'sudo python3 -m venv venv'
process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
output = process.communicate()[0]

print("You now have a virtual environment named 'venv'.")
print('Make sure to activate it anytime you want to run your servers!')

print("Now let's install some dependencies: ")
print('\n')

# ----------------------------- Try to install basic dependencies with pip -----------------------------
try:
    depend = ['django', ]
    for d in depend:
        bashCommand = 'pip install {0}'.format(d)
        print('installing......... {0}'.format(d))
        process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
        output = process.communicate()[0]
        print(output)
        print("\n\n")
except:
    print("Looks like you don't have pip!")
    print("If you're trying to run this with the default Python installation, " +
          "it's not going to work.")
    print("Try installing brew (Found here: http://brew.sh) and then run this " +
          " script again!")
    print(".......................OR, IF YOU TRUST ME...........................")
    print("Copy and paste into your terminal: /usr/bin/ruby -e " +
          "'$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)'")
    exit()

# ----------------------------- Set up django project -----------------------------
invalid_project = True

while invalid_project:
    project = input('What do you want to call your project? ')

    try:
        bashCommand = 'sudo django-admin startproject {0} .'.format(project)
        print("command is... " + bashCommand)
        process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
        output = process.communicate()[0]
        invalid_project = False
    except:
        print("Oops... Looks like we failed to create a new project. " + 
              "There might already be a Python module with name '{0}'. Let's try again.".format(project))

path = path + '/' + project
os.chdir(path)

# ----------------------------- Creating permissions -----------------------------
bashCommand = 'sudo chmod 777 settings.py'
process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
output = process.communicate()[0]

expected_file = 'settings.py'

f = open(expected_file, 'a')
if check(expected_file):
    f.write("STATIC_ROOT = os.path.join(BASE_DIR, 'static')\n")
else:
    f.writelines(
        ["""STATIC_URL = '/static/'\n", "STATIC_ROOT = os.path.join(BASE_DIR,
         'static')\n\n"""])

f.close()

# ----------------------------- Success -----------------------------
print('\n')
print('........................')
print('.      Success!!!!     .')
print('........................')
print('\n')
print('Your project directory is: {0}'.format(os.getcwd()))
print('Thanks & Django on!')
print('For common commands and other django shortcuts, ' +
      'checkout https://github.com/jShiohaha/django-env')


def check(expected_file):
        f = open(expected_file, 'r')
        for line in f:
            if "STATIC_URL = '/static/'" in line:
                return True