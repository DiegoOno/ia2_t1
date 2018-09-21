POSSIBLE_STATES = ['LOW', 'AVG', 'HIGH']

class Node:
    def __init__(self, state):
        if (state.upper() in POSSIBLE_STATES):
            self.state = state
        else:
            raise ValueError("Invalid state: " + state +
                    ". Valid states are: " + str(POSSIBLE_STATES))
