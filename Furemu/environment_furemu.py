# The frame environment

import numpy as np
import os, json
import pandas as pd





class frame(object):
    def __init__(self, base_bom):
        # Get the basic bom (e.g. frame + suspension) from source
        pass
    
    def state(self):
        # State of the frame with part placements (+ weights?)
        pass
    
    def apply_action(self, action_input):
        # Move & place parts on frame according to actions
        pass
    
    
    



    
class parts_bin(object):
    def __init__(self, bom_name, bom_directory = 'Environment/BoMs/', part_directory = 'Environment/Parts/'):
        # We will initialize the parts bin with a BoM (i.e. heuristic equivalent of gathering parts for a build according to BoM)
        
        # Get the parts bom from file
        with open(os.path.join(bom_directory, bom_name), 'r') as f:
            parts = json.load(f)
        
        # Get the parts list from the JSON BOM
        part_files = parts["parts"]
        

        # Pre-allocate pandas DF for part list
        self.part_data = pd.DataFrame(columns = ['group', 'pn', 'geom_type', 'geom_xy', 'weight'])

        # Read the json files in the part list to get part data
        for index, js in enumerate(part_files):
            with open(os.path.join(part_directory, js), 'r') as json_file:
                json_text = json.load(json_file)
                group = json_text['Group']
                pn = json_text['PN']
                geom_type = json_text['Geom']['type']
                geom_xy = json_text['Geom']['coordinates']
                weight = json_text['Weight']
                self.part_data.loc[index] = [group, pn, geom_type, geom_xy, weight]
                
        exit(1)

    
    def bin_state(self):
        # Returns the contents of the parts_bin
        pass
    
    def take_part_from_bin(self):
        # This function will take the top part from the parts_bin and remove it from the list
        pass
    






class action_map(object):
    def __init__(self):
        # Define action set: left, right, up, down, flip_x, flip_y, place
        pass
    
    def get_action(self, input):
        # Map inputs to actions
        pass
    








class reward(object):
    def __init__(self):
        # Initialize with reward = 0
        self.reward = 0
        exit(1)
    
    def score_violations (self, frame_state):
        # Penalize the score if a constraint is violated
        pass
    
    def score_blue_boc(self, frame_state):
        # Give points for placing blue parts correctly
        pass
    
    def score_red_boc(self, frame_state):
        # Give points for placing red parts correctly
        pass
    








class display(object):
    def __init__(self):
        pass
    
    def render_frame(self, frame_state):
        # Render the current frame state
        pass
    
    def render_parts_bin(self, part_bin_state):
        # Render the current bin state
        pass
    
    



