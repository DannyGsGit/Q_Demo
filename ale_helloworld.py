###############################################################################
# Getting started with ALE
# Source: https://github.com/bbitmaster/ale_python_interface/wiki/Code-Tutorial
###############################################################################

import numpy as np
import sys
from ale_python_interface import ALEInterface

ale = ALEInterface()

# Set ALE configuration for this game
ale.setInt(b"random_seed", 1018)
ale.setInt(b"frame_skip", 4)

# Load the ROM
ale.loadROM(b"freeway.bin")
legal_actions = ale.getLegalActionSet()

# Take random actions until the game is over
for episode in range(10):
    total_reward = 0.0
    while not ale.game_over():
        a = legal_actions[np.random.randint(legal_actions.size)]
        reward = ale.act(a);
        total_reward += reward
    print("Episode " + str(episode) + " ended with score: " + str(total_reward))
    ale.reset_game()

# Retrieve RAM and screen state
ram_size = ale.getRAMSize()
ram = np.zeros((ram_size),dtype=np.uint8)
ale.getRAM(ram)

(screen_width,screen_height) = ale.getScreenDims()
screen_data = np.zeros(screen_width*screen_height,dtype=np.uint32)
ale.getScreenRGB(screen_data)
