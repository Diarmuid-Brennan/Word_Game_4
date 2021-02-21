from ._anvil_designer import viewlogTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files

class viewlog(viewlogTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    log = anvil.server.call('display_log')
    self.display_errorlog_label.text = log
    # Any code you write here will run when the form opens.
    

  def review_rules_button_click(self, **event_args):
    open_form('rules')

