class Sequence:
    '''FIFO list with basic queue functionality'''
    def __init__(self):
        self.commands = []

    def isEmpty(self):
        return self.commands == []

    def enqueue(self, command):
        self.commands.insert(0, command)

    def dequeue(self):
        return self.commands.pop()

    def size(self):
        return len(self.commands)

    def listAll(self):
        return self.commands
