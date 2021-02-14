from ._anvil_designer import processwordsTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files

class processwords(processwordsTemplate):
  def __init__(self, display, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.output_label.text = display
    # Any code you write here will run when the form opens.
    

  def play_again_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form("startgame")

  def button_2_click(self, **event_args):
    open_form("rules")


