from ._anvil_designer import startgameTemplate
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files

import time

import anvil.server


class startgame(startgameTemplate):
  starttime = 0
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    
    randomWord = anvil.server.call('return_random_word')
    self.sourceword_box.text = randomWord
    self.starttime = int(round(time.time()))
    # Any code you write here will run when the form opens.
    
    
    
  def submit_button_click(self, **event_args):
    answer = self.answers_box.text
    answer = answer.split()
    answer = [word.lower() for word in answer]
 
    random = self.sourceword_box.text
    endtime = int(round(time.time()))

    resulttime =  endtime -  self.starttime
    
    user_agent = anvil.http.request(anvil.server.get_api_origin() + '/get-user-agent', json=True)['ua']
   
    result = anvil.server.call('check_input', answer, random, user_agent)
    if isinstance(result, str):  
      open_form("processwords", result)
    else:
      open_form("processwin", result, random, resulttime)
