POSSIBLE_STATES = ['LOW', 'AVG', 'HIGH']
N_STATES = len(POSSIBLE_STATES)

class Node:
    def __init__(self, name):
        self.name = name.upper()
        self.previousNodes = []
        self.stateProb = {}
        self.transitionProb = {}

    def createState(self, stateName, probability):
        stateName = stateName.upper()
        if (stateName in POSSIBLE_STATES):
            self.stateProb[stateName] = probability
        else:
            raise ValueError("Invalid state: " + stateName +
                    ". Valid states are: " + str(POSSIBLE_STATES))
    
    def getStateProb(self, stateName):
        stateName = stateName.upper()
        if (stateName not in self.stateProb):
            raise KeyError('State: ' + stateName + ' has no value.')

        else:
            return self.stateProb[stateName]

    def setTransition(self, prevStates, prob):
        #prevStates is tuple
        #i.e. (LOW, LOW) or (LOW, AVG)
        self.transitionProb[prevStates] = [float(a) for a in prob]
