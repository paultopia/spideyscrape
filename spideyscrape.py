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

def getPage(url):	
	soup = makeSoup(url)
	if url[-5:] == '.html' or url[-4:] == '.htm':
		url = url[:url.rfind('/') + 1]
	return (soup, url)

def rootify(url): 
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
	return (base, root)

def filterLinks(root, link):
	# checks non-relative links to see if link contains domain of original page
	if link[:7] == 'http://' or link[:8] == 'https://':
		if root not in link:
			return False
	return True 

def transformLink(base, root, url, link):
	if link [:4] == 'http':
		return link
	if link[0] == '/':
		return base + root + link
	return url + link

def makeLinks(base, root, url, soup):
	links = filter(lambda x: 'mailto:' not in x, [stripAnchor(alink['href']) for alink in soup.find_all('a', href=True)])
	partials = filter(lambda x: filterLinks(root, x), [s for (i,s) in enumerate(links) if s not in links[0:i]])
	return [transformLink(base, root, url, x) for x in partials if x] 

def makeTexts(uniques, soup):
	texts = [getBody(makeSoup(aurl)) for aurl in uniques]
	texts.insert(0, getBody(soup))
	boilerplate = '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"><html><head><meta http-equiv="Content-Type" content="text/html; charset=UTF-8"></head><body>'
	return boilerplate + '<br><br>'.join(texts) + '</html></body>'

def savePage(texts):
	from time import gmtime, strftime
	filename = 'scrape' + str(strftime("%Y%m%d%H%M%S", gmtime())) + '.html'
	with open(filename, 'w') as outfile:
		outfile.write(texts)
	return filename

def scrape(start):
	soup, url = getPage(start)
	base, root = rootify(url)
	uniques = makeLinks(base, root, url, soup)
	return makeTexts(uniques, soup)

if __name__ == "__main__":
	start = raw_input('URL to crawl: ')
	html = scrape(start)
	filename = savePage(html)
	print 'Scraping complete! Output saved as: ' + filename
