from task import Task
from trial import Trial
from game import Game
from agent import *

TOTAL_TRIAL_NUMBER = 100
START_NODE = 1
TRIAL_LENGTH = 3


def main():
    normal_task = Task("input.txt")
    agent_test1 = RandomAgent(normal_task)
    trials = []
    for a in range(TOTAL_TRIAL_NUMBER):
        trial = Trial(TRIAL_LENGTH, normal_task.nodes[START_NODE -1])
        trials.append(trial)
    first_game = Game(normal_task, agent_test1, trials)

    first_game.plot_rewards()
    first_game.perform_game()
    first_game.plot_rewards()




if __name__ == '__main__':
    main()