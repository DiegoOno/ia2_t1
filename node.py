POSSIBLE_STATES = ['LOW', 'AVG', 'HIGH']

class Node:
    def __init__(self, name):
        self.name = name
        self.probabilities = []
        self.parents = []
        self.state = ''

    def setProbabilities(self, dict):
        self.probabilities = dict

    def setParents(self, parentsList):
        self.parents = parentsList

    def setState(self, state):
        self.state = state


