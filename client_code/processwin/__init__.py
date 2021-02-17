from ._anvil_designer import processwinTemplate
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files

class processwin(processwinTemplate):
  sourceword = ''
  answerlist = []
  time = 0
  def __init__(self, answerlist, sourceword, time, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.sourceword = sourceword
    self.answerlist = answerlist
    self.time = time
    self.time_label.text = "Congratulations! You took " + str(time) + " seconds." 
    # Any code you write here will run when the form opens.
    

  def record_score_button_click(self, **event_args):
    name = self.input_name_box.text
    
    player_data = {
      "Time" : self.time,
      "Who" : name,
      "SourceWord" : self.sourceword,
      "Matches" : self.answerlist
    }
    
    anvil.server.call('add_score', player_data)
    open_form('scoretable', name, self.sourceword)
