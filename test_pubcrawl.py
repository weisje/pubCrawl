#! python3
'''
Overview: Script for providing test scenarios for pubCrawl.py version 1  
This script will provide means for the following tests:
-Unit Tests: For testing each of the functions featured in the pubCrawl() class.
	-Requirements:
		-One(1) positive test per function
		-One(1) negative test per function
-Software Tests: For testing that the pubCrawl() class is fulfilling requirements as stated in the design document.
	-Requirements:
		-One(1)	positive user input/system output cycle
		-One(1) negative user input cycle
'''

#*IMPORT SECTION BEGIN*
from bs4 import BeautifulSoup as bs
from selenium import webdriver
from selenium.webdriver.firefox.options import Options as firefoxOptions
import json
import os.path
import pubCrawl as PCT
import sys
#*IMPORT SECTION END*

dummySite = 'http://www.example.com/' #placeholder site for test functions that do not require a working website to run.

#*TESTING TOOL SECTION BEGIN*
def resultDisplayer(testType,testResult,reason):
	'''
	Function for accepting data from the different testing functions, reading what they are trying to accomplish, & printing the results it is given in a clear manner.
	:param testType: input to tell the function if it is dealing with a POSITIVE test type or NEGATIVE test type
	:type testType: str
	:param testResult: input to inform the function the results of the test that it is being fed 
	:type testResult: int
	:param reason: input that provides reasoning for the output of the testResult variable
	:type : str
	'''
	if testType.upper() == 'POSITIVE':
		if testResult == 1:
			print("Result: PASS")
		else:
			print(f"Result: FAIL\nReason: {reason}")
	else:
		if testResult == 0:
			print("Result: PASS")
		else:
			print(f"Result: FAIL\nReason: {reason}")
	print("="*50 + "\n")

#*TESTING TOOL SECTION END*

#*UNIT TEST SECTION BEGIN*

#**LAMBDA TEST SECTION BEGIN**
def dataPoolSorterTestClass(testSite,inputTestData):
	'''
	Function to test the pubCrawl.dataPoolSorter() lambda to assure that it
		-Accepts data pool of str objects
		-Returns a value that is listed as a dictionary(dict)
	:param inputTestData: Data that is to be tested against 
	:type inputTestData: str
	:return: str,str
	'''
	try:
		pub_crawl_dataPoolSorterTestClass = PCT.pubCrawl(testSite,True)
		results = pub_crawl_dataPoolSorterTestClass.dataPoolSorter(inputTestData)
		if(type(results) == dict):
			dataPoolSorterTestClassResult = "PASS"
			reason = "dataPoolSorter() returned an output with the class 'dict'"
		else:
			dataPoolSorterTestClassResult = "FAIL"
			reason = "dataPoolSorter() did not return an output with class 'dict'"
	except Exception as e:
			dataPoolSorterTestClassResult = "FAIL"
			reason = f"dataPoolSorter() returned exception: {e}"
	return dataPoolSorterTestClassResult,reason

def dataPoolSorterTestValue(testSite, inputTestData):
	'''
	Function to test the pubCrawl.dataPoolSorter() lambda to assure that it
		-Accepts data pool of str objects
		-Returns anticipated output value from input value
	:param inputTestData: Data that is to be tested against 
	:type inputTestData: str
	:param testSite: Website being fed into the function in order to initialize pubCrawl() class
	:type testSite: str
	:return: str,str
	'''
	try:	
		pub_crawl_dataPoolSorterTestValue = PCT.pubCrawl(testSite,True)
		dataPoolSorterOutput = pub_crawl_dataPoolSorterTestValue.dataPoolSorter(inputTestData)
		internalConversion = json.loads(inputTestData)
		if(dataPoolSorterOutput == internalConversion):
			dataPoolSorterTestValueResult = "PASS"
			reason = "dataPoolSorter() returned an output value that matched the anticipated output value." 
		else:
			dataPoolSorterTestValueResult = "FAIL"
			reason = "dataPoolSorter() did not return an output value that matched the anticipated output value."
	except Exception as e:
			dataPoolSorterTestValueResult = "FAIL"
			reason = f"dataPoolSorter() returned exception: {e}"
	return dataPoolSorterTestValueResult,reason


	print(f"Result: {dataPoolSorterTestValueResult}")
	print(f"dataPoolSorter input values: {inputTestData}")
	print(f"dataPoolSorter output values: {dataPoolSorterOutput}")

def pathCombinerTestPath(testSite,inputTestData1,inputTestData2):
	'''
	Function to test the pubCrawl.pathCombiner() lambda to assure that it:
		-Accepts str values for filepath construction
		-Returns antcipated filepaths in the form of strings
	:param inputTestData: Data that is to be tested against 
	:type inputTestData: str
	:param testSite: Website being fed into the function in order to initialize pubCrawl() class
	:type testSite: str
	:return: str,str
	'''
	try:
		pub_crawl_pathCombinerTest = PCT.pubCrawl(testSite,True)
		pathCombinerTestOutput = pub_crawl_pathCombinerTest.pathCombiner(inputTestData1,inputTestData2)
		internalConversion = os.path.join(inputTestData1,inputTestData2)
		if pathCombinerTestOutput == internalConversion:
			pathCombinerTestPathResult = "PASS"
			reason = f"pathCombiner() returned expected filepath output: '{pathCombinerTestOutput}'"
		else:
			pathCombinerTestPathResult = "FAIL"
			reason = f"pathCombiner() output did not match anticipated output\nExpected Value: {internalConversion}\nActual Value: {pathCombinerTestOutput}"
	except Exception as e:
		pathCombinerTestPathResult = "FAIL"
		reason = f"pathCombiner() returned exception: {e}"
	return pathCombinerTestPathResult,reason

