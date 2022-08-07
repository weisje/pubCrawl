#! python3 (3.9.5)
# Version: 1.0
# Developed Platform: Ubuntu Linux 20.04(Ubuntu 20.04.4 LTS)
# Operation Platform: Debian Linux instances
# Overview: pubCrawl.py is a python script designed to "scrape" the webpage of a provided URL for "actionable items"(URLs, redirects, resource references, etc).  

#*IMPORT BLOCK BEGIN*
from bs4 import BeautifulSoup as bs
import requests
import re 
import sys

#*IMPORT BLOCK END*

#*FUNCTION BLOCK BEGIN*
#**STUB BLOCK BEGIN**
#***FUTURE VERSION BLOCK BEGIN***

#STUB(Version 2.0 Feature): Function for managing & orchestrating the recursive function of user defined depths of scraping on found resources.
def recursiveDepthManager():
	pass

#STUB(Version 3.0 Feature): Function for integrating API calls on malicious site checkers(Brightcloud, Virustotal, etc) to automatically check provided URLs for malicious activity/poor community reputation.
def siteRepCheck():
	pass

#***FUTURE VERSION BLOCK END***
#***INCOMPLETE BLOCK BEGIN***
#!STUB(Incomplete): Feature for generating a filename for each of the pubCrawl outputs.
def fileNamer():
	pass

#!STUB(Incomplete): Function for accepting & parsing user input from the console line.  Expected input is from the sys.argv format that comes from the console.  
def userInputHandler(systemInput):
	defaultURL = "http://scanme.nmap.org/"
	print(len(sys.argv))
	if(len(systemInput) <= 1):
		providedURL = defaultURL
	else:
		providedURL = sys.argv[1]

	return(providedURL)

#!STUB(Incomplete): Function for attempting to clean up user's input & parsing it properly for future connection/handling.
def userInputParser(providedURL):
	pass

#!STUB(Incomplete): Function for negotiating & connecting to user supplied URL.
def siteConnector():
	pass

#!STUB(Incomplete): Function for scraping the URL provided by the user for usable information that is stored in the HTML(via hrefs).
def siteScraper():
	pass

#!STUB(Incomplete): Function for parsing the data that is found from the siteScraper & saving it to a txt file.
def dataParser():
	pass

#!STUB(Incomplete): main function: Function for the primary orchestration & running of the code
def main():
	workingURL = (userInputHandler(sys.argv))
	print(workingURL)
	print(type(workingURL))

#***INCOMPLETE BLOCK BEGIN***
#**STUB BLOCK END**
#*FUNCTION BLOCK END*

if __name__ == '__main__':
	main()