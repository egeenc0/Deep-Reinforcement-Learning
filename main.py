import tensorflow
import random
import gym

from Agent import Agent

agent = Agent()

R_table = [
    [-1, 0, 0, -1],
    [-1, 0, 0, -1],
    [-1, 0, -1, -1],
    [-1, 0, 0, 100]
]
agent.position = [0, 1]

epsilon = 0.3
condition = False
for i in range(100):
    if epsilon > random.random():
        while(not condition):
            agent.position[0] = random.choice([agent.position[0] + 1, agent.position[0] - 1,
                                              agent.position[0]])
            agent.position[1] = random.choice([agent.position[1] + 1, agent.position[1] - 1,
                                              agent.position[1]])
            condition_x = (agent.position[0] >= 0 and agent.position[0] <= 3)
            condition_y = (agent.position[1] >= 0 and agent.position[1] <= 3)
            condition = condition_x and condition_y
    print("Agent's position in the maze : ",agent.position)