def pathCombinerPositiveTests(testSite):
	'''
	Function for running tests on pubCrawl.pathCombiner() lambda with an anticipated positive/PASS outcome.
	:param testSite: Website being fed into the function in order to initialize pubCrawl() class
	:type testSite: str
	'''
	inputTestData1 = "Folder"
	inputTestData2 = "Subfolder"

	print("TEST: pathCombiner() positive value test")
	positiveValueFilepathTestResult, reason = pathCombinerTestPath(testSite,inputTestData1,inputTestData2)
	if positiveValueFilepathTestResult == 'PASS':
		print(f'Result: {positiveValueFilepathTestResult}')
	else:
		print(f'Result: {positiveValueFilepathTestResult}\n{positiveValueFilepathTestResult}Reason: {reason}')
	print("="*50 + "\n")

def pathCombinerNegativeTests(testSite):
	'''
	Function for running tests on pubCrawl.pathCombiner() lambda with an anticipated negative/FAIL outcome.
	:param testSite: Website being fed into the function in order to initialize pubCrawl() class
	:type testSite: str
	'''
	inputTestData1 = 42
	inputTestData2 = "Subfolder"

	print("TEST: pathCombiner() negative value test")
	positiveValueFilepathTestResult, reason = pathCombinerTestPath(testSite,inputTestData1,inputTestData2)
	if positiveValueFilepathTestResult == 'PASS':
		print(f'Result: FAIL\nReason: {reason}')
	else:
		print(f'Result: PASS')
	print("="*50 + "\n")

def dataPoolSorterNegativeTests(testSite):
	'''
	Function for running tests on pubCrawl.dataPoolSorter() lambda with an anticipated negative/FAIL outcome.
	:param testSite: Website being fed into the function in order to initialize pubCrawl() class
	:type testSite: str
	'''
	negativeValueInputTestData = "{'Colors':['Red','Orange'], 'Equines':['horse', 'stallion']}"
	negativeClassInputTestData = 42

	print("TEST: dataPoolSorter() negative value input test")
	negativeValueInputTest,reason = dataPoolSorterTestValue(testSite, negativeValueInputTestData)
	if negativeValueInputTest == 'FAIL':
		print('Result: PASS')
	else: 
		print('Result: FAIL\nReason: dataPoolSorter() accepted malformed input value & processed it unexpectedly')
	print("="*50 + "\n")
	print("TEST: dataPoolSorter() negative class input test")
	negativeClassInputTest, reason = dataPoolSorterTestClass(testSite, negativeClassInputTestData)
	if negativeClassInputTest == 'FAIL':
		print("Result: PASS")
	else:
		print(f"Result: FAIL\nReason: dataPoolSorter() accepted a stringified dict input value({negativeClassInputTestData}) & processed it unexpectedly")
	print("="*50 + "\n")

def dataPoolSorterPositiveTests(testSite):
	'''
	Function for running tests on pubCrawl.dataPoolSorter() lambda with an anticipated positive/PASS outcome.
	:param testSite: Website being fed into the function in order to initialize pubCrawl() class
	:type testSite: str	
	'''
	inputTestData = '{"Colors":["Red","Orange"], "Equines":["horse", "stallion"]}'
	print("TEST: dataPoolSorter() positive class test" )
	classTestResult,reason = dataPoolSorterTestClass(testSite,inputTestData)
	if classTestResult == 'PASS':
		print(f'Result: {classTestResult}')
	else:
		print(f'Result: {classTestResult}\n{classTestResult} Reason: {reason}')
	print("="*50 + "\n")
	print("TEST: dataPoolSorter() positive value test")
	valueTestResult,reason = dataPoolSorterTestValue(testSite,inputTestData)
	if valueTestResult == 'PASS':
		print(f'Result: {valueTestResult}')
	else:
		print(f'Result: {valueTestResult}\n{valueTestResult} Reason: {reason}')
	print("="*50 + "\n")

#**LAMBDA TEST SECTION END**

#**FUNCTION TEST SECTION BEGIN**
def scrapeStaticSiteTest(inputURL):
	'''
	Function for interacting with the pubCrawl.py scrapeStaticSite() function apathetically & determines if scrapeStaticSite returns a list type object or not.
	:param inputURL: URL to be fed into scrapeStaticSite() & processed 
	:type inputURL: str
	'''
	pub_crawl_scrapeStaticSiteTest = PCT.pubCrawl(inputURL,True)
	try:
		scrapeStaticSiteTest = pub_crawl_scrapeStaticSiteTest.scrapeStaticSite(inputURL)
		if type(scrapeStaticSiteTest) == list:
			scrapeStaticSiteTestResult = 1
			reason = "scrapeStaticSite() returned value with type list"
		else:
			scrapeStaticSiteTestResult = 0
			reason = f"scrapeStaticSite() returned value with type {type(scrapeDynamicSiteTest)} not list"
	except Exception as e:
		scrapeStaticSiteTestResult = 0
		reason = f"{e}"

	return scrapeStaticSiteTestResult, reason

