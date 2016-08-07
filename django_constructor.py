import subprocess
import os


def check(expected_file):
        f = open(expected_file, 'r')
        for line in f:
            if "STATIC_URL = '/static/'" in line:
                return True

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
invalid = ['', '\n']
while path in invalid:
    path = input('Enter the absolute path where you want the project: ')
    path = path.lstrip()

    if path is '\n':
        path = os.getcwd

    try:
        os.chdir(path)
        break
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

# Make the directory
bashCommand = "sudo mkdir {0}".format(dir)
process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
output = process.communicate()[0]

# Go to the directory
path += dir
os.chdir(path)

# Set up virtual environment
bashCommand = 'python3 -m venv venv'
process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
output = process.communicate()[0]

print("You now have a virtual environment named 'venv'.")
print('Make sure to activate it anytime you want to run your servers!')

print("Now let's install some dependencies: ")
print('\n')

# Try to install basic dependencies with pip
try:
    depend = ['django', ]
    for d in depend:
        bashCommand = 'pip install {0}'.format(d)
        print('installing......... {0}'.format(d))
        process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
        output = process.communicate()[0]
except:
    print("Looks like you don't have pip!")
    print("If you're trying to run this with the default Python installation, " +
          "it's not going to work.")
    print("Try installing brew (Found here: http://brew.sh) and then run this " +
          " script again!")
    print(".......................OR IF YOU TRUST ME...........................")
    print("Copy and paste into your terminal: /usr/bin/ruby -e " +
          "'$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)'")
    exit()

# Set up django project
project = input('What do you want to call your project? ')
bashCommand = 'django-admin startproject {0} .'.format(project)
process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
output = process.communicate()[0]

path = path + '/' + project
os.chdir(path)

expected_file = 'settings.py'

f = open(expected_file, 'a')
if check(expected_file):
    f.write("STATIC_ROOT = os.path.join(BASE_DIR, 'static')\n")
else:
    f.writelines(
        ["""STATIC_URL = '/static/'\n", "STATIC_ROOT = os.path.join(BASE_DIR,
         'static')\n\n"""])

f.close()

# YEET, success has been achieved
print('\n')
print('........................')
print('.      Success!!!!     .')
print('........................')
print('\n')
print('Our current directory is: {0}'.format(os.getcwd()))
print('Thanks & Django on!')
print('For common commands and other django shortcuts, ' +
      'checkout https://github.com/jShiohaha/django-env')
