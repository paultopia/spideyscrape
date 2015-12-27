from bs4 import BeautifulSoup as BS
import urllib 

def clearJunk(BSobj):
	[s.extract() for s in BSobj(['style', 'script'])]

def makeSoup(url):
	r = urllib.urlopen(url)
	soup = BS(r)
	clearJunk(soup)
	return soup
	
def getBody(BSobj):
	return ' '.join([str(i) for i in BSobj.find('body').find_all(recursive=False)])
	
def stripAnchor(url):
	badness = url.find('#')
	if badness != -1:
		return url[:badness]
	return url
	
url = raw_input('URL to crawl: ')
soup = makeSoup(url)
if url[-5:] == '.html' or url[-4:] == '.htm':
	url = url[:url.rfind('/') + 1]

# a quick bit of link validation follows
if url[:7] == 'http://':
	base = 'http://'
	chopped = url[7:]
elif url[:8] == 'https://':
	base = 'https://'
	chopped = url[8:]
else: 
	base = 'http://'
	chopped = url
if chopped.find('/') != -1:
	root = chopped[:chopped.find('/')]
else: 
	root = chopped

def filterLinks(root, link):
	# checks non-relative links to see if link contains domain of original page
	if link[:7] == 'http://' or link[:8] == 'https://':
		if root not in link:
			return False
	return True 

links = filter(lambda x: 'mailto:' not in x, [stripAnchor(alink['href']) for alink in soup.find_all('a', href=True)])
partials = filter(lambda x: filterLinks(root, x), [s for (i,s) in enumerate(links) if s not in links[0:i]])

def transformLink(base, root, url, link):
	if link [:4] == 'http':
		return link
	if link[0] == '/':
		return base + root + link
	return url + link

uniques = [transformLink(base, root, url, x) for x in partials if x] 

texts = [getBody(makeSoup(aurl)) for aurl in uniques]
texts.insert(0, getBody(soup))
from time import gmtime, strftime
filename = 'scrape' + str(strftime("%Y%m%d%H%M%S", gmtime())) + '.html'
with open(filename, 'w') as outfile:
	outfile.write('<br><br>'.join(texts))

print 'Scraping complete! Output saved as: ' + filename