def logHandlerTest(inputURL,loggingData,functionSource,writeLocation1,writeLocation2):
	'''
	Function for interacting with the pubCrawl.py logHandler() function apathetically.  Test attempts to write to the provided location & returns a 1 if successful or a 0 if there is an error.
	:param inputURL: URL for initalizing the pubCrawl.pubCrawl() class.
	:type inputURL: str
	:param loggingData: Data to activate required attribute of the function(Can be dummy data, not important to test)
	:type loggingData: str
	:param functionSource: Information on what function is calling the logHandler() function (Can be dummy data, not important to test)
	:type functionSource: str
	:param writeLocation1: parent folder where the logHandler() function will be looking to write provided loggingData & functionSource
	:type writeLocation1: str
	:param writeLocation2: child folder where the logHandler() function will be looking to write provided loggingData & functionSource
	:type writeLocation2: str
	:return: int, str
	'''
	pub_crawl_logHandlerTest =  PCT.pubCrawl(inputURL)
	logType = "TESTING"
	try:
		logHandlerTest = pub_crawl_logHandlerTest.logHandler(loggingData,functionSource, logType, writeLocation1,writeLocation2)
		logHandlerTestResult = 1
		reason = f"logHandler wrote to {os.path.join(writeLocation1,writeLocation2)} successfully."
	except Exception as e:
		logHandlerTestResult = 0
		reason = f"{e}"
	return logHandlerTestResult,reason

def fileNamerTest(inputURL):
	'''
	Function for interacting with the pubCrawl.py fileNamer() function apathetically & determines if fileNamer() returns a str type object or not
	:param inputURL: URL to be fed in to initialize the pubCrawl.pubCrawl() class 
	:type inputURL: str
	:return: int,str
	'''
	pub_crawl_fileNamerTest = PCT.pubCrawl(inputURL,True)
	try:
		fileNamerTest = pub_crawl_fileNamerTest.fileNamer()
		if type(fileNamerTest) == str:
			fileNamerTestResult = 1
			reason = f"fileNamer() returned {type(fileNamerTest)} as expected"
	except Exception as e:
		fileNamerTestResult = 0
		reason = f"{e}"

	return fileNamerTestResult,reason

def fileReaderTest(inputURL,inputFileName):
	'''
	Function for interacting with the pubCrawl.py fileReader() function apathetically & determines if fileReader() returns a str type object or not
	:param inputURL: URL to be fed in to initialize the pubCrawl.pubCrawl() class 
	:type inputURL: str
	:return: int,str
	'''
	pub_crawl_fileReaderTest = PCT.pubCrawl(inputURL,True)
	try:
		fileReaderTest = pub_crawl_fileReaderTest.fileReader(inputFileName)
		if type(fileReaderTest) == str:
			fileReaderTestResult = 1
			reason = f"fileReader() returned {type(fileReaderTest)} as expected"
		else:
			fileReaderTestResult = 0
			reason = f"fileReader() did not return expected class type\nExpected: str\nActual: {type(fileReaderTest)}"
	except Exception as e:
		fileReaderTestResult = 0
		reason = f"{e}"
	return fileReaderTestResult,reason

def dataParserTest(inputURL,providedData,providedFileName,parentFolder):
	'''
	Function for interacting with the pubCrawl.py dataParser() function apathetically, attempts to write data to a file provided, & returns whether the write was successful or not.
	:param inputURL: URL to be fed in to initialize the pubCrawl.pubCrawl() class & provide data to the function for logging. 
	:type inputURL: str
	:param providedData: Data to be written to the file
	:type providedData: set
	:param providedFileName: Name of the file where the data should be written
	:type providedFileName: str
	:param parentFolder: name of the folder that will store the file being written to.
	:type parentFolder: str
	:return: int,str
	'''
	
	pub_crawl_dataParserTest = PCT.pubCrawl(inputURL,True)
	try:
		dataParserTest = pub_crawl_dataParserTest.dataParser(inputURL,providedData,providedFileName,parentFolder)
		if type(dataParserTest) == TypeError:
			testResult = 0
			reason = f"dataParser() returned error: {dataParserTest}"
		else:
			testResult = 1
			reason = f"dataParser() was able to successfully write provided data to the file"
	except Exception as e:
		testResult = 0
		reason = f"{e}"

	return testResult, reason

def staticSiteScraperTest(inputURL,providedData,anticipatedResults):
	'''
	Function for interacting with the pubCrawl.py staticSiteScraper() function apathetically & determines if staticSiteScraper()) returns the same value as the list of anticipated URLs or not
	:param inputURL: URL to be fed in to initialize the pubCrawl.pubCrawl() class 
	:type inputURL: str
	:param providedData: Data to be ran through staticSiteScraper() to search for URLs
	:type providedData: bs4.beautifulSoup
	:param anticipatedResults: List of URLs that is expected to be found when staticSiteScraper() is ran against providedData
	:type anticipatedResults: list
 	:return: int,str
	'''
	pub_crawl_staticSiteScraperTest = PCT.pubCrawl(inputURL,True)
	try:
		staticSiteScraperTest = pub_crawl_staticSiteScraperTest.staticSiteScraper(providedData)
		if staticSiteScraperTest == anticipatedResults:
			staticSiteScraperTestResult = 1
			reason = "staticSiteScraper() returned the same list of URLs as was anticipated"
		else:
			staticSiteScraperTestResult	= 0
			reason = f"staticSiteScraper() returned the an unanticipated list of URLs\nExpected Value: {anticipatedResults}\nReceived Value: {staticSiteScraperTest}"
	except Exception as e:
		staticSiteScraperTestResult = 0
		reason = f"{e}"

	return staticSiteScraperTestResult, reason

