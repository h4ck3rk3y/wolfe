r"""
mrwolf is a problem solver and tries his best to solve your problems

Usage:
  mrwolf z
  mrwolf b
  mrwolf f
  mrwolf t
  mrwolf k

Options:
  -h --help   Show this screen.
  --version   Show version.

"""

import requests
from docopt import docopt
import json

__version__ = '0.0.3'

def main():
  '''mrwolf is a problem solver and tries his best to solve your problems'''
  arguments = docopt(__doc__, version=__version__)

if __name__ == '__main__':
  main()