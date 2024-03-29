import random
import numpy as np

class Agent:
    def __init__(self):
        self.position = [0, 1]

agent = Agent()

R_table = [
    [-1, 0, 0, -1],
    [-1, 0, 0, -1],
    [-1, 0, -1, -1],
    [-1, 0, 0, 100]
]
Q = np.zeros((4, 4, 4))  # 4x4 grid with 4 actions per state
actions = [(0, -1), (0, 1), (-1, 0), (1, 0)]  # up, down, left, right

epsilon = 0.3
learning_rate = 0.4
gamma = 0.9

def get_valid_actions(position):
    valid_actions = []
    for idx, (dx, dy) in enumerate(actions):
        new_x, new_y = position[0] + dx, position[1] + dy
        if 0 <= new_x < 4 and 0 <= new_y < 4 and R_table[new_x][new_y] != -1:
            valid_actions.append(idx)
    return valid_actions

def update_q(current_position, action, reward, new_position):
    future_rewards = Q[new_position[0], new_position[1]]
    Q[current_position[0], current_position[1], action] += learning_rate * (
        reward + gamma * np.max(future_rewards) - Q[current_position[0], current_position[1], action])

def main():
    for i in range(1000):
        current_position = agent.position
        if random.random() < epsilon:
            # Explore: choose a random action from the valid actions
            valid_actions = get_valid_actions(current_position)
            action = random.choice(valid_actions)
        else:
            # Exploit: choose the best action from Q-table
            action = np.argmax(Q[current_position[0], current_position[1]])

        # Perform the action
        new_x, new_y = current_position[0] + actions[action][0], current_position[1] + actions[action][1]
        new_position = [new_x, new_y]
        agent.position = new_position

        # Get the reward
        reward = R_table[new_x][new_y]

        # Update Q-table
        update_q(current_position, action, reward, new_position)

        if new_position == [3, 3]:
            print(f"Agent solved the maze at {i} steps")
            break
        print("Agent's position in the maze:", agent.position)

if __name__ == "__main__":
    main()
