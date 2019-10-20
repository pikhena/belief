#NLP Project - October, 2019
#Belief - belief.py
# encoding=utf8

#IMPORTS---------------------------------------------------------------
import io
import re, sys
import os
import nltk
from nltk.tokenize import word_tokenize
from nltk.util import ngrams
from collections import Counter
from math import log, pow
reload(sys)
sys.setdefaultencoding('utf8')

#GLOBAL VARIABLES---------------------------------------------------------------
""" needed varaibles, lists and dictionaries"""
#core belief data
worthless_data = []
unlovable_data = []
safety_data = []
belong_data = []
defective_data = []
whole_data = []
nothing_data = []
powerless_data = []
balance_data = []
unsure_data = []

#core belief data normalized
worthless_normalized = []
unlovable_normalized = []
safety_normalized = []
belong_normalized = []
defective_normalized = []
whole_normalized = []
nothing_normalized = []
powerless_normalized = []
balance_normalized = []
unsure_normalized = []

#vocabulary
all_vocab = []


#core belief classes data
defectivenesscbc_data = []
safetycbc_data = []
wholenesscbc_data = []
selfworthcbc_data = []
boundariescbc_data = []
moralitycbc_data = []
belongingcbc_data = []


#core belief parent classes data
helplessnessparentclass_data = []
unlovableparentclass_data = []
worthlessnessparentclass_data = []

allData = []
normalizedallData = []

#dictionaries to store probability values. It saves the words as keys in these dictionaries, and the calculation of their probabilities as the values.
helplessnessparentClassProb = {}
unlovableparentClassProb = {}
worthlessnessparentClassProb = {}

defectivenesscbcProb = {}
safetycbcProb = {}
wholenesscbcProb = {}
selfworthcbcProb = {}
boundariescbcProb = {}
moralitycbcProb = {}
belongingcbcProb = {}

worthless_prob = {}
unlovable_prob = {}
safety_prob = {}
belong_prob = {}
defective_prob = {}
whole_prob = {}
nothing_prob = {}
powerless_prob = {}
balance_prob = {}
unsure_prob = {}


#directories
alldirectory = "/Users/priscillaikhena/Downloads/NLPProject/trainingdata/"
directory_worthless = "/Users/priscillaikhena/Downloads/NLPProject/trainingdata/worthless_corpus.txt/"
directory_unlovable = "/Users/priscillaikhena/Downloads/NLPProject/trainingdata/unlovable_corpus.txt/"
directory_safety = "/Users/priscillaikhena/Downloads/NLPProject/trainingdata/safety_corpus.txt/"
directory_belong = "/Users/priscillaikhena/Downloads/NLPProject/trainingdata/belong_corpus.txt/"
directory_defective = "/Users/priscillaikhena/Downloads/NLPProject/trainingdata/defective_corpus.txt/"
directory_whole = "/Users/priscillaikhena/Downloads/NLPProject/trainingdata/whole_corpus.txt/"
directory_nothing = "/Users/priscillaikhena/Downloads/NLPProject/trainingdata/nothing_corpus.txt/"
directory_powerless = "/Users/priscillaikhena/Downloads/NLPProject/trainingdata/powerless_corpus.txt/"
directory_balance = "/Users/priscillaikhena/Downloads/NLPProject/trainingdata/balance_corpus.txt/"
directory_unsure = "/Users/priscillaikhena/Downloads/NLPProject/trainingdata/unsure_corpus.txt/"


#DICTIONARIES MAPPING BETWEEN PARENT CLASS, CORE BELIEF CLASSES, CORE BELIEFS AND QUOTES----------------------------------------------------------------

#cbc to core belief dictionary. This dictionary shows the mapping between core beliefs and core belief classes.
cbctocorebelief = {
		"defectiveness" : ["defective", "unlovable"],
		"safety" : ["safe"],
		"wholeness" : ["whole"],
		"selfworth" : ["nothing", "worthless"],
		"boundaries" : ["powerless", "balance"],
		"morality" : ["unsure"],
        "belonging" : ["belong"]
	};