def siteConnectorTest(inputURL,testURL):
	'''
	Function for interacting with the pubCrawl.py siteConnector() function apathetically & determines if siteConnector() returns a class value of str or not.
	:param inputURL: URL to be fed in to initialize the pubCrawl.pubCrawl() class 
	:type inputURL: str
	:param testURL: URL provided to test the siteConnector() function to determine if it can return a str value.
	:type testURL: str
	:return: int,str
	'''
	pub_crawl_siteConnectorTest = PCT.pubCrawl(inputURL,True)
	try:
		siteConnectorTest  = pub_crawl_siteConnectorTest.siteConnector(testURL)
		if type(siteConnectorTest) == str:
			testResult = 1
			reason = "siteConnector() returned value class str as anticipated"
		else:
			testResult = 0
			reason = f"siteConnector() did not return anticipated value class\nExpected: class str\nActual:{type(siteConnectorTest)}"
	except Exception as e:
		testResult = 0
		reason = f"{e}"

	return testResult, reason

def dynamicSiteGrabberTest(inputURL,testURL,providedDriver = None,searchingElement1='tag name',searchiningElement2='a',retrievingAttribute = 'href'):
	'''
	Function for interacting with the pubCrawl.py dynamicSiteGrabber() function apathetically & determines if dynamicSiteGrabber() returns a str type object or not
	:param inputURL: URL to be fed in to initialize the pubCrawl.pubCrawl() class 
	:type inputURL: str
	:param testURL: URL to attempt to dynamically grab HTML code from
	:type testURL: str
	:param providedDriver: Driver initializer that allows for the generation of a Firefox instance for grabbing dynamic sites. If not provided then it will default to generating its own via "pubCrawl.pubCrawl.dynamicConnectorFirefox()"
	:type providedDriver: selenium.webdriver.firefox.webdriver.WebDriver
	:param searchingElement1: First string type to look for within the HTML found while grabbing the dynamic site
	:type searchingElement1: str
	:param searchingElement2: subelement to be searched for within the HTML found while grabbing the dynamic site
	:type searchingElement2: str
	:param retrievingAttribute: attribute type to be retrieved from the HTML that is foun while grabbing the dynamic site
	:type retrievingAttribute: str
	:return: int,str
	'''	
	pub_crawl_dynamicSiteGrabberTest = PCT.pubCrawl(inputURL,True)
	if providedDriver == None:
		providedDriver = pub_crawl_dynamicSiteGrabberTest.dynamicConnectorFirefox()
	try:
		dynamicSiteGrabberTest = pub_crawl_dynamicSiteGrabberTest.dynamicSiteGrabber(providedDriver, testURL, searchingElement1,searchiningElement2,retrievingAttribute)
		if type(dynamicSiteGrabberTest) == list:
			testResult = 1
			reason = "dynamicSiteGrabber() returned class type list as anticipated"
		else:
			testResult = 0
			reason = f"dynamicSiteGrabeer() did not return expected class type\nExpected: <class 'list'>\nActual: {type(dynamicSiteGrabberTest)}"
	except Exception as e:
		testResult = 0
		reason = f"{e}"

	return testResult,reason

def userInputHandlerPositiveTests(testSite):
	'''
	Function for running tests on pubCrawl.py's userInputHandler() function with an anticipated positive/PASS outcome.
	:param testSite: Website being fed into the function to provide value to input into the called function
	:type testSite: str	
	'''

	testSwitch = 1
	print("TEST: userInputHandler() positive no supplied value test")
	inputTestData1 = ""
	systemTestData = testSite
	defaultURL = "https://www.facebook.com/"
	userInputHandlerTest1 = PCT.userInputHandler(inputTestData1,defaultURL,True)
	try:
		if userInputHandlerTest1 == defaultURL:
			userInputHandlerTestResult1 = "PASS"
			reason = ""
		else:
			userInputHandlerTestResult1 = "FAIL"
			reason = f"userInputHandler() did not return anticipated value\nExpected:{defaultURL}\nActual:{userInputHandlerTest1}"
	except Exception as e:
		userInputHandlerTestResult1 = 'FAIL'
		reason = f"userInputHandler() returned exception {e}"
	print(f"Result: {userInputHandlerTestResult1}\n{reason}")
	print("="*50 + "\n")

	print("TEST: userInputHandler() positive supplied value test")
	inputTestData2 = testSite
	defaultURL2 = "https://www.example.com/" 
	try:
		userInputHandlerTest2 = PCT.userInputHandler(inputTestData2,defaultURL2,True,inputTestData2)
		if userInputHandlerTest2 == inputTestData2:
			userInputHandlerTestResult2 = "PASS"
			reason = ""
		elif userInputHandlerTest2 == defaultURL:
			userInputHandlerTestResult2 = "FAIL"
			reason = f"userInputHandler() returned defaultURL: {defaultURL2} instead of inputTestData2: {inputTestData2}"
		else:
			userInputHandlerTestResult2 = "FAIL"
			reason = f"userInputHandler() did not return anticipated value\nExpected:{inputTestData2}\nActual:{userInputHandlerTest2}"
	except Exception as e:
		userInputHandlerTestResult1 = 'FAIL'
		reason = f"userInputHandler() returned exception {e}"

	print(f"Result: {userInputHandlerTestResult2}\n{reason}")
	print("="*50 + "\n")

