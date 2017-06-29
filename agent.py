import random

MINVAL = -1000


class Agent(object):

    def __init__(self, task):
        self.task = task

    def give_action(self, trial):
        pass


class RandomAgent(Agent):
    def give_action(self, trial):
        secure_random = random.SystemRandom()
        return secure_random.choice(self.task.actions)


class GreedyAgent(Agent):
    def give_action(self, trial):
        c_node = self.trial.current_state
        m_r = MINVAL
        for a in self.task.actions:
            reward = c_node.get_reward(a)[0]
            if reward > m_r:
                m_r = reward
                r_action = c_node.get_reward(a)[1]
        return r_action
