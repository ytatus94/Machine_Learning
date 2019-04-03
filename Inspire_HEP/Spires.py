#! /usr/bin/python

## SPIRES script version 0.6

## updated for inSPIRE

## Copyright 2015 Tom Brown

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

'''SPIRES script
Usage:
python spires.py reference [ -hbiatcev ] [ --help ] [ --library library.bib ] [ --download download_path/ ]
"reference" must be a standard arXiv reference, e.g. hep-th/9711200, 0705.0303, Maldacena:1997re or a SPIRES journal reference, e.g. CMPHA,43,199
Options:
-h, --help
displays this help message
-b
displays the BiBTeX entry
-i
displays the bibitem entry
-a
displays the author(s)
-t
displays the title
-c
displays the TeX citation key
-e
displays everything
-v
verbose mode

--download download_path/
for arXiv references downloads a pdf of the paper from the arXiv to the directory download_path/
--library library.bib
if it is not already in library.bib, appends the BiBTeX entry to library.bib; use at your own risk
'''

__version__ = "0.6"
__author__ = "Tom Brown"
__copyright__ = "Copyright 2015 Tom Brown, GNU GPL 3"


import sys, os, getopt, re, urllib



#\d is a decimal digit; \D is anything but a decimal digit
def findRefType(ref):
    ref = ref.replace('arxiv:','')
    if re.search(r'^[a-zA-Z\-\.]+/\d{7}$',ref):
        rType = 'old-style eprint'
    elif re.search(r'^\d{7}$',ref):
        rType = 'old-style eprint'
        ref = 'hep-th/' + ref
    elif re.search('^\d{4}\.\d{4,5}$',ref):
        rType = 'new-style eprint'
    elif re.search(r'^\D+:\d{4}[a-zA-Z]{2,3}$',ref):
        rType = 'texkey'
    else:
        rType = 'journal'

    return rType, ref



def getBiBTeX(ref,rType):
    if rType == 'old-style eprint':
        query = 'p=find+eprint+' + ref
    elif rType == 'new-style eprint':
        query = 'p=find+eprint+' + ref
    elif rType == 'texkey':
        query = 'texkey=' + ref
    elif rType == 'journal':
        query = 'j=' + ref
    else:
        return "no records were found in SPIRES to match your search, please try again"

    #http://inspirehep.net/search?p=hep-th%2F9711200&of=hx
    #http://inspirehep.net/search?p=1101.0121&of=hx


    BiBTeX = urllib.urlopen('http://inspirehep.net/search?' + query + '&of=hx').read()

    if 'No records' in BiBTeX:
        return "no records were found in SPIRES to match your search, please try again"

    BiBTeX = BiBTeX[BiBTeX.find('<pre>'):]
    BiBTeX = BiBTeX[BiBTeX.find('@'):]

    BiBTeX = BiBTeX[:BiBTeX.rfind('/pre>')]
    BiBTeX = BiBTeX[:BiBTeX.rfind('}')+1]
        
    return BiBTeX



def getBibitem(ref,rType):
    if rType == 'old-style eprint':
        query = 'p=find+eprint+' + ref
    elif rType == 'new-style eprint':
        query = 'p=find+eprint+' + ref
    elif rType == 'texkey':
        query = 'texkey=' + ref
    elif rType == 'journal':
        query = 'j=' + ref
    else:
        return "no records were found in SPIRES to match your search, please try again"

    bibitem = urllib.urlopen('http://inspirehep.net/search?' + query + '&of=hlxe').read()

    if 'No records' in bibitem:
        return "no records were found in SPIRES to match your search, please try again"

    bibitem = bibitem[bibitem.find('<pre>')+5:bibitem.rfind('/pre>')-1]

    #treat newlines correctly
    bibitem = bibitem.replace("<br>","\n").replace("<br />","\n").replace("&nbsp;"," ")

    return bibitem



def extractauthor(BiBTeX):
    # remove excess white space and replace with a single space
    data = re.sub(r'\s+',r' ',BiBTeX)

    author = data[data.find('author'):]
    author = author[author.find('\"')+1:]
    author = author[:author.find('\"')]

    return author



def extracttitle(BiBTeX):
    # remove excess white space and replace with a single space
    data = re.sub(r'\s+',r' ',BiBTeX)

    title = data[data.find('title'):]
    title = title[title.find('\"')+2:]
    title = title[:title.find('\"')-1]

    return title



def extractcite(BiBTeX):
    cite = BiBTeX[BiBTeX.find('{')+1:BiBTeX.find(',')]
    return cite



