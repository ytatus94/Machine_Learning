#! /usr/bin/python

## list citations script version 0.1

## Copyright 2007 Tom Brown

## This program is free software; you can redistribute it and/or
## modify it under the terms of the GNU General Public License as
## published by the Free Software Foundation; either version 3 of the
## License, or (at your option) any later version.

## This program is distributed in the hope that it will be useful,
## but WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
## GNU General Public License for more details.

## You should have received a copy of the GNU General Public License
## along with this program.  If not, see <http://www.gnu.org/licenses/>.

## See http://www.stringwiki.org/wiki/SPIRES_script for more usage
## instructions

'''list citations script
Usage:
python listcitations.py TeX_file_name.tex [ -hbiv ] [ --help ]

TeX_file_name must contain citations as standard arXiv references,
e.g. hep-th/9711200, 0705.0303, Maldacena:1997re or SPIRES journal
references, e.g. CMPHA,43,199

Options:
-h, --help
displays this help message
-b
displays the BiBTeX entry
-i
displays the bibitem entry
-v
verbose mode
'''

__version__ = "0.1"
__author__ = "Tom Brown"
__copyright__ = "Copyright 2007 Tom Brown, GNU GPL 3"

import os, sys, spires, getopt, re

bibtexOpt = 0
bibitemOpt = 0
verboseOpt = 0

try:
    options, arguments = getopt.gnu_getopt(sys.argv[1:], 'hbiv', ['help'])
except getopt.error:
    print 'error: you tried to use an unknown option or the argument for an option that requires it was missing; try \'listcitations.py -h\' for more information'
    sys.exit(0)

for o,a in options:
    if o in  ('-h','--help'):
        print __doc__
        sys.exit(0)

    elif o == '-b':
        bibtexOpt = 1

    elif o == '-i':
        bibitemOpt = 1

    elif o == '-v':
        verboseOpt = 1

if len(arguments) != 1:
    print 'you didn\'t specify a TeX file; try \'listcitations.py -h\' for more information'
    sys.exit(0)
else:
    TeXfilename = os.path.expanduser(arguments[0])

if len(options) == 0:
    bibitemOpt = 1


print TeXfilename

citations = spires.listCitations(TeXfilename)

for citation in citations:
    if verboseOpt:
        print citation
    type,ref = spires.findRefType(citation)
    if verboseOpt:
        print type, ref
    if bibtexOpt:
        BiBTeX = spires.getBiBTeX(ref,type)
        BiBTeX = re.sub('Article{[^,]*,','Article{' + citation + ',',BiBTeX)
        print BiBTeX
    if bibitemOpt:
        bibitem = spires.getBibitem(ref,type)
        bibitem = re.sub('bibitem{[^}]*}','bibitem{' + citation + '}',bibitem)
        print bibitem