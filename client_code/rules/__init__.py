from ._anvil_designer import rulesTemplate
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
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

  def view_table_button_click(self, **event_args):
    open_form('top10')

  def view_log_button_click(self, **event_args):
    open_form('viewlog')






