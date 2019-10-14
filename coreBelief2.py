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

"""dictionary mapping between parent class, core belief classes, core beliefs and quotes"""






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


print normalizedallData






#Tokenizing and Normalizing core belief lists










#Creating a vocabulary of all words in our training data






"""functions to calculate probabilities"""
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


"""functions to check the probabilities"""

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


#USER INPUT---------------------------------------------------------------
"""Main Function that prompts the user with questions, and processes their responses into keywords to pass into the functions above"""
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
