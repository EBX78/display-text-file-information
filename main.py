import time
start_time = time.time()

# import nltk
# nltk.download('punkt')
# nltk.download('stopwords')

import os
import nltk
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
# from sklearn import countvectorize

curdir = os.getcwd()
my_list = open("test.txt").readlines()

sp = PorterStemmer() # This method extracts the root of the word
stop_words = set(stopwords.words("english")) # Make a list of stop words

sent_count = 0
word_count = 0
root_count = 0
stop_count = 0
# Call each list item
for item in my_list:
    s_c = len(nltk.sent_tokenize(item))
    if item != "\n":
        word_tokens = word_tokenize(item) # Extract the words of each item and make a list for words of each sentence

        # Remove extra symbols and extensions from word
        for i in word_tokens:
            if i in [",", ":", "-", "'s", "."]:
                word_tokens.remove(i)

        root_word_list = [] # Make a list for root words
        for word in word_tokens: # Call each word from the list
            rootword = sp.stem(word) # Use this method to extract the root of the word
            root_word_list.append(rootword) # add the root words to the list we made in line 29

        root_stop_list = [] # New list for rooted words that Remove stop words
        stopword_list = [] # new List for stop words
        count = 0 # to count stop words in sentences
        for word in word_tokens:
            rootword = sp.stem(word)
            root_stop_list.append(rootword)

            # Move stop words to new list
            if word in stop_words:
                stopword_list.append(rootword)
                count += 1

        # Remove stop words from the list of root words
        for i in stopword_list:
            root_stop_list.remove(i)

        word_count += len(word_tokens)
        root_count += len(root_stop_list)
        stop_count += count
    sent_count += s_c
        

word_avg = round(word_count / sent_count,3)

print("Sentences:    %i"%(sent_count))
print("Words:    %i"%(word_count))
print("Root words:    %i"%(root_count))
print("Stop words:    %i"%(stop_count))
print("Word per sentence: %f"%(word_avg))

ftime = ((time.time() - start_time) // 60)
stime = ((time.time() - start_time) % 60)
print("\n%im %is" % (ftime, stime))
