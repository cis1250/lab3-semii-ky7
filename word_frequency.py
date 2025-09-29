#!/usr/bin/env python3

# Word frequency exercise
# TODO: (Read detailed instructions in the Readme file)
# 1. Prompt the user: Ask the user to enter a sentence.
user_inp=input("Enter a valid sentence: ")
# 2. Split the sentence
user_inp = user_inp.replace('.', ',')
spl_ui=user_inp.split(',')
print(spl_ui)
# 3. Create lists to store words and their corresponding frequencies
words=[]
freq=[]
# 4. Iterate through words and update frequencies
all_words = []
for phrase in spl_ui:
    words_in_phrase = phrase.strip().split()
    all_words.extend(words_in_phrase)        
    


for word in all_words:
    word = word.lower()  

    if word in words:
        idx = words.index(word)  
        freq[idx] += 1           
    else:
        words.append(word)      
        freq.append(1)   
for i in range(len(words)): 
    print(f"{words[i]}: {freq[i]}")


import re

#This is a function that checks if a text qualifies as a sentence. You do not need to modify this!
def is_sentence(text):
    # Check if the text is not empty and is a string
    if not isinstance(text, str) or not text.strip():
        return False

    # Check for starting with a capital letter
    if not text[0].isupper():
        return False

    # Check for ending punctuation
    if not re.search(r'[.!?]$', text):
        return False

    # Check if it contains at least one word (non-whitespace characters)
    if not re.search(r'\w+', text):
        return False

    return True

user_sentence = input("Enter a sentence: ")

while (is_sentence(user_sentence) == False):
    print("This does not meet the criteria for a sentence.")
    user_input = input("Enter a sentence: ")
    
