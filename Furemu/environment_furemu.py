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
        # Create display window
        import pygame

        pygame.init()

        # Define the colors we will use in RGB format
        black = (  0,   0,   0)
        white = (255, 255, 255)
        blue =  (  0,   0, 255)
        green = (  0, 255,   0)
        red =   (255,   0,   0)
        color_background = (66, 244, 226)
         
        # Set the height and width of the screen
        size = [800, 600]
        screen = pygame.display.set_mode(size)
         
        pygame.display.set_caption("Hirachi Furemu Environment")
        
        #Loop until the user clicks the close button.
        done = False
        clock = pygame.time.Clock()
         
        while not done:
         
            # This limits the while loop to a max of 10 times per second.
            # Leave this out and we will use all CPU we can.
            clock.tick(10)
             
            for event in pygame.event.get(): # User did something
                if event.type == pygame.QUIT: # If user clicked close
                    done=True # Flag that we are done so we exit this loop
         
            # All drawing code happens after the for loop and but
            # inside the main while done==False loop.
             
            # Clear the screen and set the screen background
            screen.fill(color_background)
            
            # This MUST happen after all the other drawing commands.
            pygame.display.flip()
            
        pygame.quit()
 
        
        exit(1)
    
    def render_frame(self, frame_state):
        # Render the current frame state
        pass
    
    def render_parts_bin(self, part_bin_state):
        # Render the current bin state
        pass
    
    