def downloadeprint(ref,rType,downloadPath):
    downloadPath = os.path.expanduser(downloadPath)
    if rType == 'old-style eprint':
        urllib.urlretrieve('http://arxiv.org/pdf/' + ref, downloadPath + ref.replace('/','-') + '.pdf')
    elif rType == 'new-style eprint':
        urllib.urlretrieve('http://arxiv.org/pdf/' + ref, downloadPath + ref + '.pdf')



def updatelibrary(cite,BiBTeX,BiBTeXlibraryFileName):
    BiBTeXlibraryFileName = os.path.expanduser(BiBTeXlibraryFileName)
    libraryfile = open(BiBTeXlibraryFileName, 'r')
    library = libraryfile.read()
    libraryfile.close()

    if library.count(cite) == 0:
        print 'adding BiBTeX entry to ' + BiBTeXlibraryFileName
        #find the end of the file (the second argument means count from
        #the end of the file
        libraryfile = open(BiBTeXlibraryFileName, 'a')
        libraryfile.write('\n' + BiBTeX + '\n')
        libraryfile.close()      
    else:
        print 'BiBTeX entry already in library'



def listCitations(fileName):
    fileName = os.path.expanduser(fileName)
    f=open(fileName, 'r')
    data = f.read()
    f.close()

    if data.find(r'\begin{thebibliography}') >= 0:
        data = data[:data.find(r'\begin{thebibliography}')]

    citations = []

    while(data.find(r'\cite{') >=0):
        data = data[data.find(r'\cite{') + 6:]
        if(data.find('}') >=0):
            citation = data[:data.find('}')]
            data = data[data.find('}')+1:]
            citation = citation + ','
            while(citation.find(',') >=0):
                if citation[:citation.find(',')] not in citations:
                    citations.append(citation[:citation.find(',')])
                citation = citation[citation.find(',')+1:]
    return citations



if __name__ == "__main__":

    authorOpt = 0
    titleOpt = 0
    bibtexOpt = 0
    bibitemOpt = 0
    citeOpt = 0
    verboseOpt = 0
    libraryOpt = 0
    downloadOpt = 0

    try:
        options, arguments = getopt.gnu_getopt(sys.argv[1:], 
        'hbiatcev', ['help','library=','download='])
    except getopt.error:
        print 'error: you tried to use an unknown option or the argument for an option that requires it was missing; try \'spires.py -h\' for more information'
        sys.exit(0)

    for o,a in options:
        if o in  ('-h','--help'):
            print __doc__
            sys.exit(0)

        elif o == '--library':
            if a == '':
                print '--library expects an argument'
                sys.exit(0)
            libraryOpt = 1
            BiBTeXlibraryFileName = os.path.expanduser(a)
            print 'library file name is ' + BiBTeXlibraryFileName

        elif o == '--download':
            downloadOpt = 1
            if a == '':
                a = './'
            elif a[-1] != '/':
                a = a + '/'
            downloadPath = os.path.expanduser(a)
            print 'download path is ' + downloadPath

        elif o == '-b':
            bibtexOpt = 1

        elif o == '-i':
            bibitemOpt = 1

        elif o == '-a':
            authorOpt = 1

        elif o == '-t':
            titleOpt = 1

        elif o == '-c':
            citeOpt = 1

        elif o == '-e':
            bibtexOpt = 1
            authorOpt = 1
            titleOpt = 1
            citeOpt = 1

        elif o == '-v':
            verboseOpt = 1

    if len(arguments) != 1:
        print 'you didn\'t specify a SPIRES reference; try \'spires.py -h\' for more information'
        sys.exit(0)
    else:
        ref=arguments[0]

    if len(options) == 0:
        bibtexOpt = 1
        authorOpt = 1
        titleOpt = 1
        citeOpt = 1

    print ref
    rType, ref = findRefType(ref)
    print rType, ref

    if verboseOpt:
        print 'the reference ' + ref + ' is a(n) ' + rType

    if (bibtexOpt + authorOpt + titleOpt + citeOpt + libraryOpt) > 0:
        BiBTeX = getBiBTeX(ref,rType)
        if 'no records' in BiBTeX:
            print BiBTeX
            sys.exit(0)

    if bibtexOpt:
        print BiBTeX

    if bibitemOpt:
        bibitem = getBibitem(ref,rType)
        print bibitem
        if 'no records' in bibitem:
            sys.exit(0)

    if authorOpt:
        author = extractauthor(BiBTeX)
        print author

    if titleOpt:
        title = extracttitle(BiBTeX)
        print title

    if (citeOpt + libraryOpt) > 0:
        cite = extractcite(BiBTeX)

    if citeOpt:
        print '\cite{' + cite + '}'

    if libraryOpt:
        updatelibrary(cite,BiBTeX,BiBTeXlibraryFileName)

    if downloadOpt:
        downloadeprint(ref,rType,downloadPath)