# wrapper for pythonista on iOS to scrape a document, pop up an open in dialogue, 
# allow you to do something with it, then silently delete the original from pythonista 
# sandboxed internal filesystem to avoid clutter.

import sys
import spideyscrape
import console
import os

args = sys.argv[1:]  # see if the user gave us a command line argument
start = args[0] if args else raw_input('URL to crawl: ')
html = spideyscrape.scrape(start)
filename = spideyscrape.savePage(html)
console.open_in(filename)
os.remove(filename)
