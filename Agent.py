import random
class Agent:
    def __init__(self):
        self.epsilon = 0.3
        self.actions = []
        self.state = 0

    def act(self):
        action = None
        if(random.random() > self.epsilon):
            action = random.choice(self.actions)
            return action
        else:
            return self.model(self.state)

    def model(self,state):
        return None