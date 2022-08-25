#! python3
'''
Version: 1.0
Developed Platform: Ubuntu Linux 20.04(Ubuntu 20.04.4 LTS)
Operation Platform: Debian Linux instances
Overview: pubCrawl.py is a python script designed to "scrape" the webpage of a provided URL for "actionable items"(URLs, redirects, resource references, etc).  
'''

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


#***INCOMPLETE BLOCK END***
#**STUB BLOCK END**

def userInputHandler(systemInput):
	'''
	Function for accepting & parsing user input from the console line.  Expected input is from the sys.argv format that comes from the console.
	'''
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


def __init__(self, inputURL):
	'''
	#!INCOMPLETE(Working to create pubCrawl class)
	'''
	self.inputURL = inputURL

def run():
	pass

def logHandler(loggingData, functionSource, logType = 'INFORMATION'):
	'''
	Function for gathering error information & recording it to a central location.
	'''
	logTime = datetime.datetime.now()
	fileName = logType + '_LOGS' + '.txt'
	fullFilePath = "./output/logs/" + fileName
	openMode = 'a+'
	writeFile = open(fullFilePath, openMode)
	writeFile.write(str(logTime) +  " (" + functionSource + "): " + loggingData + ";\n")
	writeFile.close()
	sys.exit("Log written to: " + fileName + "\npubCrawl.py Exiting.")

def fileNamer():
	'''
	Feature for generating a unique filename for each of the pubCrawl outputs.
	'''
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

def fileReader(fullFileName):
	'''
	Function for reading exterior files & returning their content to requestor.
	:param fullFileName: file location of data to be read & returned
	:type fullFileName: str
	:return: file data in str format
	'''
	try:
		with open(fullFileName) as file:
			data = file.read()
		return data
	except Exception as e:
		logHandler(e, 'fileReader', 'ERROR')

def dataParser(providedData, providedFileName, mode = 'w', fileType = ".txt"):
	'''
	Function for parsing the data that is found from the siteScraper & saving it to a txt file.
	'''
	try:
		fileName = providedFileName + fileType
		fileLocation = "./output/"
		fullFilePath = fileLocation + fileName
		with open(fullFilePath, mode) as fileWriter:
			for link in providedData:
				fileWriter.write('%s\n' % link)
		fileWriter.close()
	except Exception as e:
		logHandler(e, 'dataParser', 'ERROR')

def siteScraper(providedHTML):
	'''
	Function for scraping the URL provided by the user for usable information that is stored in the HTML(via hrefs).
	'''
	urlList = []
	try:
		for link in providedHTML.find_all(attrs={'href': re.compile("^https?://")}):
			print("\'href\': " + link.get('href'))
			urlList.append("%s" % link.get('href'))
		return(urlList)
	except Exception as e:
		logHandler(e, 'siteScraper', 'ERROR')

def siteConnector(workingURL):
	'''
	Function for negotiating & connecting to user supplied URL.
	'''
	try:
		response = requests.get(workingURL)
		return(response.text)
	except Exception as e:
		logHandler(e, 'siteConnector', 'ERROR')

def main():
	'''
	Function for the primary orchestration & running of the code
	'''
	workingURL = userInputHandler(sys.argv)
	targetResponse = siteConnector(workingURL)
	siteHTML = bs(targetResponse, 'html.parser')
	urlList = siteScraper(siteHTML)
	fileName = fileNamer()
	dataParser(urlList, fileName)


#*FUNCTION BLOCK END*

if __name__ == '__main__':
	main()
