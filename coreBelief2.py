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
		"safety" : "safe",
		"wholeness" : "whole",
		"selfworth" : ["nothing", "worthless"],
		"boundaries" : ["powerless", "balance"],
		"morality" : "unsure",
        "belonging" : "belong"
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
        "belonging" : ["quote7", "advice7"],
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
#function to calculate the probability that keywords fall into parent class - HELPLESS
#function to calculate the probability that keywords fall into parent class - WORTHLESS
#function to calculate the probability that keywords fall into parent class - UNLOVABLE
#function to calculate the probability that keywords fall into CBC - SAFETY
#function to calculate the probability that keywords fall into CBC - MORALITY
#function to calculate the probability that keywords fall into CBC - BOUNDARIES
#function to calculate the probability that keywords fall into CBC - BELONGING
#function to calculate the probability that keywords fall into CBC - DEFECTIVENESS
#function to calculate the probability that keywords fall into CBC - WHOLENESS
#function to calculate the probability that keywords fall into CBC - SELFWORTH
#function to calculate the probability that keywords in CoreBelief -
#function to calculate the probability that keywords in CoreBelief -
#function to calculate the probability that keywords in CoreBelief -
#function to calculate the probability that keywords in CoreBelief -
#function to calculate the probability that keywords in CoreBelief -
#function to calculate the probability that keywords in CoreBelief -
#function to calculate the probability that keywords in CoreBelief -
#function to calculate the probability that keywords in CoreBelief -
#function to calculate the probability that keywords in CoreBelief -
#function to calculate the probability that keywords in CoreBelief -


#FUNCTIONS TO CHECK AND RETURN THE GREATER PROBABILITY, FOR THE TEST DATA.----------------------------------------------------------------

#function to check the parent class. This function takes in the keywords, and returns the parent class with the highest probability
    #the function calls other parent class functions to calculate their probabilities, and then returns the greatest.
    #if it's a tie, choose one to return.




#function to check the core belief class. This function takes in the keywords, and the parent class.
    #this function first finds what core belief classes to look at, by looking at the dictionary value of the parent class passed into the function.
    #After seeing their values, it then calls the calculation classes for the corresponding core belief classes.
    #It returns what core belief class has the highest probability
    #if it's a tie, choose one to return.




#function to check the core belief. This function takes in keywords and also the CBC class. It then calls the corresponding core belief functions,
    #and returns the core belief with the highest score.
    #if it's a tie, choose one to return.


#USER INPUT - MAIN FUNCTION THAT PROMPTS THE USER WITH QUESTIONS, AND PROCESSES THEIR RESPONSES INTO KEYWORDS, THEN CALLING THE FUNCTIONS ABOVE---------------------------------------------------------------

#def main function
#ask the user the first question, and then register their first response as keywords.
#pass keywords into the the check parent class function.
#save the parent class received into a variable called parentclass.

#then ask the second question, save those keywords2 and pass into the check CBC class with the new keywords2 and the parentclass
#save the CBC returned into a variable

#then ask the next question.
#save the reponse into the another variable - keywords3.
#call the check CB to get the highest CB, passing in the new keywords3  and the CBC class, and save what is returned into a coremodel variable.
#Print out this coremodel as the found CoreBelief!


#If the core belief isn't identified, go one level back to the CBC and call the CBC class to check. Thus it'll be recursive here.

#DIRECTORY OF FILES-----------------------------------------------------
