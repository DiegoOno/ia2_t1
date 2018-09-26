POSSIBLE_STATES = ['LOW', 'AVG', 'HIGH']

class Node:
    stateProb = {}

    def __init__(self, name):
        self.name = name
        self.probabilities = []
        self.parents = []
        self.state = ''

    def createState(self, stateName, probability):
        if (stateName.upper() in POSSIBLE_STATES):
            self.stateProb[stateName] = probability
        else:
            raise ValueError("Invalid state: " + stateName +
                    ". Valid states are: " + str(POSSIBLE_STATES))

    def setProbabilities(self, dict):
        self.probabilities = dict

    def setParents(self, parentsList):
        self.parents = parentsList

    def setState(self, state):
        self.state = state

    def getStateProb(self, stateName):
        return self.stateProb[stateName]