#parent class to core belief class, is a dictionary that shows the mapping between parent classes and the sub core belief classes.
parentclasstocbc = {
		"helplessness" : ["safety", "morality", "boundaries"],
		"unlovable" : ["belonging", "defectiveness"],
        "worthlessness" : ["wholeness", "selfworth"]

	};

#core belief class to quote, is a dictionary that shows the mapping between core belief classes and the quotes and ecouraging words we'd like to show the user based on the core belief class detected.
cbctoquote = {
		"defectiveness" : ["quote1", "advice1"],
		"safety" : ["quote2", "advice2"],
		"wholeness" : ["quote3", "advice3"],
		"selfworth" : ["quote4", "advice4"],
		"boundaries" : ["quote5", "advice5"],
		"morality" : ["quote6", "advice6"],
        "belonging" : ["quote7", "advice7"]
	};

#corebelief to core belief statements
cbtostatement = {
		"defective" : "I am defective, it's always my fault.",
		"unlovable" : "Nobody loves me, I am unlovable.",
		"safe" : "I am unsafe, I can't trust anyone.",
		"whole" : " I am not whole, I have lost my spirit.",
		"nothing" : "I am nothing, I don't exist.",
		"worthless" : "I am worthless.",
		"powerless" : "I am powerless",
		"balance" : "I am out of balance, my life is out of control.",
		"unsure" : "I am wrong about everything.",
		"belong" : "I don't belong, no one understands me."
	};


#READING IN THE CORPUS----------------------------------------------------------------
#Opens all the data, and reads in the words
for filename in os.listdir(alldirectory):
    with io.open(os.path.join(alldirectory, filename), "rb") as bookFile:
        wordList = bookFile.read()
        allData.append(wordList)

#Filling up the core belief lists above
belong_data = allData[0]
powerless_data = allData[1]
unsure_data = allData[2]
balance_data = allData[3]
defective_data = allData[4]
worthless_data = allData[5]
unlovable_data = allData[6]
whole_data = allData[7]
safety_data = allData[8]
nothing_data = allData[9]

#Tokenizing and Normalizing all data

def lower(word):
    word = word.lower()
    return word

joinallData = " ".join(allData) #joining all the strings in all data so all data becomes one big string that can be tokenized
tokenizedallData = nltk.word_tokenize(joinallData)


for word in tokenizedallData:
    newword = lower(word)
    normalizedallData.append(newword)


#Tokenizing and Normalizing core belief lists

worthless_tokenized = nltk.word_tokenize(worthless_data)
unlovable_tokenized = nltk.word_tokenize(unlovable_data)
safety_tokenized = nltk.word_tokenize(safety_data)
belong_tokenized = nltk.word_tokenize(belong_data)
defective_tokenized = nltk.word_tokenize(defective_data)
whole_tokenized = nltk.word_tokenize(whole_data)
nothing_tokenized = nltk.word_tokenize(nothing_data)
powerless_tokenized = nltk.word_tokenize(powerless_data)
balance_tokenized = nltk.word_tokenize(balance_data)
unsure_tokenized = nltk.word_tokenize(unsure_data)


for word in worthless_tokenized:
    newword = lower(word)
    worthless_normalized.append(newword)

for word in unlovable_tokenized:
    newword = lower(word)
    unlovable_normalized.append(newword)

for word in safety_tokenized:
    newword = lower(word)
    safety_normalized.append(newword)

for word in belong_tokenized:
    newword = lower(word)
    belong_normalized.append(newword)

for word in defective_tokenized:
    newword = lower(word)
    defective_normalized.append(newword)

for word in whole_tokenized:
    newword = lower(word)
    whole_normalized.append(newword)

for word in nothing_tokenized:
    newword = lower(word)
    nothing_normalized.append(newword)

for word in powerless_tokenized:
    newword = lower(word)
    powerless_normalized.append(newword)

for word in balance_tokenized:
    newword = lower(word)
    balance_normalized.append(newword)

for word in unsure_tokenized:
    newword = lower(word)
    unsure_normalized.append(newword)


#Filling up core belief class lists

