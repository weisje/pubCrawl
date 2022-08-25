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
import string
import sys
import datetime

#*IMPORT BLOCK END*

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
	adjectives = {"Environment":["desert", "tundra", "mountain", "space", "field", "urban"],
"StealthCunning":["hidden", "covert", "uncanny", "scheming", "decisive", "untouchable", "stalking"],
"Volatility":["rowdy", "dangerous", "explosive", "threatening", "warring", "deadly", "killer", "insane", "wild"],
"NegativeConnotation":["bad", "unnecessary", "unknown", "unexpected", "waning"],
"Colors":["red", "orange", "yellow", "green", "blue", "violet"],
"Adjectives":["draconic", "wireless", "spinning", "falling", "orbiting", "hunting", "chasing", "searching", "revealing", "flying", "destroyed", "inconceivable", "tarnished"]}
	nouns = {"LargeCats":["panther", "wildcat", "tiger", "lion", "cheetah", "cougar", "leopard", "jaguar"],
"Snakes":["anaconda", "viper", "cottonmouth", "python", "boa", "sidewinder", "cobra"],
"Birds":["falcon", "eagle", "hawk", "owl", "osprey", "vulture", "petrel", "sparrow", "finch", "cardinal", "dove", "pigeon", "heron", "gull"],
"Insects":["tick", "beetle", "fly", "cicada", "weevil", "ant", "dragonfly", "damselfly", "grasshopper", "flea", "mantis"],
"Predators":["coyote", "wolf", "jackal", "bear", "stoat", "ferret", "weasel", "mink", "alligator", "crocodile", "badger", "wolverine", "hyena"],
"Prey":["wildebeest", "gazelle", "zebra", "elk", "moose", "deer", "stag", "koala", "sloth", "quoll"],
"Equines":["horse", "stallion", "foal", "colt", "mare", "yearling", "filly", "gelding", "mule", "donkey", "pony"],
"MythicalCreatures":["mermaid", "unicorn", "fairy", "troll", "yeti", "pegasus", "griffin", "dragon"],
"OrganicMaterials":[ "amber", "bone", "coral", "ivory", "jet", "nacre", "pearl", "obsidian", "glass"],
"Gems":["agate", "beryl", "diamond", "opal", "ruby", "onyx", "sapphire", "emerald", "jade"],
"Occupations":["nomad", "wizard", "cleric", "pilot", "captain", "commander", "general", "major", "admiral", "chef", "inspector", "sorcerer", "warlock", "fighter", "barbarian", "monk", "farmer", "soldier", "broker", "accountant", "auditor", "actor", "actress", "nurse", "doctor", "manager", "operator", "agent", "spy", "engineer", "carpenter", "cooper", "cobbler", "smith", "artist", "athlete", "technician", "officer", "supervisor", "controller", "attendant", "assembler", "specialist", "breeder", "caretaker", "trainer", "teacher", "tutor", "appraiser", "assessor", "arbitrator", "mediator", "councilor", "lawyer", "architect", "drafter", "recruiter", "recruit", "greenhorn", "novice", "journeyman", "archivist", "scientist", "researcher", "director", "producer", "therapist", "worker", "laborer", "astronomer", "marine", "grunt", "astronaut", "mechanic", "installer", "bellhop", "porter", "bailiff", "baker", "barber", "bartender", "clerk", "collector", "chemist", "physicists", "developer", "biologist", "bookkeeper", "mason", "analyst", "janitor", "driver", "planner", "cutter", "butcher", "buyer", "purchaser", "merchant", "trader", "mate", "cartographer", "cashier", "teller", "cook", "executive", "choreographer", "adjuster", "investigator", "clergyman", "pope", "cardinal", "bishop", "psychologist", "psychiatrist", "coordinator", "coach", "scout", "painter", "concierge", "miner", "tender", "coroner", "paramedic", "jailer", "messenger", "courier", "guard", "curator", "representative", "dancer", "performer", "musician", "administrator", "assistant", "salesman", "vendor", "editor", "advisor", "electrician", "etcher", "engraver", "extractor", "fisherman", "forester", "contractor", "rancher", "farmhand", "watchman", "weaver", "roofer", "wheelwright", "locksmith", "tanner", "grocer", "minstrel", "miller", "armorer", "barrister"],
"Technology":["mainframe", "device", "motherboard", "network", "transistor", "packet", "robot", "android", "cyborg", "display", "battery", "memory", "disk", "computer", "server", "cartridge", "tape", "camera", "projector"],
"SeaCreatures":["octopus", "lobster", "crab", "barnacle", "hammerhead", "orca", "piranha", "shark", "whale"],
"Weather":["storm", "thunder", "lightning", "rain", "hail", "sun", "drought", "snow", "drizzle"],
"Music":["piano", "keyboard", "guitar", "trumpet", "trombone", "flute", "cornet", "horn", "tuba", "clarinet", "saxophone", "piccolo", "violin", "harp", "cello", "drum", "organ", "banjo", "rhythm", "beat", "sound", "song"],
"Tools":["lathe","mill","mask","screwdriver", "hammer", "pliers", "wrench", "saw", "axe", "crowbar", "file", "vise", "anvil", "scissors", "clamp", "planer", "mallet", "chisel", "level", "plumb", "rake", "shovel"],
"Tableware":["fork", "spoon", "knife", "plate", "bowl", "dish", "mug", "cup", "shaker", "platter"],
"Weapons":["dagger", "gun", "knife", "cannon", "mortar", "bola","boomerang","crossbow","longbow","bow","sling","spear","bayonet", "club", "dagger", "halberd", "lance", "pike", "quarterstaff", "sabre", "sword", "tomahawk", "grenade", "mine", "missile", "torpedo", "bazooka", "blunderbuss", "shotgun", "rifle", "pistol", "carbine", "revolver", "musket", "catapult", "ballista"],
"Illness":["plague", "fever","smallpox","covid"],
"Poison":["anthrax","ricin"],
"Armor":["Aventail", "Bevor", "Coif", "Gorget", "Helmet", "Armet", "Barbute", "Bascinet", "Helm", "Morion", "Sallet", "Spangenhelm", "Visor", "Brigandine", "Codpiece", "Cuirass", "Fauld", "Gambeson", "Hauberk", "Jupon", "Pourpoint", "Ailette", "Besagew", "Couter", "Gauntlet", "Pauldron", "Rerebrace", "Spaulder", "Vambrace", "Chausses", "Cuisses", "Greaves", "Poleyn", "Sabaton", "Schynbald", "Tassets"],
"Appliances":["kettle","fridge", "refrigerator", "microwave", "oven", "stove", "washer", "dryer", "vacuum", "freezer", "toaster", "blender", "pan", "steamer", "rack", "broom", "mop", "brush", "bucket", "rag", "towel", "napkin"],
"MundaneObjects":["chain","ink","case","door"],
"Nouns":["warning", "presence", "weapon", "player"]
}
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
