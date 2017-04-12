# -*- coding: utf-8 -*-
"""
Created on Wed Apr 12 18:21:56 2017

@author: macan
"""
## this code was built bit by bit in class this date. 

# ***** first iteration *********
## read in the word dictonary
#words = open("spell.words").readlines()
## strip all of the new line characters
## lambda is a throwaway function, map applies code to every line, i.e.: strip to every line
#words = map(lambda x: x.strip(), words)
#
#print('zygotic' in words)
#print('mistastas' in words) # made up word!

# ******** second iteration **********
# ******* improved coding, using functions so reusable. Any dictonary can be used *********
#def load_words(file_name):
#    words = open(file_name).readlines()
#    words = map(lambda x: x.strip(), words)
#    return words
#
## more memory efficient coding of above, no variable 'words' created. Same job!
#def load_words2(file_name):
#    return map(lambda x: x.strip(), open(file_name).readlines())
#
#def check_word(words, word):
#    return word in words
#
#def check_words(words, sentence):
#    words_to_check = sentence.split(' ')
#    for word in words_to_check:
#        if not check_word(words, word):
#            print('Word is misspelt: ' + word)
#            return False
#    return True
#
#
#words = load_words('spell.words')
## now check if the word zygotic is a word
#print(check_word(words, 'zygotic'))
#print(check_word(words, 'mistasdas'))
#print(check_words(words, 'zygotic mistasdas elementary bomzzzdas'))

## ************ third iteration **********
#class SpellChecker(object):
#    def __init__(self):
#        self.words = []
#    
#    def load_words(self, file_name):
#        self.words = open(file_name).readlines()
#        self.words = map(lambda x: x.strip(), self.words)
#    
#    def check_word(self, word):
#        return word.strip('.').lower() in self.words
#    
#    def check_words(self, sentence):
#        words_to_check = sentence.split(' ')
#        failed_words = [] # added afterwards based on unittest
#        for word in words_to_check:
#            if not self.check_word(word):
#                print('Word is misspelt: ' + word)
#                failed_words.append(word) # added afterwards based on unittest
#        return failed_words
#
## enable so that this is only called when the script run from the command line
#if __name__ == '__main__': 
#    spell_checker = SpellChecker()
#    spell_checker.load_words('spell.words')
#    # now check if the word zygotic is a word
#    print(spell_checker.check_word('zygotic'))
#    print(spell_checker.check_word('mistasdas'))
#    print(spell_checker.check_words('zygotic mistasdas elementary'))

# ************ fourth iteration **********
class SpellChecker(object):
    def __init__(self):
        self.words = []
    
    def load_file(self, file_name):
        lines = open(file_name).readlines()
        return map(lambda x: x.strip().lower(), lines)
    
    def load_words(self, file_name):
        self.words = self.load_file(file_name)
    
    def check_word(self, word):
        return word.strip('.').lower() in self.words
    
    # index = 0 is set here so that the function can be called for one line and index defaults to 0
    def check_words(self, sentence, index=0):
        words_to_check = sentence.split(' ')
        caret_position = 0
        failed_words = [] # added afterwards based on unittest
        for word in words_to_check:
            if not self.check_word(word):
                print('Word is misspelt {0} on line {1} at pos {2}.').format(word, index+1,caret_position+1)
                failed_words.append({'word':word, 'line': index+1, 'pos': caret_position+1}) # added afterwards based on unittest
            # update the caret position to be the length of the word plus 1 for the split character.
            caret_position = caret_position + len(word) + 1

        return failed_words
    
    def check_document(self, file_name):
        self.sentences = self.load_file(file_name)
        failed_words_in_sentences = []
        index = 0
        for index, sentence in enumerate(self.sentences):
            failed_words_in_sentences.extend(self.check_words(sentence, index))
            index = index + 1
        return failed_words_in_sentences


# enable so that this is only called when the script run from the command line
if __name__ == '__main__': 
    spell_checker = SpellChecker()
    spell_checker.load_words('spell.words')
    # now check if the word zygotic is a word
    print(spell_checker.check_word('zygotic'))
    print(spell_checker.check_word('mistasdas'))
    print(spell_checker.check_words('zygotic mistasdas elementary'))