defectivenesscbc_data = defective_normalized + unlovable_normalized
safetycbc_data = safety_normalized
wholenesscbc_data = whole_normalized
selfworthcbc_data = nothing_normalized + worthless_normalized
boundariescbc_data = powerless_normalized + balance_normalized
moralitycbc_data = unsure_normalized
belongingcbc_data = belong_normalized


#Filling up parent class lists
helplessnessparentclass_data = safetycbc_data + moralitycbc_data + boundariescbc_data
unlovableparentclass_data = belongingcbc_data + defectivenesscbc_data
worthlessnessparentclass_data = wholenesscbc_data + selfworthcbc_data



#Creating a vocabulary of all words in our training data

normalizedallDataCount = Counter(normalizedallData)
for key, value in normalizedallDataCount.iteritems():
        if value >= 2:
            all_vocab.append(key)



#CALCULATING AND ASSIGNING PROBABILITIES - TRAINING THE DATA----------------------------------------------------------------
def calculateProbScore(wordfreq, totalcountofwordsingroup, vocabularycount, k):

    score = log((wordfreq + k), 10) / log((totalcountofwordsingroup + (vocabularycount * k)), 10)
    return score
#Parent Classes Calculation
normalizedHelpless = Counter(helplessnessparentclass_data)
normalizedUnlovable = Counter(unlovableparentclass_data)
normalizedWorthless = Counter(worthlessnessparentclass_data)

#function to calculate the probability that keywords fall into parent class - HELPLESS
for key, value in normalizedHelpless.iteritems():

            helplesswordscore = calculateProbScore(value, len(helplessnessparentclass_data), len(all_vocab), 1)
            helplessnessparentClassProb[key] = helplesswordscore

#function to calculate the probability that keywords fall into parent class - WORTHLESS
for key, value in normalizedWorthless.iteritems():

            worthlesswordscore = calculateProbScore(value, len(worthlessnessparentclass_data), len(all_vocab), 1)
            worthlessnessparentClassProb[key] = worthlesswordscore


#function to calculate the probability that keywords fall into parent class - UNLOVABLE
for key, value in normalizedUnlovable.iteritems():

            unlovablewordscore = calculateProbScore(value, len(unlovableparentclass_data), len(all_vocab), 1)
            unlovableparentClassProb[key] = unlovablewordscore


#Core Belief Classes Calculation
normalizedsafetycbc = Counter(safetycbc_data)
normalizedmoralitycbc = Counter(moralitycbc_data)
normalizedboundariescbc = Counter(boundariescbc_data)
normalizedbelongingcbc = Counter(belongingcbc_data)
normalizeddefectivecbc = Counter(defectivenesscbc_data)
normalizedwholenesscbc = Counter(wholenesscbc_data)
normalizedselfworthcbc = Counter(selfworthcbc_data)

#function to calculate the probability that keywords fall into CBC - SAFETY
for key, value in normalizedsafetycbc.iteritems():

            safetycbcwordscore = calculateProbScore(value, len(safetycbc_data), len(all_vocab), 1)
            safetycbcProb[key] = safetycbcwordscore

#function to calculate the probability that keywords fall into CBC - MORALITY
for key, value in normalizedmoralitycbc.iteritems():

            moralitycbcwordscore = calculateProbScore(value, len(moralitycbc_data), len(all_vocab), 1)
            moralitycbcProb[key] = moralitycbcwordscore


#function to calculate the probability that keywords fall into CBC - BOUNDARIES
for key, value in normalizedboundariescbc.iteritems():

            boundariescbcwordscore = calculateProbScore(value, len(boundariescbc_data), len(all_vocab), 1)
            boundariescbcProb[key] = boundariescbcwordscore



#function to calculate the probability that keywords fall into CBC - BELONGING
for key, value in normalizedbelongingcbc.iteritems():

            belongingcbcwordscore = calculateProbScore(value, len(belongingcbc_data), len(all_vocab), 1)
            belongingcbcProb[key] = belongingcbcwordscore


#function to calculate the probability that keywords fall into CBC - DEFECTIVENESS
for key, value in normalizeddefectivecbc.iteritems():

            defectivecbcwordscore = calculateProbScore(value, len(defectivenesscbc_data), len(all_vocab), 1)
            defectivenesscbcProb[key] = defectivecbcwordscore



