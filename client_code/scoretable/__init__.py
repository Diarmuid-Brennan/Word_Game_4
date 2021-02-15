from ._anvil_designer import scoretableTemplate
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files

class scoretable(scoretableTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run when the form opens.
    

  def play_again_button_click(self, **event_args):
    open_form('startgame')

  def review_rules_button_click(self, **event_args):
    open_form('rules')


