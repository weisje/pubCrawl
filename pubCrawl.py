#! python3 (3.9.5)
# Version: 1.0
# Developed Platform: Ubuntu Linux 20.04(Ubuntu 20.04.4 LTS)
# Operation Platform: Debian Linux instances
# Overview: pubCrawl.py is a python script designed to "scrape" the webpage of a provided URL for "actionable items"(URLs, redirects, resource references, etc).  

#*IMPORT BLOCK BEGIN*
from bs4 import BeautifulSoup as bs
import random
import requests
import re 
import sys

#*IMPORT BLOCK END*

#*FUNCTION BLOCK BEGIN*
#**STUB BLOCK BEGIN**
#***FUTURE VERSION BLOCK BEGIN***

#!STUB(Version 2.0 Feature): Function for attempting to clean up user's input & parsing it properly for future connection/handling.
def userInputParser(providedURL):
	return providedURL

#STUB(Version 2.0 Feature): Function for managing & orchestrating the recursive function of user defined depths of scraping on found resources.
def recursiveDepthManager(intDepth = 1):
	if(intDepth == 1):
		pass

#STUB(Version 3.0 Feature): Function for integrating API calls on malicious site checkers(Brightcloud, Virustotal, etc) to automatically check provided URLs for malicious activity/poor community reputation.
def siteRepCheck():
	pass

#***FUTURE VERSION BLOCK END***
#***INCOMPLETE BLOCK BEGIN***
#!STUB(Incomplete): Feature for generating a filename for each of the pubCrawl outputs.
def fileNamer():
	pass

#!STUB(Incomplete): Function for scraping the URL provided by the user for usable information that is stored in the HTML(via hrefs).
def siteScraper(providedHTML):
	for link in providedHTML.find_all(attrs={'href': re.compile("^https?://")}):
		print("\'href\': " + link.get('href'))

#!STUB(Incomplete): Function for parsing the data that is found from the siteScraper & saving it to a txt file.
def dataParser():
	pass


#***INCOMPLETE BLOCK BEGIN***
#**STUB BLOCK END**

#Function for negotiating & connecting to user supplied URL.
def siteConnector(workingURL):
	response = requests.get(workingURL)
	return(response.text)

#Function for accepting & parsing user input from the console line.  Expected input is from the sys.argv format that comes from the console.  
def userInputHandler(systemInput):
	defaultURL = "http://scanme.nmap.org/"
	if(len(systemInput) <= 1):
		cleanedURL = defaultURL
	else:
		providedURL = sys.argv[1]
		cleanedURL = userInputParser(providedURL)
	return(cleanedURL)

#main function: Function for the primary orchestration & running of the code
def main():
	workingURL = userInputHandler(sys.argv)
	targetResponse = siteConnector(workingURL)
	siteHTML = bs(targetResponse, 'html.parser')
	urlList = siteScraper(siteHTML)

#*FUNCTION BLOCK END*

if __name__ == '__main__':
	main()