#function to calculate the probability that keywords fall into CBC - WHOLENESS
for key, value in normalizedwholenesscbc.iteritems():

            wholenesscbcwordscore = calculateProbScore(value, len(wholenesscbc_data), len(all_vocab), 1)
            wholenesscbcProb[key] = wholenesscbcwordscore



#function to calculate the probability that keywords fall into CBC - SELFWORTH

for key, value in normalizedselfworthcbc.iteritems():

            selfworthcbcwordscore = calculateProbScore(value, len(selfworthcbc_data), len(all_vocab), 1)
            selfworthcbcProb[key] = selfworthcbcwordscore

#Core Belief Calculation

normalizedworthlesscb = Counter(worthless_normalized)
normalizedunlovablecb = Counter(unlovable_normalized)
normalizedsafetycb = Counter(safety_normalized)
normalizedbelongcb = Counter(belong_normalized)
normalizeddefectivecb = Counter(defective_normalized)
normalizedwwholecb = Counter(whole_normalized)
normalizednothingcb = Counter(nothing_normalized)
normalizedpowerlesscb = Counter(powerless_normalized)
normalizedbalancecb = Counter(balance_normalized)
normalizedunsurecb = Counter(unsure_normalized)

#function to calculate the probability that keywords in Worthless CB
for key, value in normalizedworthlesscb.iteritems():

            worthcbwordscore = calculateProbScore(value, len(worthless_normalized), len(all_vocab), 1)
            worthless_prob[key] = worthcbwordscore


#function to calculate the probability that keywords in Unlovable CB
for key, value in normalizedunlovablecb.iteritems():

            unlovablecbwordscore = calculateProbScore(value, len(unlovable_normalized), len(all_vocab), 1)
            unlovable_prob[key] = unlovablecbwordscore


#function to calculate the probability that keywords in Safety CB
for key, value in normalizedsafetycb.iteritems():

            safetycbwordscore = calculateProbScore(value, len(safety_normalized), len(all_vocab), 1)
            safety_prob[key] = safetycbwordscore

#function to calculate the probability that keywords in Belong CB
for key, value in normalizedbelongcb.iteritems():

            belongcbwordscore = calculateProbScore(value, len(belong_normalized), len(all_vocab), 1)
            belong_prob[key] = belongcbwordscore


#function to calculate the probability that keywords in Defective CB
for key, value in normalizeddefectivecb.iteritems():

            defectivecbwordscore = calculateProbScore(value, len(defective_normalized), len(all_vocab), 1)
            defective_prob[key] = defectivecbwordscore


#function to calculate the probability that keywords in Whole CB
for key, value in normalizedwwholecb.iteritems():

            wholecbwordscore = calculateProbScore(value, len(whole_normalized), len(all_vocab), 1)
            whole_prob[key] = wholecbwordscore


#function to calculate the probability that keywords in Nothing CB
for key, value in normalizednothingcb.iteritems():

            nothingcbwordscore = calculateProbScore(value, len(nothing_normalized), len(all_vocab), 1)
            nothing_prob[key] = nothingcbwordscore

#function to calculate the probability that keywords in Powerless CB
for key, value in normalizedpowerlesscb.iteritems():

            powerlesscbwordscore = calculateProbScore(value, len(powerless_normalized), len(all_vocab), 1)
            powerless_prob[key] = powerlesscbwordscore


#function to calculate the probability that keywords in Balance CB
for key, value in normalizedbalancecb.iteritems():

            balancecbwordscore = calculateProbScore(value, len(balance_normalized), len(all_vocab), 1)
            balance_prob[key] = balancecbwordscore


#function to calculate the probability that keywords in Unsure CB
for key, value in normalizedunsurecb.iteritems():

            unsurecbwordscore = calculateProbScore(value, len(unsure_normalized), len(all_vocab), 1)
            unsure_prob[key] = unsurecbwordscore

#FUNCTIONS TO RETURN THE PROBABILITIES OF WORDS TO TEST THE MODEL-------------------------------------------------

#Parent Classes
def checkHelplessnessParentClassProb(word):
	if word in helplessnessparentClassProb.keys():
		helplessvalue = helplessnessparentClassProb.get(word)

	else:
		helplessvalue = 0

	return helplessvalue



