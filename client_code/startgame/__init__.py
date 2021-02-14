from ._anvil_designer import startgameTemplate
from anvil import *
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.server

randomWord = anvil.server.call('return_random_word')
class startgame(startgameTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    #randomWord = anvil.server.call('return_random_word')

    self.sourceword_box.text = "Your word is :    " + randomWord
    # Any code you write here will run when the form opens.
    

  def submit_button_click(self, **event_args):
    answer = self.answers_box.text
    answer = answer.split()
    result = anvil.server.call('check_input', answer, randomWord)
    print(type(result))
    if isinstance(result, str):  
      open_form("processwords", result)
    else:
      open_form("processwin", result)
