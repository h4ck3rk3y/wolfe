r"""
mrwolf is a problem solver and tries his best to solve your problems

Usage:
  mrwolf (b | bash) [-g | --google]
  mrwolf (f | fish) [-g | --google]
  mrwolf (k | ksh) [-g | --google]
  mrwolf (t | tcsh) [-g | --google]
  mrwolf (z | zsh) [-g | --google]
  mrwolf (on | off)
  mrwolf (l | last) <-g | --google>
  mrwolf

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

__version__ = '0.0.3'

def last(google=False):
  try:
    output = subprocess.check_output("echo $lasterr", shell = True, stderr = subprocess.STDOUT)
    if google:
      google(output[:30])
    else:
      stackoverflow(output[:30])
  except subprocess.CalledProcessError as e:
    print e.output
    return

def on():
  command = """PROMPT_COMMAND='last="$(cat /tmp/last)";lasterr="$(cat /tmp/lasterr)"; exec >/dev/tty; exec > >(tee /tmp/last); exec 2>/dev/tty; exec 2> >(tee /tmp/lasterr)'"""
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
  command = """PROMPT_COMMAND='last="$(cat /tmp/last)";lasterr="$(cat /tmp/lasterr)"; exec >/dev/tty; exec > >(tee /tmp/last); exec 2>/dev/tty; exec 2> >(tee /tmp/lasterr)'"""
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

def google(command, error):
  url = 'https://www.google.com/search?q=%s' %(command.split(" ")[0] +  " " + error)
  webbrowser.open(url)

def fetch_error(shell, google = False):
  filename = history_files[shell]
  filename = os.path.join(os.path.expanduser('~'), filename)
  try:
    history_file = open(filename, 'r')
    history_file.close()
  except (OSError, IOError) as e:
    print 'File Not Found'
    return
  except:
    print 'Unkown error'
    return
  command = subprocess.check_output(['tail', '-1', filename])
  print command
  try:
    subprocess.check_output(command, stderr=subprocess.STDOUT, shell=True)
  except subprocess.CalledProcessError as e:
    error = e.output
    if google:
      return google(errror[:30])
    else:
      return stackoverflow(error[:30])
  except:
    print 'Something unforseen happened.'



def main():
  '''mrwolf is a problem solver and tries his best to solve your problems'''
  arguments = docopt(__doc__, version=__version__)
  if arguments['b'] or arguments['bash']:
    fetch_error('bash', arguments['-g'] or arguments['--google'])
  elif arguments['f'] or arguments['fish']:
    fetch_error('fish', arguments['-g'] or arguments['--google'])
  elif arguments['k'] or arguments['ksh']:
    fetch_error('ksh', arguments['-g'] or arguments['--google'])
  elif arguments['t'] or arguments['tcsh']:
    fetch_error('tcsh', arguments['-g'] or arguments['--google'])
  elif arguments['z'] or arguments['zsh']:
    fetch_error('zsh', arguments['-g'] or arguments['--google'])
  elif arguments['on']:
    on()
  elif arguments['off']:
    off()
  else:
    print __doc__

if __name__ == '__main__':
  main()