def checkUnlovableParentClassProb(word):
	if word in unlovableparentClassProb.keys():
		unlovablevalue = unlovableparentClassProb.get(word)

	else:
		unlovablevalue = 0

	return unlovablevalue


def checkWorthlessnessParentClassProb(word):
	if word in worthlessnessparentClassProb.keys():
		worthlessvalue = worthlessnessparentClassProb.get(word)

	else:
		worthlessvalue = 0

	return worthlessvalue

#Core Belief Classes
def checkSafetyCoreBeliefClassProb(word):
	if word in safetycbcProb.keys():
		safetyvalue = safetycbcProb.get(word)

	else:
		safetyvalue = 0

	return safetyvalue


def checkDefectiveCoreBeliefClassProb(word):
	if word in defectivenesscbcProb.keys():
		defectivevalue = defectivenesscbcProb.get(word)

	else:
		defectivevalue = 0

	return defectivevalue

def checkWholenessCoreBeliefClassProb(word):
	if word in wholenesscbcProb.keys():
		wholenessvalue = wholenesscbcProb.get(word)

	else:
		wholenessvalue = 0

	return wholenessvalue


def checkSelfWorthCoreBeliefClassProb(word):
	if word in selfworthcbcProb.keys():
		selfworthvalue = selfworthcbcProb.get(word)

	else:
		selfworthvalue = 0

	return selfworthvalue


def checkBoundariesCoreBeliefClassProb(word):
	if word in boundariescbcProb.keys():
		boundariesvalue = boundariescbcProb.get(word)

	else:
		boundariesvalue = 0

	return boundariesvalue


def checkMoralityCoreBeliefClassProb(word):
	if word in moralitycbcProb.keys():
		moralityvalue = moralitycbcProb.get(word)

	else:
		moralityvalue = 0

	return moralityvalue


def checkBelongingCoreBeliefClassProb(word):
	if word in belongingcbcProb.keys():
		belongingvalue = belongingcbcProb.get(word)

	else:
		belongingvalue = 0

	return belongingvalue

#Core Beliefs
def checkWorthlessCoreBeliefProb(word):
	if word in worthless_prob.keys():
		worthvalue = worthless_prob.get(word)

	else:
		worthvalue = 0

	return worthvalue

def checkUnlovableCoreBeliefProb(word):
	if word in unlovable_prob.keys():
		unlovablevalue = unlovable_prob.get(word)

	else:
		unlovablevalue = 0

	return unlovablevalue

def checkSafetyCoreBeliefProb(word):
	if word in safety_prob.keys():
		safetyvalue = safety_prob.get(word)

	else:
		safetyvalue = 0

	return safetyvalue


def CheckBelongCoreBeliefProb(word):
	if word in belong_prob.keys():
		belongvalue = belong_prob.get(word)

	else:
		belongvalue = 0

	return belongvalue

def checkDefectiveCoreBeliefProb(word):
	if word in defective_prob.keys():
		defectivevalue = defective_prob.get(word)

	else:
		defectivevalue = 0

	return defectivevalue


def checkWholeCoreBeliefProb(word):
	if word in whole_prob.keys():
		wholevalue = whole_prob.get(word)

	else:
		wholevalue = 0

	return wholevalue


def checkNothingCoreBeliefProb(word):
	if word in nothing_prob.keys():
		nothingvalue = nothing_prob.get(word)

	else:
		nothingvalue = 0

	return nothingvalue


def checkPowerlessCoreBeliefProb(word):
	if word in powerless_prob.keys():
		powerlessvalue = powerless_prob.get(word)

	else:
		powerlessvalue = 0

	return powerlessvalue

def checkBalanceCoreBeliefProb(word):
	if word in balance_prob.keys():
		balancevalue = balance_prob.get(word)

	else:
		balancevalue = 0

	return balancevalue


def checkUnsureCoreBeliefProb(word):
	if word in unsure_prob.keys():
		unsurevalue = unsure_prob.get(word)

	else:
		unsurevalue = 0

	return unsurevalue

