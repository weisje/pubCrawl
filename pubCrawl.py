#! python3
'''
Version: 1.2
Developed Platform: Ubuntu Linux 20.04(Ubuntu 20.04.4 LTS)
Operation Platform: Debian Linux instances
Overview: pubCrawl.py is a python script designed to "scrape" the webpage of a provided URL for "actionable items"(URLs, redirects, resource references, etc).  
'''

#*IMPORT BLOCK BEGIN*
from bs4 import BeautifulSoup as bs
from selenium import webdriver
from selenium.webdriver.firefox.options import Options as firefoxOptions
import datetime
import json
import os.path
import random
import requests
import re
import string
import sys
#*IMPORT BLOCK END*

#*LAMBDA BLOCK BEGIN*
#**INCOMPLETE BLOCK BEGIN**
#**INCOMPLETE BLOCK END**

#*LAMBDA BLOCK END*

#*FUNCTION BLOCK BEGIN*
#**STUB BLOCK BEGIN**
#***FUTURE VERSION BLOCK BEGIN***
def userInputParser(providedURL):
	'''
	#!STUB(Version 2.0 Feature)
	Function for attempting to clean up user's input & parsing it properly for future connection/handling.
	'''
	try:
		return providedURL
	except Exception as e:
		logHandler(e, 'userInputParser', 'ERROR')

#***FUTURE VERSION BLOCK END***
#**STUB BLOCK END**

def userInputHandler(systemInput):
	'''
	Function for accepting & parsing user input from the console line.  Will return a default value(defaultURL) if no value is given by the user.
	:param systemInput: Input Data
	:type systemInput: str
	:return: url as str
	'''
	defaultURL = "https://www.instagram.com/"
	try:
		if(len(systemInput) <= 1):
			cleanedURL = defaultURL
		else:
			providedURL = sys.argv[1]
			cleanedURL = userInputParser(providedURL)
		return(cleanedURL)
	except Exception as e:
		logger = pubCrawl(systemInput)
		logger.logHandler(e, 'userInputHandler', 'ERROR')

