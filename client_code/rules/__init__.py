from ._anvil_designer import rulesTemplate
from anvil import *
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.server
from ..startgame import startgame

class rules(rulesTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run when the form opens.

  def play_game_button_click(self, **event_args):
      open_form("startgame")