#test = checkWholeCoreBeliefProb('safe')
#test2 = checkSafetyCoreBeliefProb('safe')
#print test
#print test2


#FUNCTIONS TO CHECK AND RETURN THE GREATER PROBABILITY, FOR THE TEST DATA.----------------------------------------------------------------

#function to check the parent class. This function takes in the keywords, and returns the parent class with the highest probability
    #the function calls other parent class functions to calculate their probabilities, and then returns the greatest.
    #if it's a tie, choose one to return.
def getParentClass(list):
	helplessness = []
	unlovable = []
	worthlessness = []
	for word in list:
		helplessness.append(checkHelplessnessParentClassProb(word))
		unlovable.append(checkUnlovableParentClassProb(word))
		worthlessness.append(checkWorthlessnessParentClassProb(word))

	helplessnessvalue = 0
	for num in helplessness:
		helplessnessvalue += num

	unlovablevalue = 0
	for num in unlovable:
		unlovablevalue += num

	worthlessnessvalue = 0
	for num in worthlessness:
		worthlessnessvalue += num


	if helplessnessvalue > unlovablevalue and helplessnessvalue > worthlessnessvalue:
		return "helplessness"

	if unlovablevalue > helplessnessvalue and unlovablevalue > worthlessnessvalue:
		return "unlovable"

	if worthlessnessvalue > helplessnessvalue and worthlessnessvalue > unlovablevalue:
		return "worthlessness"


#function to check the core belief class. This function takes in the keywords, and the parent class.
    #this function first finds what core belief classes to look at, by looking at the dictionary value of the parent class passed into the function.
    #After seeing their values, it then calls the calculation classes for the corresponding core belief classes.
    #It returns what core belief class has the highest probability
    #if it's a tie, choose one to return.

def getCoreBeliefClass(list, parentclass):
	corebeliefclasses = parentclasstocbc.get(parentclass)
	belongingvalue = 0
	safetyvalue = 0
	moralityvalue = 0
	defectivenessvalue = 0
	wholenessvalue = 0
	selfworthvalue = 0

	belonging = []
	safety = []
	morality = []
	defectiveness = []
	wholeness = []
	selfworth = []


	for cbc in corebeliefclasses:

		if cbc == "belonging":
			for word in list:
				belonging.append(checkBelongingCoreBeliefClassProb(word))

		if cbc == "safety":
			for word in list:
				safety.append(checkSafetyCoreBeliefClassProb(word))

		if cbc == "morality":
			for word in list:
				morality.append(checkMoralityCoreBeliefClassProb(word))

		if cbc == "defectiveness":
				for word in list:
					defectiveness.append(checkDefectiveCoreBeliefClassProb(word))

		if cbc == "wholeness":
			for word in list:
				wholeness.append(checkWholenessCoreBeliefClassProb(word))

		if cbc == "selfworth":
			for word in list:
				selfworth.append(checkSelfWorthCoreBeliefClassProb(word))

	for num in belonging:
		belongingvalue += num

	for num in safety:
		safetyvalue += num

	for num in morality:
		moralityvalue += num

	for num in defectiveness:
		defectivenessvalue += num

	for num in wholeness:
		wholenessvalue += num

	for num in selfworth:
		selfworthvalue += num


	highest = max(belongingvalue, safetyvalue, moralityvalue, defectivenessvalue, wholenessvalue, selfworthvalue)
	if belongingvalue == highest:
		return "belonging"

	elif safetyvalue == highest:
		return "safety"

	elif moralityvalue == highest:
		return "morality"

	elif defectivenessvalue == highest:
		return "defectiveness"

	elif wholenessvalue == highest:
		return "wholeness"

	elif selfworthvalue == highest:
		return "selfworth"

#function to check the core belief. This function takes in keywords and also the CBC class. It then calls the corresponding core belief functions,
    #and returns the core belief with the highest score.
    #if it's a tie, choose one to return.

