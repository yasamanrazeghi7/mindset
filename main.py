from task import Task


def main():
    normal_task = Task("input.txt")
    print (normal_task.nodes.__len__())
    print(normal_task.actions.__len__())
    print(normal_task.actions)
    normal_task.print_task_file("output.txt")
    print(normal_task)

if __name__ == '__main__':main()