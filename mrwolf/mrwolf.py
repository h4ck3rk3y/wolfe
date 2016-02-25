r"""
mrwolf is a problem solver and tries his best to solve your problems

Usage:
  mrwolf (z | zsh) (-g | --google)
  mrwolf (b | bash) (-g | --google)
  mrwolf (f | fish) (-g | --google)
  mrwolf (t | tcsh) (-g | --google)
  mrwolf (k | ksh) (-g | --google)
  mrwolf (on | off)
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

history_files {
  'bash' : '~/.bash_history',
  'fish' : '~/.config/fish/fish_history',
  'ksh' : '~/.ksh_history',
  'tcsh' : '~/.tcsh_history',
  'zsh' : '~/.zsh_history'
}

try:
  bash_mode_file = open(os.path.join(os.path.expanduser("~"), './mrwolf/config.json'), 'r')
  bash_mode = json.loads(bash_mode_file.read())['bash_mode']
  bash_mode_file.close()
except:
  bash_mode_file = open(os.path.join(os.path.expanduser("~"), './mrwolf/config.json'), 'w')
  bash_mode_file.write(json.dumps({'bash_mode' : False}))
  bash_mode = False
  bash_mode_file.close()


__version__ = '0.0.3'

def toggle(on, off):
  if on and bash_mode:
    print 'bash mode already on'
  elif on and not bash_mode:
    bash_mode = True
  elif off and not bash_mode:
    print 'bash mode already off'
  elif off and bash_mode:
    bash_mode = False

  bash_mode_file = open(os.path.join(os.path.expanduser("~"), './mrwolf/config.json'), 'w')
  bash_mode_file.write(json.dumps({'bash_mode' bash_mode}))
  bash_mode_file.close()

def fetch_error(history_file):

def main():
  '''mrwolf is a problem solver and tries his best to solve your problems'''
  arguments = docopt(__doc__, version=__version__)

if __name__ == '__main__':
  main()