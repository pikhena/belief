#NLP Project - October, 2019
#Belief - belief.py
# encoding=utf8

#IMPORTS---------------------------------------------------------------
import io
import re, sys
import os
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
#chi_squares = []


alldirectory = "/Users/priscillaikhena/Downloads/NLP/trainingdata/"
directory_worthless = "/Users/priscillaikhena/Downloads/NLP/trainingdata/worthless_corpus.txt/"
directory_unlovable = "/Users/priscillaikhena/Downloads/NLP/trainingdata/unlovable_corpus.txt/"
directory_safety = "/Users/priscillaikhena/Downloads/NLP/trainingdata/safety_corpus.txt/"
directory_belong = "/Users/priscillaikhena/Downloads/NLP/trainingdata/belong_corpus.txt/"
directory_defective = "/Users/priscillaikhena/Downloads/NLP/trainingdata/defective_corpus.txt/"
directory_whole = "/Users/priscillaikhena/Downloads/NLP/trainingdata/whole_corpus.txt/"
directory_nothing = "/Users/priscillaikhena/Downloads/NLP/trainingdata/nothing_corpus.txt/"
directory_powerless = "/Users/priscillaikhena/Downloads/NLP/trainingdata/powerless_corpus.txt/"
directory_balance = "/Users/priscillaikhena/Downloads/NLP/trainingdata/balance_corpus.txt/"
directory_unsure = "/Users/priscillaikhena/Downloads/NLP/trainingdata/unsure_corpus.txt/"

#READING IN THE CORPUS----------------------------------------------------------------
#Opens all the data, and reads in the words
for filename in os.listdir(alldirectory):
    #with io.open(os.path.join(alldirectory, filename), "r") as bookFile:
    print filename
    with io.open(os.path.join(alldirectory, filename), "rb") as bookFile:
        wordList = bookFile.read()
        #print wordList
        #for i in wordList:
            #print i
            #match = re.split(r'\W+', i)
            #print match

            #for word in match:
            #    print word
            #    allData.append(word)

#print allData

#def reader(dir):
#    worthless_corpus = dir+"worthless_corpus.txt"
    #files = os.listdir(dir)
#    dictionary = {file: tokenizer(open(file).read()) for file in files}
#    tokens = dictionary.values()
#    for token in tokens:
#        for e in token:
#            worthless_data.append(e)

#    print worthless_corpus
#    print worthless_data


#def normalise(word):
#    return re.sub(r'\W+', '', word.lower())

#def tokenizer(str):
#    tokens = [normalise(word) for word in str.split(" ") if normalise(word).isalpha()]
#    allTokens = tokens
#    return allTokens


"""dictionary mapping between parent class, core belief classes, core beliefs and quotes"""


"""import loop through training data"""




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
