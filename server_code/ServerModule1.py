import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
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
    misspeltWords= []
    invalidLetters = set()
    duplicates = False
    exist = True
    
    if len(answer) != 7:
      response += "You have enterd an incorect number of words : " + str(len(answer)) + ", not 7 \n"
      
      
    for word in answer:
        checkWord = randomWord
        if len(word) < 4:
          tooSmallWords.append(word)
            
            
        matches = find_possible_matches(word)
        if len(matches)== 0:
          misspeltWords.append(word)
          exist = False
        
        if word == randomWord:
          response += "You cannot use the sourceword : " + randomWord + "\n"
          exist = False
          
        found = True  
        for letter in word:
          if letter in checkWord:
            checkWord = checkWord.replace(letter, "", 1)
          else:
            invalidLetters.add(letter)
            found = False
          
          
        if found == True and exist == True and len(word) > 3:
          if word not in foundWords:
            foundWords.append(word)
          else:
            duplicates = True
            
            
    if len(tooSmallWords) > 0:
      smallWord = ' '.join(tooSmallWords)
      response += "These words are too small : "+ smallWord + "\n"
    if len(misspeltWords) > 0 :
      misspelt = ' '.join(misspeltWords)
      response += "You misspelt these words : "+ misspelt + "\n"   
    if duplicates == True:
      duplcate =' '.join(answer)
      response += "You have entered duplcates in your list : "+ duplcate + "\n"
    if len(invalidLetters) > 0:
      invalidLetter = list(invalidLetters)
      invalid = ' '.join(invalidLetter)
      response += "You have usd invalid letters : "+ invalid + "\n"
      
    if(len(foundWords) == 7 and len(answer)==7):
      return foundWords
    else:
      return response
            
        
@anvil.server.callable
def add_score(player_data_dict):
  app_tables.topscores.add_row(
    **player_data_dict
  )        
        
@anvil.server.callable
def get_score_table():
  #return app_tables.topscores.search(tables.order_by("Time", ascending=True)) 
  position = 1 
  scores = app_tables.topscores.search(tables.order_by("Time", ascending=True))
  players = []
  for row in scores:
    Position = str(position)     
    playerDetails = {
                      'Position' : Position,
                        'Time' : row['Time'],
                        'Who' : row['Who'],
                        'SourceWord' : row['SourceWord'],
                        'Matches' : row['Matches']
                      } 
    position += 1
    players.append(playerDetails)
  return players

@anvil.server.callable
def find_player_position(playerList, name, sourceword):
    for i, dic in enumerate(playerList):
        if dic['Who'] == name and dic['SourceWord'] == sourceword:
            return i + 1 
  

  
  
  
  
  
  
  
  
  
  
  
  
  