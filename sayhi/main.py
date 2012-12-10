# -*- coding: utf-8 -*-
import sys
import getpass
from optparse import OptionParser

from termcolor import cprint

from . import __version__


def main():
    usage = 'usage: %prog [options]'
    parser = OptionParser(usage=usage)
    parser.add_option('-c', '--color',
                      action='store', type='string', dest='color',
                      help='Text color')
    parser.add_option('-u', '--user',
                      action='store', type='string', dest='user',
                      help='Username to greet')
    parser.add_option('-v', '--version',
                      action='store_true', dest='version',
                      help='Show version number')
    (options, args) = parser.parse_args()

    # version check
    if options.version:
        print 'Version %s' % __version__
        sys.exit()

    colors = ['red', 'green', 'blue']
    color = None
    if options.color in colors:
        color = options.color

    user = options.user if options.user else getpass.getuser()

    cprint('Greetings, %s!' % user, color)


if __name__ == '__main__':
    main()
