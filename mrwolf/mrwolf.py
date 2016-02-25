r"""
mrwolf is a problem solver and tries his best to solve your problems

Usage:
  mrwolf (b | bash) (-g | --google)
  mrwolf (f | fish) (-g | --google)
  mrwolf (k | ksh) (-g | --google)
  mrwolf (t | tcsh) (-g | --google)
  mrwolf (z | zsh) (-g | --google)
  mrwolf

Options:
  -h --help   Show this screen.
  --version   Show version.

"""

import requests
import subprocess
from docopt import docopt
import os
import json
import webbrowser

history_files {
  'bash' : '~/.bash_history',
  'fish' : '~/.config/fish/fish_history',
  'ksh' : '~/.ksh_history',
  'tcsh' : '~/.tcsh_history',
  'zsh' : '~/.zsh_history'
}

__version__ = '0.0.3'

def google(command, error):
  url = 'https://www.google.com/search?q=%s' %(command.split(" ")[0] +  " " + error)
  webbrowser.open(url)

def fetch_error(shell, google = False):
  filename = history_files[shell]
  try:
    history_file = open(filename, 'r')
    history_file.close()
  except (OSError, IOError) as e:
    print 'File Not FOund'
    return
  except:
    print 'Unkown error'
    return
  command = subprocess.check_output(['tail', '-1', filename])
  try:
    subprocess.check_output(command, stderr=subprocess.STDOUT, shell=True)
  except subprocess.CalledProcessError as e:
    error = e.output
    if google:
      return google(command, errror[:30])
    else:
      return stackoverflow(command, error[:30])
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
  elif arguments['zsh'] or arguments['zsh']:
    fetch_error('zsh', arguments['-g'] or arguments['--google'])
  else:
    print __doc__

if __name__ == '__main__':
  main()