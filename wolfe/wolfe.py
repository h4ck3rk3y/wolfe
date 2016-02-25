r"""
i am winston wolfe, i solve problems

Usage:
  wolfe (on | off)
  wolfe (l | last)
  wolfe [QUERY ...] [-g | --google]

Options:
  -h --help   Show this screen.
  --version   Show version.

"""

import requests
import subprocess
from docopt import docopt
import os
import shutil
import webbrowser
from api import stackoverflow

history_files = {
  'bash' : '.bash_history',
  'fish' : '.config/fish/fish_history',
  'ksh' : '.ksh_history',
  'tcsh' : '.tcsh_history',
  'zsh' : '.zsh_history'
}

__version__ = '0.0.7'

def last(last_arr, google=False):
	error = " ".join(last_arr[2:])
	position_of_last_colon = error.rfind(":")
	if position_of_last_colon <0:
		print 'Nothing wrong with the previous command!'
		return
	error_name = error[:position_of_last_colon].rfind(" ")
	error = error[error_name + 1:]
	if google:
		google_search(error)
	else:
		stackoverflow(error)


def on():
  command = """PROMPT_COMMAND='l="$(cat /tmp/lasterr)";exec 2>/dev/tty; exec 2> >(tee /tmp/lasterr)'"""
  try:
    shutil.copyfile(os.path.join(os.path.expanduser('~'), '.bashrc'), os.path.join(os.path.expanduser('~'), '.bashrc.bak'))
    basrhc_file = open(os.path.join(os.path.expanduser('~'), '.bashrc'), 'a')
    basrhc_file.write("\n")
    basrhc_file.write(command)
    basrhc_file.write("\n")
    basrhc_file.close()
    os.system("exec bash;")
  except (OSError, IOError) as e:
    print "bashrc Not Found"
  except:
    print 'Unkown Error'
    print 'Back up of bashrc in ~/.bashrc.bak'

def off():
  command = """PROMPT_COMMAND='l="$(cat /tmp/lasterr)";exec 2>/dev/tty; exec 2> >(tee /tmp/lasterr)'"""
  try:
    basrhc_file  = open(os.path.join(os.path.expanduser('~'), '.bashrc'), 'r')
    lines = basrhc_file.readlines()
    basrhc_file.close()
    basrhc_file  = open(os.path.join(os.path.expanduser('~'), '.bashrc'), 'w')
    for line in lines:
      if not command in line:
        basrhc_file.write(line)
    basrhc_file.close()
    os.system("kill -9 " + str(os.getppid()))
  except:
    import traceback; traceback.print_exc();
    print 'Unexpected error'
    print 'Back up of bashrc in ~/.bashrc.bak'

def google_search(error):
  url = 'https://www.google.com/search?q=%s' %(error)
  webbrowser.open(url)

def main():
  '''i am winston wolfe, i solve problems'''
  arguments = docopt(__doc__, version=__version__)
  if arguments['on']:
    print 'Mr. Wolfe is at your service'
    print 'If any of your programs run into an error'
    print 'use wolfe $l'
    print 'To undo the changes made by mr wolfe in your  bashrc, do wolfe off'
    on()
  elif arguments['off']:
    off()
    print 'Mr. Wolfe says goodbye!'
  elif arguments['QUERY']:
  	last(arguments['QUERY'], arguments['-g'] or arguments['--google'])
  else:
    print __doc__

if __name__ == '__main__':
  main()