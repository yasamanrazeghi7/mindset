class Trial(object):
    def __init__(self, moves_number, start_state):
        self.moves_number = moves_number
        self.start_state = start_state
        self.current_state = start_state
        self.total_reward = 0
        self.end_state = None
        self.remaining_moves = moves_number
        self.state = "not_started"

    def get_current_state(self):
        return self.current_state

    def get_reward(self):
        return self.total_reward

    def get_state(self):
        return self.state

    def do_action(self, action):
        if self.state == "finished":
            print ("the trial is finished")
            return
        self.state = "in_the_middle"
        self.remaining_moves = self.remaining_moves - 1;
        if self.remaining_moves == 0:
            self.state = "finished"
        [reward, n_node] = self.current_state.get_reward( action)
        self.total_reward += reward
        self.current_state = n_node

    def do_many_actions(self, actions):
        for a in actions:
            self.do_action(a)