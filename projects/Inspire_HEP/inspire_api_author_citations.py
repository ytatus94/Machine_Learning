# -*- coding: utf-8 -*-
#
# This file is part of INSPIRE.
# Copyright (C) 2014-2017 CERN.
#
# INSPIRE is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# INSPIRE is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with INSPIRE. If not, see <http://www.gnu.org/licenses/>.
#
# In applying this license, CERN does not waive the privileges and immunities
# granted to it by virtue of its status as an Intergovernmental Organization
# or submit itself to any jurisdiction.
#
# Comments, questions? Send email to feedback@inspirehep.net.
#

"""A script to use the INSPIRE API to do automated searching."""

from urllib2 import Request, urlopen, URLError
from bs4 import BeautifulSoup, Comment
import re
import sys
import time

#Set the defaults
START_YEAR = 1990
END_YEAR   = 1992
DEFAULT_AUTHOR = 'R.P.Feynman.1'
FUZZY_DATE_FACTOR = 2

def search_inspire(url):
    """Do an API search at INSPIRE."""
    request = Request(url)
    try:
        response = urlopen(request)
        result = response.read()
        soup = BeautifulSoup(result, "lxml")
        return soup
    except URLError, error:
        print 'URL =', url
        print 'No result. Got an error code:', error
        quit()

def get_result(search, number_only=False):
    """
       Takes an INSPIRE search and returns the list of INSPIRE recids.
    """
    number = '250'
    if number_only:
        number = '1'
    url = 'http://inspirehep.net/search?of=xm&rg=' + number + '&ot=001&p=' + \
          search.replace(' ', '+')
    soup = search_inspire(url)
    try:
        comments = soup.findAll(text=lambda text:isinstance(text, Comment))
        number_of_records = int(re.sub(r'\D', '', comments[0]))
    except IndexError:
        number_of_records = 0
    if number_only:
        return number_of_records

    recids = [int(recid.string) for recid in soup.findAll('controlfield')]

    if number_of_records > 250:
        jrec_number = 251
        while jrec_number < number_of_records:
            url_split = url + '&jrec=' + str(jrec_number)
            soup = search_inspire(url_split)
            for recid in soup.findAll('controlfield'):
                recids.append(int(recid.string))
            jrec_number += 250

    if number_of_records != len(recids):
        print "Problem: number of records = %d, number of recids = %d" % \
              (number_of_records, len(recids))
        print recids
        quit()
    return recids

def main(author):
    """Find the number of citations of an author per year."""

    search = 'find ea ' + author
    result = get_result(search)

    print """
    Citations per year of the %d papers of %s
    Time period: %d-%d
    """ % (len(result), author, START_YEAR, END_YEAR)

    print "{0:4} {1:6} {2:6}".format('Year', ' Cites', ' Total')
    sleep_time = 1
    big_total = 0
    for year in range(START_YEAR, END_YEAR):
        total = 0
        #FUZZY_DATE_FACTOR accounts for fuzziness in dates in INSPIRE
        year_next = year + FUZZY_DATE_FACTOR
        search = 'exactauthor:' + author + ' date:1900->' + str(year_next)
        for recid in get_result(search):
            time.sleep(sleep_time)
            search = 'refersto:recid:' + str(recid) + ' earliestdate:' + \
                     str(year)
            total += get_result(search, number_only=True)
        big_total += total
        print "{0:4} {1:6} {2:6}".format(year, total, big_total)
    print "{0:11} {2:6}".format('Total', '', big_total)

if __name__ == '__main__':
    try:
        main(str(sys.argv[1]))
    except IndexError:
        print "No author selected using", DEFAULT_AUTHOR
        print "To choose an author, run the command, e.g.,"
        print "python inspire_api.py j.j.schwinger.1"
        main(DEFAULT_AUTHOR)
    except KeyboardInterrupt:
        print 'Exiting'

