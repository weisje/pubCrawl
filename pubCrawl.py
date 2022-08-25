#! python3
# Version: 1.0
# Developed Platform: Ubuntu Linux 20.04(Ubuntu 20.04.4 LTS)
# Operation Platform: Debian Linux instances
# Overview: pubCrawl.py is a python script designed to "scrape" the webpage of a provided URL for "actionable items"(URLs, redirects, resource references, etc).  

#*IMPORT BLOCK BEGIN*
from bs4 import BeautifulSoup as bs
import json
import random
import requests
import re
import string
import sys
import datetime

#*IMPORT BLOCK END*

#*LAMBDA BLOCK BEGIN*
#**INCOMPLETE BLOCK BEGIN**

#!INCOMPLETE(Being Tested): Lambda designed to read str pool of data & output it as a dictionary.  Expected output: dict.
dataPoolSorter = lambda data : json.loads(data)

#**INCOMPLETE BLOCK END**
#*LAMBDA BLOCK END*

#*FUNCTION BLOCK BEGIN*
#**STUB BLOCK BEGIN**
#***FUTURE VERSION BLOCK BEGIN***

#!STUB(Version 2.0 Feature): Function for attempting to clean up user's input & parsing it properly for future connection/handling.
def userInputParser(providedURL):
	try:
		return providedURL
	except Exception as e:
		logHandler(e, 'userInputParser', 'ERROR')

#STUB(Version 2.0 Feature): Function for managing & orchestrating the recursive function of user defined depths of scraping on found resources.
def recursiveDepthManager(intDepth = 1):
	if(intDepth == 1):
		pass

#STUB(Version 3.0 Feature): Function for integrating API calls on malicious site checkers(Brightcloud, Virustotal, etc) to automatically check provided URLs for malicious activity/poor community reputation.
def siteRepCheck():
	pass

#***FUTURE VERSION BLOCK END***
#***INCOMPLETE BLOCK BEGIN***

#!INCOMPLETE(Being Tested): Function for reading exterior files & returning their value to requestor. Expected output: str.
def fileReader(fullFileName):
	try:
		with open(fullFileName) as file:
			data = file.read()
		return data
	except Exception as e:
		logHandler(e, 'fileReader', 'ERROR')

#!STUB(Being Tested): Function for gathering error information & recording it to a central location.
def logHandler(loggingData, functionSource, logType = 'INFORMATION'):
	logTime = datetime.datetime.now()
	fileName = logType + '_LOGS' + '.txt'
	fullFilePath = "./output/logs/" + fileName
	openMode = 'a+'
	with open(fullFilePath, openMode) as writeFile:
		writeFile.write(str(logTime) +  " (" + functionSource + "): " + loggingData + ";\n")
	sys.exit("Log written to: " + fileName + "\npubCrawl.py Exiting.")

#***INCOMPLETE BLOCK BEGIN***
#**STUB BLOCK END**

#Function for parsing the data that is found from the siteScraper & saving it to a txt file.
def dataParser(providedData, providedFileName, mode = 'w', fileType = ".txt"):
	try:
		fileName = providedFileName + fileType
		fileLocation = "./output/"
		fullFilePath = fileLocation + fileName
		with open(fullFilePath, mode) as fileWriter:
			for link in providedData:
				fileWriter.write('%s\n' % link)
	except Exception as e:
		logHandler(e, 'dataParser', 'ERROR')
#Function for scraping the URL provided by the user for usable information that is stored in the HTML(via hrefs).
def siteScraper(providedHTML):
	urlList = []
	try:
		for link in providedHTML.find_all(attrs={'href': re.compile("^https?://")}):
			print("\'href\': " + link.get('href'))
			urlList.append("%s" % link.get('href'))
		return(urlList)
	except Exception as e:
		logHandler(e, 'siteScraper', 'ERROR')

#Function for negotiating & connecting to user supplied URL.
def siteConnector(workingURL):
	try:
		response = requests.get(workingURL)
		return(response.text)
	except Exception as e:
		logHandler(e, 'siteConnector', 'ERROR')

#Function for accepting & parsing user input from the console line.  Expected input is from the sys.argv format that comes from the console.  
def userInputHandler(systemInput):
	defaultURL = "http://scanme.nmap.org/"
	try:
		if(len(systemInput) <= 1):
			cleanedURL = defaultURL
		else:
			providedURL = sys.argv[1]
			cleanedURL = userInputParser(providedURL)
		return(cleanedURL)
	except Exception as e:
		logHandler(e, 'userInputHandler', 'ERROR')

#Feature for generating a unique filename for each of the pubCrawl outputs.
def fileNamer():
	filePath = "./fileNames/"
	adjectiveFile = "adjectives.txt"
	adjectiveFilePath = filePath + adjectiveFile
	adjectiveDataPool = fileReader(adjectiveFilePath)
	adjectives = dataPoolSorter(adjectiveDataPool)
	nounFile = "nouns.txt"
	nounFilePath = filePath + nounFile
	nounDataPool = fileReader(nounFilePath)
	nouns = dataPoolSorter(nounDataPool)
  
	try:
		adjectiveKey = random.choice(list(adjectives))
		adjectivePool = adjectives[adjectiveKey]
		adjectiveSelection = random.choice(list(adjectivePool)).capitalize()
		nounKey = random.choice(list(nouns))
		nounPool = nouns[nounKey]
		nounSelection = random.choice(list(nounPool)).capitalize()
		randomDigits = ''.join(random.choice(string.digits) for _ in range(4))
		fileName = adjectiveSelection + nounSelection + randomDigits
		return(fileName)
	except Exception as e:
		logHandler(e, 'filleNamer', 'ERROR')


#main function: Function for the primary orchestration & running of the code
def main():
	
	workingURL = userInputHandler(sys.argv)
	targetResponse = siteConnector(workingURL)
	siteHTML = bs(targetResponse, 'html.parser')
	urlList = siteScraper(siteHTML)
	fileName = fileNamer()
	dataParser(urlList, fileName)


#*FUNCTION BLOCK END*

if __name__ == '__main__':
	main()
