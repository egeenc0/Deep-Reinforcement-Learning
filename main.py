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
for i in range(1000):
    condition = False
    if epsilon > random.random():
        while(not condition):
            agent.position[0] = random.choice([agent.position[0] + 1, agent.position[0] - 1,
                                              agent.position[0]])
            agent.position[1] = random.choice([agent.position[1] + 1, agent.position[1] - 1,
                                              agent.position[1]])
            special = not (agent.position[0] == 2 and agent.position[1] == 2)
            condition_x = (agent.position[0] >= 0 and agent.position[0] <= 3) and special
            condition_y = (agent.position[1] >= 0 and agent.position[1] <= 3) and special
            condition = condition_x and condition_y
            if agent.position[0] == 3 and agent.position[1] == 3:
                print("Agent solved the maze at", i, " steps")
                break
    print("Agent's position in the maze : ", agent.position)
