import random
from sys import maxint


class Agent(object):

    def __init__(self, task, trial):
        self.task = task
        self.trial = trial

    def give_action(self):
        pass


class RandomAgent(Agent):
    def give_action(self):
        secure_random = random.SystemRandom()
        return secure_random.choice(self.task.actions)


class GreedyAgent(Agent):
    def give_action(self):
        c_node = self.trial.current_state
        m_r = -maxint-1
        for a in self.task.actions:
            reward = c_node.get_reward(a)[0]
            if reward > m_r:
                m_r = reward
                r_action = c_node.get_reward(a)[1]
        return r_action
