#! python3

'''
Overview: pubCrawl.py is a python script designed to "scrape" the webpage of a provided URL for "actionable items"(URLs, redirects, resource references, etc).  
'''

#*IMPORT BLOCK BEGIN*
from bs4 import BeautifulSoup as bs
from selenium import webdriver
from selenium.webdriver.firefox.options import Options as firefoxOptions
from urllib.parse import urlparse
import datetime
import json
import os.path
import random
import requests
import re
import string
import sys
#*IMPORT BLOCK END*

#*FUNCTION BLOCK BEGIN*
#**STUB BLOCK BEGIN**
#***FUTURE VERSION BLOCK BEGIN***

#***FUTURE VERSION BLOCK END***
	
#**STUB BLOCK END**

def userInputHandler(systemInput,defaultURL = "https://www.instagram.com/",testMode = False,argValue=" "):
	'''
	Function for accepting & parsing user input from the console line.  Will return a default value(defaultURL) if no value is given by the user.
	:param systemInput: Input Data
	:type systemInput: str
	:param defaultURL: URL provided to the function to indicate the URL that is to be returned if no value is supplied by the user during initialization of the program
	:type defaultURL: str
	:param testMode: Testing value; value to inform the function whether it is operating in a function testing scenario or not.  Default is set to "False" to help assure that the function operates with the assumption of a live environment unless instructed otherwise. 
	:type testMode: boolean
	:param argValue: Testing value; value to be provided when testing the function that provides a value in place of "sys.argv[1]" which will not be supplied when running unit tests from test_pubcrawl.py
	:type argValue: str
	:return: str
	'''
	
	try:
		if(len(systemInput) <= 1):
			cleanedURL = defaultURL
		else:
			if testMode == False:
				argValue = sys.argv[1]
			else:
				argValue = argValue
			providedURL = argValue
			urlCleaner = pubCrawl(providedURL)
			cleanedURL = urlCleaner.userInputParser(providedURL)
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

	def siteRepCheck(self):
		'''
		#!STUB(Future Feature)
		Function for integrating API calls on malicious site checkers(Brightcloud, Virustotal, etc) to automatically check provided URLs for malicious activity/poor community reputation.
		'''
		pass

	#**FUTURE VERSION BLOCK END***
	#*STUB BLOCK END**

	#Lambda designed to read str pool of data & output it as a dictionary.  Expected output: dict
	dataPoolSorter = lambda self, data : json.loads(data)

	#Lambda designed to provide ease of operating system filepath construction.  Expected output: str
	pathCombiner = lambda self, firstFileValue, secondFileValue : os.path.join(firstFileValue, secondFileValue)

	def __init__(self, inputURL,scanDepth = 0, testMode = False):
		'''
		Function for initializing the pubCrawl class when it is called.
		:param inputURL: URL submitted for scraping by the program
		:type inputURL: str
		:param testMode: value to inform the class if it is operating under testing conditions or not
		:type testMode: boolean
		'''
		self.inputURL = inputURL
		self.scanDepth = scanDepth
		self.testMode = testMode

	def depthScanManager(self,workingURL, scanDepth = 1, targetType = 'HYBRIDSITE'):
		'''
		#!STUB(Future Feature)
		Function for managing & orchestrating the depth that URLs will be scanned for further URLs user defined depths of scraping on found resources.
		:param workingURL: Intial URL that is to be scrapped by pubCrawl.
		:type workingURL: str
		:param targetType: Value that indicates the type of site that is going to be scraped.  DYNAMICSITE indicates a site that should be scraped for only URLs that arrive after scripts are allowed to load.  STATICSITE indicates a site that should only be scraped for URLS before scripts are allowed to load.  HYBRIDSITE indicates a site that should be scraped for URLS both before & after scripts are allowed to load.
		:type targetType: str
		:param intDepth: value that defines how far down the program should look for URLs within the URLs that it does find. Will be adjusted & implemented in later version.
		:type intDepth: int
		:return: list of URLs
		'''

		masterList = []
		scanningList = []
		resultList = []
		try:
			for depth in range(scanDepth):
				if depth == 0:
					#urlList = self.scrapeSite(workingURL,targetType)
					scanningList.append(workingURL)
				else:
					scanningList = []
					for url in resultList:
						scanningList.append(url)
					resultList = []

				for url in scanningList:
					if url in masterList:
						continue
					else:
						urlList = self.scrapeSite(url,targetType)
						for url in urlList:
							if url in resultList:
								continue
							else:
								resultList.append(url)
						print(f"resultsList Length: {len(resultList)}")
						print(f"masterList Length: {len(masterList)}")

				#for url in urlList:
					#resultList.append(url)

			masterList = set.union(set(resultList),set(masterList))
			return(masterList)
		except Exception as e:
			self.logHandler(e, 'depthScanManager', 'ERROR')

	def userInputParser(self,providedURL):
		'''
		Function for attempting to clean up user's input & parsing it properly for future connection/handling.
		:param providedURL: URL passed to the function to be evaluated & parsed to assure that the working URL is constructed in a predictable, more absolute way
		:type providedURL: str
		:return: str
		'''

		print(f"userInputParser's providedURL: {providedURL}")
		try:
			parsedURL = urlparse(providedURL)
			if parsedURL[1] != '':	#Check to determine if the value in parsedURL's netloc(parsedURL[1]) is populated.
				checkedURL = self.urlNetLocCreator(parsedURL)
			else:
				checkedURL = self.schemeIterator(parsedURL)

			return checkedURL

		except Exception as e:
			self.logHandler(e, 'userInputParser', 'ERROR')

	def schemeIterator(self,providedRelativeURL, schemeOptions = ['https','http']):
		'''
		Function for attempting to regulate & massage user inputted URLs for better functionality, primarily while working with the requests library.  	
		:param providedRelativeURL: Value to define the URL that will have different schemes applied to it to assure that it will lead to a functional URL.
		:type providedRelativeURL: str
		:param schemeOptions: list of options to be iterated through to be applied to the providedRelativeURL if no schemes have already been applied to providedRelativeURL when it was submitted.
		:type schemeOptions: list of strings that define URL schemes to be tested. This will be in order to assure that the URL provided will resolve properly.
		:return str:
		'''

		try:
			for scheme in schemeOptions:
				urlToCheck = f"{scheme}://{providedRelativeURL[2]}/" #Line that reconstructs the value in providedURL's path to add the current tested scheme to form "{SCHEME}://{PATH}"({http}://{scanme.nmap.org}" excluding curley braces)
				try: #Block to test the relative provided URL with the applied scheme
					request = requests.get(urlToCheck)
					checkedURL = urlToCheck
					break
				except:
					continue
			
			return checkedURL

		except Exception as e:
			self.logHandler(e, 'schemeIterator', 'ERROR')

	def urlNetLocCreator(self, providedURL):
		'''
		Function for taking strings provided by calling function, evaluating, & processing it so that netlocations(netloc) can be seperated more easily from paths(path).
		:param providedURL: Value to define the URL that will be evaluated & rebuilt so it more cleanly provides an absolute URL instead of a relative URL.
		:type providedURL: str
		:return: str
		'''

		try:
			checkedURL = f"{providedURL[0]}://{providedURL[1]}/" #Line that reconstructs the provided URL to include only the URL's scheme(parsedURL[0]) & it's netloc(parsedURL[1]) in form "{SCHEME}://{NETLOC}/"("{http}://{scanme.nmap.org}/" excluding curley braces)
			return checkedURL

		except Exception as e:
			self.logHandler(e, 'urlNetLocCreator', 'ERROR')

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
			logHandlerReturn = self.logHandler(e, 'scrapeDynamicSite', 'ERROR')
			testResolve = self.testHandler(logHandlerReturn,e)

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
			logHandlerReturn = self.logHandler(e, "scrapeStaticSite", 'ERROR')
			testResolve = self.testHandler(logHandlerReturn,e)

	def logHandler(self, loggingData, functionSource, logType = 'INFORMATION',writeLocation1 = "output",writeLocation2 = "logs"):
		'''
		Function for gathering error information & recording it to a central location.
		:param loggingData: Exception data provided by the calling function that is to be recorded.
		:type loggingData: str
		:param functionSource: Name of the function that is calling logHandler() so it can be recorded for logs.
		:type functionSource: str
		:param logType: Exception type provided by calling function to be recorded.
		:type logType: str
		:param writeLocation1: String indicating the parent folder of where logHandler() should write its log results
		:type writeLocation1: str
		:param writeLocation2: String indicating the child folder of where logHandler() should write its log results
		:type writeLocation2: str
		'''
		testMode = self.testMode
		if testMode == False:
			loggingData = str(loggingData)
			functionSource = str(functionSource)
			logType = str(logType)
			logTime = datetime.datetime.now()
			logTime = str(logTime)
			fileName = logType + '_LOGS' + '.txt'
			logFilePath = self.pathCombiner(writeLocation1,writeLocation2)
			fullFilePath = self.pathCombiner(logFilePath,fileName)
			openMode = 'a+'
			with open(fullFilePath, openMode) as writeFile:
				writeFile.write(logTime +  " (" + functionSource + "): " + loggingData + ";\n")
			if logType != "TESTING":
				print(f"During runtime {functionSource} met a logable event type {logType}")
				print(f"Log written to: {fullFilePath}")
			return None
		else:
			return loggingData

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
			logHandlerReturn = self.logHandler(e, "fileNamer", 'ERROR')
			testResolve = self.testHandler(logHandlerReturn,e)

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
			logHandlerReturn = self.logHandler(e, 'fileReader', 'ERROR')
			testResolve = self.testHandler(logHandlerReturn,e)

	def dataParser(self, targetSite, providedData, providedFileName, parentFolder = "output", fileType = ".txt"):
		'''
		Function for parsing the data that is found from the staticSiteScraper & saving it to a data file.
		:param targetSite: Value to indicate what site is being scraped for URLs.
		:type targetSite: str
		:param providedData: Data provided by calling function that will be written to the file
		:type providedData: str
		:param providedFileName: File name that is provided by calling function that the data will be written to.
		:type providedFileName: str
		:param parentFolder: Value that indicates what folder data should be written to.
		:type parentFolder: str
		:param fileType: the filetype of the file that the data will be written to.
		:type fileType: str
		'''
		mode = 'w'
		try:
			fileName = providedFileName + fileType
			fullFilePath = self.pathCombiner(parentFolder,fileName)
			with open(fullFilePath, mode) as fileWriter:
				fileWriter.write(f'URL Scraped: {targetSite}\n')
				for link in providedData:
					fileWriter.write(f'{link}\n')
		except Exception as e:
			logHandlerReturn = self.logHandler(e, 'dataParser', 'ERROR')
			testResolve = self.testHandler(logHandlerReturn,e)
			return(testResolve)

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
			logHandlerReturn = self.logHandler(e, "siteConnector", 'ERROR')
			testResolve = self.testHandler(logHandlerReturn,e)

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
			logHandlerReturn = self.logHandler(e, 'dynamicConnectorFirefox', 'ERROR')
			testResolve = self.testHandler(logHandlerReturn,e)

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
			driver.close()
			return foundURLs

		except Exception as e:
			logHandlerReturn = self.logHandler(e, 'dynamicSiteGrabber', 'ERROR')
			testResolve = self.testHandler(logHandlerReturn,e)

	def testHandler(self,logHandlerValue,exceptionValue):
		'''
		Function for assisting the class to determine what steps to complete based on the values it recieves
		:param logHandlerValue: Value that may be passed to the fuction that was supplied by logHandler() if the class is running in testMode
		:type logHandlerValue: str
		:param exceptionValue: Value that is supplied to the function & returned if it is determined that the logHandlerValue contains nothing(None)
		:type exceptionValue: TypeError
		:return: TypeError
		'''
		if logHandlerValue == None:
			sys.exit("Exiting")
		else:
			return exceptionValue

	def scrapeSite(self, workingURL, targetType='HYBRIDSITE'):
		'''
		Function for activating & operating the pubCrawl class in the anticipated order & manner if the user is planning on performing both static & dynamic scraping.
		:param workingURL: URL that will be scraped for more URLs
		:type workingURL: str
		:param targetType: Value that indicates the type of site that is going to be scraped.  DYNAMICSITE indicates a site that should be scraped for only URLs that arrive after scripts are allowed to load.  STATICSITE indicates a site that should only be scraped for URLS before scripts are allowed to load.  HYBRIDSITE indicates a site that should be scraped for URLS both before & after scripts are allowed to load.
		:type targetType: str
		:return: List of URLs
		'''

		targetType = targetType.upper()
		urlList = []
		print(f"URL to be scraped: {workingURL}")
		if(targetType == 'HYBRIDSITE'):
			staticURLList = self.scrapeStaticSite(workingURL)
			dynamicURLList = self.scrapeDynamicSite(workingURL)
			uniqueURLSet = set.union(set(staticURLList),set(dynamicURLList))
		elif(targetType == 'DYNAMICSITE'):
			uniqueURLList = self.scrapeDynamicSite(workingURL)
			uniqueURLSet = set(uniqueURLList)
		elif(targetType == 'STATICSITE'):
			uniqueURLList = self.scrapeStaticSite(workingURL)
			uniqueURLSet = set(uniqueURLList)
		else:
			sys.exit(f'{targetType} is not a valid targetType value. Try again with one of the following:\n\n\tHYBRIDSITE\n\tDYNAMICSITE\n\tSTATICSITE\n')

		for url in uniqueURLSet:
			urlList.append(url)

		return(urlList)


	def scrapingController(self,targetType = 'HYBRIDSITE',scrapeDepth = 1):
		'''
		!(STUB: Work in Progress) 
		Function for dictating how & when a URL should be scraped.  Acts as a contril function for the pubCrawl class.
		:param targetType: Value that indicates the type of site that is going to be scraped.  DYNAMICSITE indicates a site that should be scraped for only URLs that arrive after scripts are allowed to load.  STATICSITE indicates a site that should only be scraped for URLS before scripts are allowed to load.  HYBRIDSITE indicates a site that should be scraped for URLS both before & after scripts are allowed to load.
		:type targetType: str
		:param scrapeDepth: Variable that dictates how many times the URLs should be iterated through.  Default value is 1 to represent that at the very least the inputURL should be scraped
		:type scrapeDepth: int

		'''
		workingURL = self.inputURL
		#urlList = self.scrapeSite(workingURL,targetType)
		urlList = self.depthScanManager(workingURL, 2)
		print(type(urlList))
		print(urlList)

		fileName = self.fileNamer()
		self.dataParser(workingURL,urlList, fileName)
		print(f"Results stored to {fileName}")


def main():
	'''
	Function for the primary orchestration & running of the code
	'''

	workingURL = userInputHandler(sys.argv)
	pub_crawl = pubCrawl(workingURL)
	pub_crawl.scrapingController()

#*FUNCTION BLOCK END*

if __name__ == '__main__':
	main()
