# wrapper for pythonista on iOS to scrape a document, pop up an open in dialogue, 
# allow you to do something with it, then silently delete the original from pythonista 
# sandboxed internal filesystem to avoid clutter.

# use with bookmarklet: 
# javascript:window.location='pythonista://scrapewrap.py?action=run&args='+window.location.href;

import sys
import spideyscrape
import console
import os

print('scraping ' + str(sys.argv[1]))
html = spideyscrape.scrape(sys.argv[1])
filename = spideyscrape.savePage(html)
console.open_in(filename)
os.remove(filename)
