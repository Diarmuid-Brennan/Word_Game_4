import anvil.google.auth, anvil.google.drive, anvil.google.mail
from anvil.google.drive import app_files
import anvil.google.auth, anvil.google.drive, anvil.google.mail
from anvil.google.drive import app_files
import anvil.server
import random

file = str(app_files.words.get_bytes(), 'UTF-8')
file = file.split()

words = {line.strip("\n").replace("'s",'').lower() for line in file}
words = sorted(words)  # Ignore the empty word at the start of the list.

@anvil.server.callable
def find_possible_matches(pattern):
    """Given any pattern of the type "__a___b__c", this function
       looks up and returns all the potential matches for the
       pattern in the Linux dictionary of words."""

    def match_pattern(w, p):
        """Returns True if 'w' matches 'p', False otherwise."""
        letters = {k: v for k, v in enumerate(p) if v != "_"}
        return not any([w[i] != p[i] for i in letters.keys()])

    pattern = pattern.lower()  # Just in case...
    matches = [
        word  ## SELECT...
        for word in words  ## FROM...
        if len(word) == len(pattern) and match_pattern(word, pattern)  ## WHERE...
        ]
    return matches
  
@anvil.server.callable
def return_random_word():
    matches = [
        word  ## SELECT...
        for word in words  ## FROM...
        if len(word) >= 8 ##WHERE
        ]
    return random.choice(matches)
  
@anvil.server.callable
def check_input(answer,randomWord):
    response = ""
    tooSmallWords =[]
    foundWords =[]
    duplicateWords = set()
    misspeltWords= []
    invalidLetters = set()
    if(len(answer) != 7):
      response += "You have enterd an incorect number of words : " + str(len(answer)) + ", not 7 \n"
    for word in answer:
        if(len(word) < 4):
          tooSmallWords.append(word)
        for letter in word:
          if letter not in randomWord:
            invalidLetters.append(letter)
        matches = find_possible_matches(word)
        if(len(matches)== 0):
          misspeltWords.append(word)
        else:
          if word not in foundWords:
            foundWords.append(word)
          else:
            duplicateWords.append(word)
            
    if(len(foundWords) == 7 and len(answer)==7):
      return "Wellldone"
    else:
      return response
            
        
        
        
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  