def getCoreBelief(list, corebeliefclass):

	corebeliefs = cbctocorebelief.get(corebeliefclass)

	defectivevalue = 0
	unlovablevalue = 0
	safevalue = 0
	wholevalue = 0
	nothingvalue = 0
	worthlessvalue = 0
	powerlessvalue = 0
	balancevalue = 0
	unsurevalue = 0
	belongvalue = 0

	defective = []
	unlovable = []
	safe = []
	whole = []
	nothing = []
	worthless = []
	powerless = []
	balance = []
	unsure = []
	belong = []

	for cb in corebeliefs:

		if cb == "defective":
			for word in list:
				defective.append(checkDefectiveCoreBeliefProb(word))

		elif cb == "unlovable":
			for word in list:
				unlovable.append(checkUnlovableCoreBeliefProb(word))

		elif cb == "safe":
			for word in list:
				safe.append(checkSafetyCoreBeliefProb(word))

		elif cb == "whole":
			for word in list:
				whole.append(checkWholeCoreBeliefProb(word))

		elif cb == "nothing":
			for word in list:
				nothing.append(checkNothingCoreBeliefProb(word))

		elif cb == "worthless":
			for word in list:
				worthless.append(checkWorthlessCoreBeliefProb(word))

		elif cb == "powerless":
			for word in list:
				powerless.append(checkPowerlessCoreBeliefProb(word))

		elif cb == "balance":
			for word in list:
				balance.append(checkBalanceCoreBeliefProb(word))

		elif cb == "unsure":
			for word in list:
				unsure.append(checkUnsureCoreBeliefProb(word))

		elif cb == "belong":
			for word in list:
				belong.append(CheckBelongCoreBeliefProb(word))


	for num in defective:
		defectivevalue += num

	for num in unlovable:
		unlovablevalue += num

	for num in safe:
		safevalue += num

	for num in nothing:
		nothingvalue += num

	for num in worthless:
		worthlessvalue += num

	for num in powerless:
		powerlessvalue += num

	for num in balance:
		balancevalue += num

	for num in unsure:
		unsurevalue += num

	for num in belong:
		belongvalue += num

	for num in whole:
		wholevalue += num


	highest = max(defectivevalue, unlovablevalue, safevalue, nothingvalue, worthlessvalue, powerlessvalue, balancevalue, unsurevalue, belongvalue, wholevalue)


	if defectivevalue == highest:
		return "defective"

	elif unlovablevalue == highest:
		return "unlovable"

	elif safevalue == highest:
		return "safe"

	elif nothingvalue == highest:
		return "nothing"

	elif worthlessvalue == highest:
		return "worthless"

	elif powerlessvalue == highest:
		return "powerless"

	elif balancevalue == highest:
		return "balance"

	elif unsurevalue == highest:
		return "unsure"

	elif belongvalue == highest:
		return "belong"

	elif wholevalue == highest:
		return "whole"

#Testing the model.

def testFunction():

	firstanswer = ["I", "feel", "so", "safe", "unsafe"]
	secondanswer = ["I", "just", "feel", "not"]
	thirdanswer = ["I", "just", "do", "not" , "safe", "world."]


	parentclass = getParentClass(firstanswer)
	corebeliefclass = getCoreBeliefClass(secondanswer, parentclass)
	corebelief = getCoreBelief(thirdanswer, corebeliefclass)


	print parentclass
	print corebeliefclass
	print cbtostatement.get(corebelief)
#USER INPUT - MAIN FUNCTION THAT PROMPTS THE USER WITH QUESTIONS, AND TELLS THEM THEIR CORE BELIEF------------------

def userInputFunction():
	preanswer = raw_input("How are you feeling today? ")
	firstanswer = raw_input("What negative thought about yourself would you like to change today? ")
	firstanswerarray = firstanswer.split()
	parentclass = getParentClass(firstanswerarray)
	secondanswer = raw_input("Assuming this thought is true, why would it be so bad? ")
	secondanswerarray = secondanswer.split()
	corebeliefclass = getCoreBeliefClass(secondanswerarray, parentclass)
	thirdanswer = raw_input("Why would that be so bad? ")
	thirdanswerarray = thirdanswer.split()
	corebelief = getCoreBelief(thirdanswerarray, corebeliefclass)

	print parentclass
	print corebeliefclass
	print corebelief

	#print secondanswer
	#print thirdanswer

#testFunction()
userInputFunction()
