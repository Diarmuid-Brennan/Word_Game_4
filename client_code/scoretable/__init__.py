from ._anvil_designer import scoretableTemplate
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files

class scoretable(scoretableTemplate):
  def __init__(self, name, sourceword, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    
    position = 1 
    scores = anvil.server.call('get_score_table')
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
      
    #playerPosition = find_player_position(players, name, sourceword)
    playerPosition = anvil.server.call('find_player_position', players, name, sourceword)
    print(playerPosition)
    totalPlayers = len(players)  
    self.position_label.text = "You are placed in position " + str(playerPosition) + " out of " + str(totalPlayers) + " players."
    outputList = players[:10]
    self.repeating_panel_scores.items = outputList
  
  
  
  def play_again_button_click(self, **event_args):
    open_form('startgame')

  def review_rules_button_click(self, **event_args):
    open_form('rules')

 
