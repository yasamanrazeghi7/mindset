from trial import State
import matplotlib.pyplot as plt;

plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

class Game(object):
    def __init__(self, task, agent, trials):
        self.task = task
        self.trials = trials
        self.agent = agent
        self.total_reward = 0
        self.state = State.NOT_STARTED

    def perform_game(self):
        for t in self.trials:
            while t.state != State.FINISHED:
                act = self.agent.give_action(t)
                t.do_action(act)
            self.total_reward += t.total_reward

    def get_total_reward(self):
        return self.total_reward

    def plot_rewards(self):
        performance_list = []
        x_axis = []
        i = 1
        for t in self.trials:
            performance_list.append(t.get_reward())
            x_axis.append(i)
            i += 1

        print(performance_list)
        y_pos = np.arange(len(performance_list))
        plt.bar(y_pos, performance_list, align='center', alpha=0.5)
        plt.xticks(y_pos, x_axis)
        plt.ylabel('Rewards')
        plt.title(self.state)
        plt.show()