def userInputHandlerNegativeTests(testSite):
	'''
	Function for running tests on pubCrawl.py's userInputHandler() function with an anticipated negative/FAIL outcome.
	:param testSite: Website being fed into the function to provide value to input into the called function
	:type testSite: str	
	'''

	testSwitch = 0
	print("TEST: userInputHandler() negative supplied value test")
	defaultURL1 = testSite
	testURL = 1
	try:
		userInputHandlerTest1 = PCT.userInputHandler(testURL, defaultURL1)
		if userInputHandlerTest1 == defaultURL:
			userInputHandlerTestResult1 = 'FAIL'
			reason = f"userInputHandler() returned : {userInputHandlerTest1}"
		else:
	 		userInputHandlerTestResult1 = 'PASS'
	 		reason = ""
	except Exception as e:
		userInputHandlerTestResult1 = 'PASS'
		reason = ""
	print(f"Result: {userInputHandlerTestResult1}\n{reason}")
	print("="*50 + "\n")

def scrapeDynamicSitePositiveTest(testSite):
	'''
	Function for running tests on pubCrawl.py's scrapeDynamicSite() function with an anticipated positive/PASS outcome.
	:param testSite: Website being fed into the function to provide value to input into the called function
	:type testSite: str	
	'''
	'''
	print("TEST: ")
	print("="*50 + "\n")
	'''
	print("TEST: scrapeDynamicSite() positive supplied value test")
	pub_crawl_scrapeDynamicSiteTest = PCT.pubCrawl(testSite)
	#results = pub_crawl_scrapeDynamicSiteTestClass.scrapeDynamicSite(testSite)
	try:
		scrapeDynamicSiteTest = pub_crawl_scrapeDynamicSiteTest.scrapeDynamicSite(testSite)
		if type(scrapeDynamicSiteTest) == list:
			scrapeDynamicSiteTestResult = "PASS"
			reason = ""
		else:
			scrapeDynamicSiteTestResult = "FAIL"
			reason = f"scrapeDynamicSite() returned {type(scrapeDynamicSiteTestResult)} not list."
	except Exception as e:
		scrapeDynamicSiteTestResult = "FAIL"
		reason = f"{e}"

	print(f"Result: {scrapeDynamicSiteTestResult}\n{reason}")
	print("="*50 + "\n")

def scrapeDynamicSiteNegativeTest(testSite):
	'''
	Function for running tests on pubCrawl.py's scrapeDynamicSite() function with an anticipated negative/FAIL outcome.
	:param testSite: URL being fed in to initialize the pubCrawl() class
	:type testSite: str	
	'''
	'''
	print("TEST: scrapeDynamicSite() ")
	print("="*50 + "\n")
	'''
	print("TEST: scrapeDynamicSite() negative supplied value test")
	testingValue = "https://scanme.nmap.org/"
	pub_crawl_scrapeDynamicSiteTest = PCT.pubCrawl(testSite,True)
	try:
		scrapeDynamicSiteTest = pub_crawl_scrapeDynamicSiteTest.scrapeDynamicSite(testingValue)
		if type(scrapeDynamicSiteTest) == list:
			scrapeDynamicSiteTestResult = "FAIL"
			reason = f"scrapeDynamicSite() returned {type(scrapeDynamicSiteTestResult)}"
		else:
			scrapeDynamicSiteTestResult = "PASS"
			reason = f""
			pass
	except Exception as e:
		scrapeDynamicSiteTestResult = "PASS"
		reason = f""
		pass

	print(f"Result: {scrapeDynamicSiteTestResult}\n{reason}")
	print("="*50 + "\n")

def scrapeStaticSitePositiveTest(testSite):
	'''
	Function for running tests on pubCrawl.py's scrapeStaticSite() function with an anticipated positive/PASS outcome.
	:param testSite: Website being fed into the function to provide value to input into the called function
	:type testSite: str	
	'''

	testType = "POSITIVE"

	print("TEST: scrapeStaticSiteTest() positive provided input")
	testResult,reason = scrapeStaticSiteTest(testSite)
	resultDisplayer(testType,testResult,reason)

def scrapeStaticSiteNegativeTest():
	'''
	Function for running tests on pubCrawl.py's scrapeStaticSite() function with an anticipated negative/FAIL outcome.
	'''
	testType = "NEGATIVE"
	testingValue = 1

	print("TEST: scrapeStaticSiteTest() negative provided input")
	testResult,reason = scrapeStaticSiteTest(testingValue)
	resultDisplayer(testType,testResult,reason)

