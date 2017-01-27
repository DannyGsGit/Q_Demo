from ale_python_interface import ALEInterface
import numpy as np
import sys

ale = ALEInterface()

# Set ALE configuration for this game
ale.setInt(b"random_seed", 1018)
ale.setInt(b"frame_skip", 4)

# Load the ROM
ale.loadROM(b"roms/freeway.bin")
legal_actions = ale.getMinimalActionSet()

print("legal_actions")
print(legal_actions)

action_map = dict()
for i in range(len(legal_actions)):
    action_map[legal_actions[i]] = i

print("action_map")
print(action_map)
print(type(action_map))


batch = 32
num_act = 4
actions = np.zeros([batch])
for i in range(batch):
    actions[i] = np.random.randint(0,4, size = 1)
print(actions)

actions_onehot = np.zeros((batch, num_act))
actions_int = actions.astype(int)
for i in range(batch):
    #print(type(actions_int[i]))
	actions_onehot[i,actions_int[i]] = 1
print(actions_onehot)
