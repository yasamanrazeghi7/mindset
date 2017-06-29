from enum import Enum


class State(Enum):
    NOT_STARTED = 1
    IN_THE_MIDDLE = 2
    FINISHED = 3


class Trial(object):
    def __init__(self, moves_number, start_node):
        self.moves_number = moves_number
        self.start_node = start_node
        self.current_node = start_node
        self.total_reward = 0
        self.remaining_moves = moves_number
        self.state = State.NOT_STARTED

    def get_current_node(self):
        return self.current_node

    def get_reward(self):
        return self.total_reward

    def get_state(self):
        return self.state

    def do_action(self, action):
        if self.state == State.FINISHED:
            print ("the trial is finished")
            return
        self.state = State.IN_THE_MIDDLE
        reward, n_node = self.current_node.get_reward(action)
        self.total_reward += reward
        self.current_node = n_node
        self.remaining_moves = self.remaining_moves - 1;
        if self.remaining_moves == 0:
            self.state = State.FINISHED

    def do_many_actions(self, actions):
        for a in actions:
            self.do_action(a)