def logHandlerPositiveTest(testSite):
	'''
	Function for running tests on pubCrawl.py's logHandler() function with an anticipated positive/PASS outcome.
	:param testSite: Website being fed into the function to provide value to input into the called function
	:type testSite: str	
	'''
	testType = "POSITIVE"
	loggingData = "Data To Be Logged"
	functionSource = "logHandlerPositiveTest"
	writeLocation1 = "testingDataFolder"
	writeLocation2 = "output"

	print("TEST: logHandlerTest() positive provided input")
	testResult,reason = logHandlerTest(testSite,loggingData,functionSource,writeLocation1,writeLocation2)
	resultDisplayer(testType,testResult,reason)
	
def logHandlerNegativeTest(testSite):
	'''
	Function for running tests on pubCrawl.py's logHandler() function with an anticipated negative/FAIL outcome.
	:param testSite: URL being fed in to initialize the pubCrawl() class
	:type testSite: str	
	'''
	testType = "NEGATIVE"
	loggingData = None
	functionSource = "logHandlerNegativeTest"
	writeLocation1 = "dev"
	writeLocation2 = "null"

	print("TEST: logHandlerTest() negative provided input")
	testResult,reason = logHandlerTest(testSite,loggingData,functionSource,writeLocation1,writeLocation2)
	resultDisplayer(testType,testResult,reason)

def fileNamerPositiveTest(testSite):
	'''
	Function for running tests on pubCrawl.py's fileNamer() function with an anticipated positive/PASS outcome.
	:param testSite: Website being fed into the function to provide value to input into the called function
	:type testSite: str	
	'''
	testType = "POSITIVE"

	print("TEST: fileNamer() positive provided input")
	testResult,reason = fileNamerTest(testSite)
	resultDisplayer(testType,testResult,reason)

def fileReaderPositiveTest(testSite):
	'''
	!STUB 	Function for running tests on pubCrawl.py's fileReader() function with an anticipated positive/PASS outcome.
	:param testSite: Website being fed into the function to provide value to input into the called function
	:type testSite: str	
	'''
	testType = "POSITIVE"
	readLocation1 = "testingDataFolder"
	readLocation2 = "fileReaderTestData"
	inputFileName = os.path.join(readLocation1,readLocation2)

	print("TEST: fileReader() positive provided input")
	testResult,reason = fileReaderTest(testSite,inputFileName)
	resultDisplayer(testType,testResult,reason)
	
def fileReaderNegativeTest(testSite):
	'''
	Function for running tests on pubCrawl.py's fileReader() function with an anticipated negative/FAIL outcome.
	:param testSite: URL being fed in to initialize the pubCrawl() class
	:type testSite: str	
	'''
	testType = 'NEGATIVE'
	readLocation1 = "testingDataFolder"
	readLocation2 = "noFile"

	print("TEST: fileReader() negative provided input")
	inputFileName = os.path.join(readLocation1,readLocation2)
	testResult,reason = fileReaderTest(testSite,inputFileName)
	resultDisplayer(testType,testResult,reason)

def dataParserPositiveTest(testSite):
	'''
	Function for running tests on pubCrawl.py's dataParser() function with an anticipated positive/PASS outcome.
	:param testSite: Website being fed into the function to provide value to input into the called function
	:type testSite: str	
	'''
	
	testType = "POSITIVE"
	providedData = {"Red","Blue","Green"}
	providedFileName = "positiveWrite"
	parentFolder = "testingDataFolder"

	print("TEST: dataParser() positive input")
	testResult,reason = dataParserTest(testSite,providedData,providedFileName,parentFolder)
	resultDisplayer(testType,testResult,reason)

def dataParserNegativeTest(testSite):
	'''
	Function for running tests on pubCrawl.py's dataParser() function with an anticipated negative/FAIL outcome.
	:param testSite: URL being fed in to initialize the pubCrawl() class
	:type testSite: str	
	'''
	testType = "NEGATIVE"
	providedData = {"Red","Blue","Green"}
	providedFileName = None
	parentFolder = None

	print("TEST: dataParser() negative input")
	testResult,reason = dataParserTest(testSite,providedData,providedFileName,parentFolder)
	resultDisplayer(testType,testResult,reason)