class pubCrawl:
	'''
	Class designed scrape target site/URL's code for visible URLs.  It will then take the results & write them to a text file for review. 
	'''
	#*STUB BLOCK BEGIN**
	#**FUTURE VERSION BLOCK BEGIN***
	def recursiveDepthManager(self,intDepth = 1):
		'''
		#!STUB(Version 2.0 Feature)
		Function for managing & orchestrating the recursive function of user defined depths of scraping on found resources.
		'''
		if(intDepth == 1):
			pass

	def siteRepCheck(self):
		'''
		#!STUB(Version 3.0 Feature)
		Function for integrating API calls on malicious site checkers(Brightcloud, Virustotal, etc) to automatically check provided URLs for malicious activity/poor community reputation.
		'''
		pass

	#**FUTURE VERSION BLOCK END***
	#*STUB BLOCK END**

	#Lambda designed to read str pool of data & output it as a dictionary.  Expected output: dict
	dataPoolSorter = lambda self, data : json.loads(data)

	#Lambda designed to provide ease of operating system filepath construction.  Expected output: str
	pathCombiner = lambda self, firstFileValue, secondFileValue : os.path.join(firstFileValue, secondFileValue)

	def __init__(self, inputURL):
		'''
		Function for initializing the pubCrawl class when it is called.
		'''
		self.inputURL = inputURL

	def scrapeDynamicSite(self,inputURL):
		'''
		Function designed to gather & return URLs from websites that require activation before they can be properly scraped for URLs.
		:param inputURL: URL of the target to be scraped
		:type inputURL: str
		:return: list
		'''
		try:
			dynamicURLList = self.dynamicSiteGrabber(self.dynamicConnectorFirefox(),inputURL)
			return(dynamicURLList)
		except Exception as e:
			self.logHandler(e, 'scrapeDynamicSite', 'ERROR')

	def scrapeStaticSite(self,inputURL):
		'''
		Function designed to gather & return URLs from websites that are static & have HTML available to be scraped without dynamic code activitation.
		:param inputURL: URL of the target to be scraped
		:type inputURL: str
		:return: list
		'''
		try:
			targetResponse = self.siteConnector(inputURL)
			siteHTML = bs(targetResponse, 'html.parser')
			staticURLList = self.staticSiteScraper(siteHTML)
			return staticURLList
		except Exception as e:
			self.logHandler(e, 'scrapeStaticSite', 'ERROR')

	def logHandler(self, loggingData, functionSource, logType = 'INFORMATION'):
		'''
		Function for gathering error information & recording it to a central location.
		:param loggingData: Exception data provided by the calling function that is to be recorded.
		:type loggingData: str
		:param functionSource: Name of the function that is calling logHandler() so it can be recorded for logs.
		:type functionSource: str
		:param logType: Exception type provided by calling function to be recorded.
		:type logType: str
		'''
		loggingData = str(loggingData)
		functionSource = str(functionSource)
		logType = str(logType)
		logTime = datetime.datetime.now()
		logTime = str(logTime)
		fileName = logType + '_LOGS' + '.txt'
		logFilePath = self.pathCombiner("output","logs")
		fullFilePath = self.pathCombiner(logFilePath,fileName)
		openMode = 'a+'
		with open(fullFilePath, openMode) as writeFile:
			writeFile.write(logTime +  " (" + functionSource + "): " + loggingData + ";\n")
		print(f"During runtime {functionSource} met a logable event type {logType}")
		sys.exit(f"Log written to: {fullFilePath}\npubCrawl.py Exiting.")

	def fileNamer(self):
		'''
		Feature for generating a unique filename for each of the pubCrawl outputs.
		:return: str in format ADJECTIVENOUN####
		'''
		adjectiveFilePath = self.pathCombiner("fileNames","adjectives.txt")
		adjectiveDataPool = self.fileReader(adjectiveFilePath)
		adjectives = self.dataPoolSorter(adjectiveDataPool)
		nounFilePath = self.pathCombiner("fileNames","nouns.txt")
		nounDataPool = self.fileReader(nounFilePath)
		nouns = self.dataPoolSorter(nounDataPool)

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
			self.logHandler(e, 'filleNamer', 'ERROR')

	def fileReader(self, fullFileName):
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
			self.logHandler(e, 'fileReader', 'ERROR')

	def dataParser(self, targetSite, providedData, providedFileName, fileType = ".txt"):
		'''
		Function for parsing the data that is found from the staticSiteScraper & saving it to a data file.
		:param providedData: Data provided by calling function that will be written to the file
		:type providedData: str
		:param providedFileName: File name that is provided by calling function that the data will be written to.
		:type providedFileName: str
		:param fileType: the filetype of the file that the data will be written to.
		:type fileType: str
		'''
		mode = 'w'
		try:
			fileName = providedFileName + fileType
			fullFilePath = self.pathCombiner("output",fileName)
			with open(fullFilePath, mode) as fileWriter:
				fileWriter.write(f'URL Scraped: {targetSite}\n')
				for link in providedData:
					fileWriter.write(f'{link}\n')
		except Exception as e:
			self.logHandler(e, 'dataParser', 'ERROR')

	def staticSiteScraper(self, providedHTML):
		'''
		Function for scraping the URL provided by the user for usable information that is stored in the HTML(via hrefs).
		:param providedHTML: HTML provided by the calling function that will be searched for available URLs
		:type providedHTML: str
		:return: modified list
		'''
		urlList = []
		try:
			for link in providedHTML.find_all(attrs={'href': re.compile("^https?://")}):
				#print("\'href\': " + link.get('href'))
				urlList.append("%s" % link.get('href'))
			return(urlList)
		except Exception as e:
			self.logHandler(e, 'staticSiteScraper', 'ERROR')

	def siteConnector(self, workingURL):
		'''
		Function for negotiating & connecting to user supplied URL.
		:param workingURL: URL provided by calling function that will be connected to by siteConnector()
		:type workingURL: str
		:return: str
		'''
		try:
			response = requests.get(workingURL)
			return(response.text)
		except Exception as e:
			self.logHandler(e, 'siteConnector', 'ERROR')

	def dynamicConnectorFirefox(self):
		'''
	Function for creating a Selenium web browser driver in Firefox
		:return: selenium.webdriver.firefox.webdriver.WebDriver
		'''
		try:
			options = firefoxOptions()
			options.add_argument("--headless") #This line is to assure that a browser window does not open on the user's screen.  This line can be commented out if you want to open n number of browser windows where n is equal to the number of URLs being scraped.
			driver = webdriver.Firefox(options=options)
			return driver
		except Exception as e:
			self.logHandler(e, 'dynamicConnectorFirefox', 'ERROR')

	def dynamicSiteGrabber(self,providedDriver,providedURL,searchingElement1 = 'tag name',searchingElement2 = 'a',retrievingAttribute = 'href'):
		'''
		Function for running & grabbing HTML elements from a site after it has been summoned.  Function then searches for elements on the page to be returned.
		:param providedDriver: Driver that has been generated via selenium for calling on the website
		:type providedDriver: selenium.webdriver.firefox.webdriver.WebDriver
		:param providedURL: Provided URL that will be summoned & scraped for information
		:type providedURL: str
		:param searchingElement1: The type of element that is to be searched for in resulting HTML once the site has been summoned.
		:type searchingElement1: str
		:param searchingElement2: Subtype of element that is to be searched for in resulting HTML when the site has been summoned.
		:type searchingElement2: str
		:param retrievingAttribute: Type of element that will be scanned for & retrieved to be returned to the calling function
		:type retrievingAttribute: str
		:return: list
		'''
		try:
			foundURLs = []
			driver = providedDriver
			driver.get(providedURL)
			allLinks = driver.find_elements(searchingElement1,searchingElement2)
			for elem in allLinks:
				foundURLs.append(elem.get_attribute(retrievingAttribute))
			return foundURLs
		except Exception as e:
			self.logHandler(e, 'dynamicSiteGrabber', 'ERROR')

	def scrapeSite(self,targetType='HYBRIDSITE'):
		'''
		Function for activating & operating the pubCrawl class in the anticipated order & manner if the user is planning on performing both static & dynamic scraping.
		'''
		workingURL = self.inputURL
		targetType = targetType.upper()
		print(f"URL to be scraped: {workingURL}")
		if(targetType == 'HYBRIDSITE'):
			staticURLList = self.scrapeStaticSite(workingURL)
			dynamicURLList = self.scrapeDynamicSite(workingURL)
			uniqueURLList = set.union(set(staticURLList),set(dynamicURLList))
		elif(targetType == 'DYNAMICSITE'):
			uniqueURLList = self.scrapeDynamicSite(workingURL)
			uniqueURLList = set(uniqueURLList)
		elif(targetType == 'STATICSITE'):
			uniqueURLList = self.scrapeStaticSite(workingURL)
			uniqueURLList = set(uniqueURLList)
		else:
			sys.exit(f'{targetType} is not a valid targetType value. Try again with one of the following:\n\n\tHYBRIDSITE\n\tDYNAMICSITE\n\tSTATICSITE\n')

		fileName = self.fileNamer()
		self.dataParser(workingURL,uniqueURLList, fileName)
		print(f"Results stored to {fileName}")

def main():
	'''
	Function for the primary orchestration & running of the code
	'''

	workingURL = userInputHandler(sys.argv)
	pub_crawl = pubCrawl(workingURL)
	pub_crawl.scrapeSite()

#*FUNCTION BLOCK END*

if __name__ == '__main__':
	main()
