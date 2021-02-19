from ._anvil_designer import top10Template
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files

class top10(top10Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    players = anvil.server.call('get_score_table')
    outputList = players[:10]
    self.repeating_panel_scores.items = outputList
    # Any code you write here will run when the form opens.
    

  def play_again_button_click(self, **event_args):
    open_form('startgame')

  def review_rules_button_click(self, **event_args):
    open_form('rules')


  