def staticSiteScraperPositiveTest(testSite):
	'''
	Function for running tests on pubCrawl.py's staticSiteScraper() function with an anticipated positive/PASS outcome.
	:param testSite: Website being fed into the function to provide value to input into the called function
	:type testSite: str	
	'''
	testType = "POSITIVE"
	anticipatedResults = ['https://www.google-analytics.com/analytics.js', 'https://nmap.org/', 'https://nmap.org/book/man.html', 'https://nmap.org/book/install.html', 'https://nmap.org/download.html', 'https://nmap.org/changelog.html', 'https://nmap.org/book/', 'https://nmap.org/docs.html', 'https://npcap.com/', 'https://npcap.com/guide/', 'https://npcap.com/guide/npcap-devguide.html#npcap-api', 'https://npcap.com/#download', 'https://npcap.com/changelog', 'https://seclists.org/', 'https://seclists.org/nmap-announce/', 'https://seclists.org/nmap-dev/', 'https://seclists.org/bugtraq/', 'https://seclists.org/fulldisclosure/', 'https://seclists.org/pen-test/', 'https://seclists.org/basics/', 'https://seclists.org/', 'https://sectools.org', 'https://sectools.org/tag/pass-audit/', 'https://sectools.org/tag/sniffers/', 'https://sectools.org/tag/vuln-scanners/', 'https://sectools.org/tag/web-scanners/', 'https://sectools.org/tag/wireless/', 'https://sectools.org/tag/sploits/', 'https://sectools.org/tag/packet-crafters/', 'https://sectools.org/', 'https://insecure.org/', 'https://insecure.org/advertising.html', 'https://insecure.org/fyodor/', 'https://nmap.org', 'https://insecure.org/fyodor', 'https://nmap.org', 'https://npcap.com', 'https://sectools.org', 'https://seclists.org/', 'https://insecure.org/', 'https://insecure.org/fyodor/', 'https://insecure.org/advertising.html', 'https://insecure.org/privacy.html']

	print("TEST: staticSiteScraper() positive input")
	with open(os.path.join("testingDataFolder","staticSiteScraperData.bs4"), "r") as htmlFileReader:
		providedData = htmlFileReader.read()
	providedData = bs(providedData,'html.parser')
	testResult,reason = staticSiteScraperTest(testSite,providedData,anticipatedResults)
	resultDisplayer(testType,testResult,reason)

def staticSiteScraperNegativeTest(testSite):
	'''
	!STUB Function for running tests on pubCrawl.py's staticSiteScraper() function with an anticipated negative/FAIL outcome.
	:param testSite: URL being fed in to initialize the pubCrawl() class
	:type testSite: str	
	'''
	testType = "NEGATIVE"
	anticipatedResults = []

	print("TEST: staticSiteScraper() negative input")
	with open(os.path.join("testingDataFolder","staticSiteScraperData.bs4"), "r") as htmlFileReader:
		providedData = htmlFileReader.read()
	providedData = bs(providedData,'html.parser')
	testResult,reason = staticSiteScraperTest(testSite,providedData,anticipatedResults)
	resultDisplayer(testType,testResult,reason)

def siteConnectorPositiveTest(testSite):
	'''
	Function for running tests on pubCrawl.py's siteConnector() function with an anticipated positive/PASS outcome.
	:param testSite: Website being fed into the function to provide value to initialize the called function within pubCrawl() class
	:type testSite: str	
	'''

	testType = "POSITIVE"

	print("TEST: siteConnector() positive input")
	testResult, reason = siteConnectorTest(testSite,testSite)
	resultDisplayer(testType,testResult,reason)
	
def siteConnectorNegativeTest(testSite):
	'''
	Function for running tests on pubCrawl.py's siteConnector() function with an anticipated negative/FAIL outcome.
	:param testSite: URL being fed in to initialize the pubCrawl() class
	:type testSite: str	
	''' 
	testType = "negative"
	testURL = "https://scanme.nmap.org/" #malformed URL: scanme.nmap.org does not have HTTPS enabled.
	
	print("TEST: siteConnector() negative input")
	testResult, reason = siteConnectorTest(testSite,testURL)
	resultDisplayer(testType,testResult,reason)

def dynamicConnectorFirefoxPositiveTest(testSite):
	'''
	Function for running tests on pubCrawl.py's dynamicConnectorFirefox() function with an anticipated positive/PASS outcome.
	:param testSite: Website being fed into the function to provide value to input into the called function
	:type testSite: str	
	'''
	testType = "POSITIVE"

	print("TEST: dynamicConnectorFirefox() positive input")
	pub_crawl_dynamicConnectorFirefoxTest = PCT.pubCrawl(testSite,True)
	dynamicConnectorFirefoxTest = pub_crawl_dynamicConnectorFirefoxTest.dynamicConnectorFirefox()
	if str(type(dynamicConnectorFirefoxTest)) == "<class 'selenium.webdriver.firefox.webdriver.WebDriver'>":
		testResult = 1
		reason = ""
	else:
		testResult = 0
		reason = f"dynamicConnectorFirefox() returned {type(dynamicConnectorFirefoxTest)} instead of selenium.webdriver.firefox.webdriver.WebDriver"
	resultDisplayer(testType,testResult,reason)

def dynamicSiteGrabberPositiveTest(testSite):
	'''
	!STUB 	Function for running tests on pubCrawl.py's dynamicSiteGrabber() function with an anticipated positive/PASS outcome.
	:param testSite: Website being fed into the function to provide value to input into the called function
	:type testSite: str	
	'''
	testType = 'POSITIVE'
	testURL = 'http://scanme.nmap.org'
	
	print("TEST: dynamicSiteGrabber() positive input")
	testResult,reason = dynamicSiteGrabberTest(testSite,testURL)
	resultDisplayer(testType,testResult,reason)

def dynamicSiteGrabberNegativeTest(testSite):
	'''
	!STUB Function for running tests on pubCrawl.py's dynamicSiteGrabber() function with an anticipated negative/FAIL outcome.
	:param testSite: URL being fed in to initialize the pubCrawl() class
	:type testSite: str	
	'''
	testType = 'NEGATIVE'
	testURL = 'https://scanme.nmap.org' #Malformed URL; scanme.nmap.org does not have HTTPS enabled.

	print("TEST: dynamicSiteGrabber() negative input")
	testResult,reason = dynamicSiteGrabberTest(testSite,testURL)
	resultDisplayer(testType,testResult,reason)

