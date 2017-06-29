from node import Node


class Task(object):
    def __init__(self, file_name):
        self.actions = []
        self.nodes = []
        self.create_task(file_name)

    def create_task(self, file_name):
        i_file = open(file_name, 'r')
        line = i_file.readline()
        tokens = line.split()
        node_number = int(tokens[0])
        action_number = int(tokens[1])
        for a in range(action_number):
            self.actions.append(tokens[a+2])
        for n in range(node_number):
            new_node = Node(n+1)
            self.nodes.append(new_node)
        for n in range(node_number):
            for a in range(action_number):
                line = i_file.readline()
                tokens = line.split()
                self.nodes[n].add_action(tokens[1], int(tokens[3]), tokens[2])
        i_file.close()

    def __str__(self):
        return "%d %d %s" % (len(self.nodes), len(self.actions), ' '.join(self.actions))

    def write_task_file(self, file_name):
        r_file = open(file_name, 'w')
        r_file.write("%d %d %s \n" % (len(self.nodes), len(self.actions), ' '.join(self.actions)))
        for n in self.nodes:
            for a in self.actions:
                r_file.write("%d %c %d %d \n" % (int(n.get_name()), a, int(n.get_reward(a)[1]), int(n.get_reward(a)[0])))
        r_file.close()

