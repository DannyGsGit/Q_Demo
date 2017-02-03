# The frame environment

import numpy as np
import os, json
import pandas as pd





class frame(object):
    def __init__(self, base_bom):
        # Get the basic bom (e.g. frame + suspension) from source
        pass
    
    def state(self):
        pass
    
    def apply_action(self, action_input):
        pass
    
    
    



    
class parts_bin(object):
    def __init__(self, bom_name, bom_directory = 'Environment/BoMs/', part_directory = 'Environment/Parts/'):
        
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




    
    def state(self):
        pass
    
    def get_part(self):
        pass
    






class action_map(object):
    def __init__(self):
        # Define action set
        
        pass
    
    def get_action(self, input):
        pass
    








class reward(object):
    def __init__(self):
        # Reward = 0
        pass
    
    def score_violations (self, frame_state):
        pass
    
    def score_blue_boc(self, frame_state):
        pass
    
    def score_red_boc(self, frame_state):
        pass
    








class display(object):
    def __init__(self):
        # Create display window
        pass
    
    def render_frame(self, frame_state):
        pass
    
    def render_parts_bin(self, part_bin_state):
        pass
    
    