#***INCOMPLETE/STUB SECTION BEGIN***

def scrapeSitePositiveTest(testSite):
	'''
	!STUB 	Function for running tests on pubCrawl.py's scrapeSite() function with an anticipated positive/PASS outcome. Not sure if this should be in the unit Tests as it is the running function for the class.  Should this be in "softwareTests()" instead?
	:param testSite: Website being fed into the function to provide value to input into the called function
	:type testSite: str	
	'''
	pass
	
def scrapeSiteNegativeTest(testSite):
	'''
	!STUB Function for running tests on pubCrawl.py's scrapeSite() function with an anticipated negative/FAIL outcome. Not sure if this should be in the unit Tests as it is the running function for the class.  Should this be in "softwareTests()" instead? Not sure how to force this to fail.  Looking to guidance.
	:param testSite: URL being fed in to initialize the pubCrawl() class
	:type testSite: str	
	'''
	pass

def fileNamerNegativeTest(testSite):
	'''
	!STUB 	Function for running tests on pubCrawl.py's fileNamerNegativeTest() function with an anticipated negative/FAIL outcome. Testing note: I am not sure how to properly do negative testing on a function with no input.  I could force it to not work properly by futzing with a source value within the function, but that doesn't feel like I am testing the function's actual functionality.
	:param testSite: URL being fed in to initialize the pubCrawl() class
	:type testSite: str	
	''' 
	testType = "NEGATIVE"
	print("TEST: fileNamer() negative provided input")
	testResult,reason = fileNamerTest(testSite)
	resultDisplayer(testType,testResult,reason)

def dynamicConnectorFirefoxNegativeTest(testSite):
	'''
	!STUB Function for running tests on pubCrawl.py's dynamicConnectorFirefox() function with an anticipated negative/FAIL outcome. Test note: I am not sure how to test for a negative outcome of a function with no input. Leaving for discussion at later time.
	:param testSite: URL being fed in to initialize the pubCrawl() class
	:type testSite: str	
	'''
	testType = "NEGATIVE"

	print("TEST: dynamicConnectorFirefox() negative input")

#***INCOMPLETE/STUB SECTION END***

#**FUNCTION TEST SECTION END**

def negativeUnitTests(testSite):
	'''
	Function for running all the of the available functions that perform negative unit tests at the same time.
	:param testSite: Website being fed into the function in order to initialize pubCrawl() class
	:type testSite: str
	'''

	dataPoolSorterNegativeTests(testSite)
	pathCombinerNegativeTests(testSite)
	userInputHandlerNegativeTests(testSite)
	scrapeDynamicSiteNegativeTest(testSite)
	scrapeStaticSiteNegativeTest()
	logHandlerNegativeTest(testSite)
	fileReaderNegativeTest(testSite)
	dataParserNegativeTest(testSite)
	staticSiteScraperNegativeTest(testSite)
	siteConnectorNegativeTest(testSite)
	dynamicSiteGrabberNegativeTest(testSite)

	
	#fileNamerNegativeTest(testSite)
	#dynamicConnectorFirefoxNegativeTest(testSite)
	#scrapeSiteNegativeTest(testSite)

def positiveUnitTests(testSite):
	'''
	Function for running all the of the available functions that perform positive unit tests at the same time.
	:param testSite: Website being fed into the function in order to initialize pubCrawl() class
	:type testSite: str
	'''
	
	dataPoolSorterPositiveTests(testSite)
	pathCombinerPositiveTests(testSite)
	userInputHandlerPositiveTests(testSite)
	scrapeDynamicSitePositiveTest(testSite)
	scrapeStaticSitePositiveTest(testSite)
	logHandlerPositiveTest(testSite)
	fileNamerPositiveTest(testSite)
	fileReaderPositiveTest(testSite)
	dataParserPositiveTest(testSite)
	staticSiteScraperPositiveTest(testSite)
	siteConnectorPositiveTest(testSite)
	dynamicConnectorFirefoxPositiveTest(testSite)
	dynamicSiteGrabberPositiveTest(testSite)

	#scrapeSitePositiveTest(testSite)


def runUnitTests(testSite):
	'''
	Function for testing all unit tests in turn instead of having to call them individually.
	:param testSite: Website being fed into the function in order to initialize pubCrawl() class
	:type testSite: str
	'''
	positiveUnitTests(testSite)
	negativeUnitTests(testSite)

#*UNIT TEST SECTION END*

#*SOFTWARE TEST SECTION BEGIN*
def runSoftwareTests(testSite):
	'''
	Function for testing all unit tests in turn instead of having to call them individually.
	:param testSite: Website being fed into the function in order to initialize pubCrawl() class
	:type testSite: str
	'''
	pass

#*SOFTWARE TEST SECTION END*

def runTests(testSite):
	'''
	Function for testing all tests in turn instead of having to call them individually.
	:param testSite: Website being fed into the function in order to initialize pubCrawl() class
	:type testSite: str
	'''
	runUnitTests(testSite)
	runSoftwareTests(testSite)

def main():
	runTests(dummySite)

if __name__ == '__main__':
	main()
