**Basics**:

This is a very basic scraper-spider for those html books where there's a table of contents page that links to a bunch of sub-pages with actual content (like the documentation for a bunch of libraries).

Dependencies: Beautiful Soup 4 on Python 2.7+ (including Python 3.x).
 
It assumes all content is vanilla html or at least can be accessed through vanilla html.  

**Usage**:

`python spideyscrape.py http://url/for/table_of_contents/toc.html`

Run script from terminal (etc.), then pass the script a url to the table of contents (ToC) page through the prompt you get (or via a command line argument, thanks to a kind contribution from @cclauss). This script scrapes every unique page linked from the ToC and concatenates the contents of their html bodies into one big html page.
 
The point is to save those things for offline reading, for planes etc.  It targets [Pythonista](http://omz-software.com/pythonista/) on iPad for optimum usefulness as offline reader, but also works fine on real computers.  On the iPad with Pythonista, probably the most useful way to invoke this script is by saving the following bookmarklet to Mobile Safari: 

    javascript:window.location='pythonista://spideyscrape.py?action=run&args='+window.location.href;

Then navigate to the ToC page you want to scrape and activate the bookmarklet.  

You can also `import` this as a module from some other script, in which case `spideyscrape.scrape('http://url/for/table_of_contents/toc.html')` will return the offline-capable HTML document.  This is mostly useful on iPad if you'd like to do something with the document other than save to the local filesystem, like pass it to [a Dropbox script](https://gist.github.com/mlgill/8311088) or [a document conversion script](http://wcm1.web.rice.edu/pandoc-on-ios.html) or the like.  

Speaking of Pythonista: as it turns out, it's a bit of a hassle to get html files out of its internal filesystem (as of 12-28-15).  The export action in the basic Pythonista action menu, for whatever reason, will only let you export files with a .py extension.  A cheap workaround to get the resulting html file in Dropbox, Google Drive, etc. anyway is to just temporarily slap a .py extension on the html file.  Then, by magic, the export menu will appear, and, thereafter, the good old iOS "open in" dialogue.

Alternatively, the easiest possible way to scrape something then get it right out of Pythonista is to download [this wrapper script](https://gist.github.com/paultopia/1103beb1980851a57977), then change your bookmarklet to point to scrapewrap.py rather than spideyscrape.py --- it will simply pop up an "open in" menu when scraping is complete, and you can send directly to Dropbox, PDF converter, or whatever.

Please only scrape content with copyright terms that permit copying.  Be nice to writers.  The primary intended use of this is to scrape documents offered to the public under licenses that permit copying, but which are often distributed in clueless formats (such as the documentation for many open-source software packages, which is often provided under Creative Commons or MIT licenses, permitting scraping).

**Contributing**: 

PRs are welcome.  Go wild.  :-)  However, I'd like to keep this runnable on both Pythonista on iOS and full-sized computers, so please don't rely on any Pythonista-specific libraries (like the clipboard module) without also providing a fallback for big machines; likewise please don't rely on any libraries that can't be installed in Pythonista without providing a more vanilla fallback.  

**Future**: 

1.  Down the road, I'd like to extend to make it possible to specify a crawl depth to recursively scrape to, and figure out some sensible way to order the sub-pages in that context. 

2.  It would also be cool to download and include images embedded in the original page.  Right now absolute url images should work but relative url images will probably break (not tested).  

**Terms**: 

The MIT License (MIT)
Copyright (c) 2015 Paul Gowder <http://paul-gowder.com>

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge,  publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do  so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR CPYRIGHT HOLDERS BE LIABLE  FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
