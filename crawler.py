#!/usr/bin/python
# -*- coding: utf-8 -*-

from urllib2 import urlopen, Request
from urlparse import urlparse, urljoin
import re

class Parser():
    def getLinks(self, url):
        headers = { 'User-Agent': 'Hugobot/1.0.1 (+http://hucruz.com)' }
        req = Request(url, headers= headers)
        return map(lambda t: urljoin(url,t),re.findall('''href=["'](.[^"']+)["']''', urlopen(req).read(), re.I))

def spider(url, maxVisits):
    queue = [url]
    count = 0
    visited = []
    while count < maxVisits and queue != []:
        url = queue.pop(0)
        if url in visited:
            continue
        visited.append(url)
        count += 1
        try:
            print "Indexing:", url
            parser = Parser()
            links = parser.getLinks(url)
            queue += links
        except Exception as e:
            print url," Error:", e

if __name__ == "__main__":
    try:
        url = sys.argv[1]
        maxVisits = 30
        spider(url, maxVisits)
    except:
        print "Usage: python",sys.argv[0],"[url]"
