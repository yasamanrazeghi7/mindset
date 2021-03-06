class Node(object):
    def __init__(self, name):
        self.name = name
        self.actions_dict = {}
        # for index, action in enumerate(self.actions):
        #     self.add_action(action, self.rewards[index], self.next_nodes[index])


    def add_action(self, action, reward, next_node):
        self.actions_dict[action] = (reward, next_node)


    def get_reward(self, action):
        """return tuple of (reward, target node)"""
        return self.actions_dict[action]

    def get_name(self):
        return self.name
