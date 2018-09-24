from node import Node, N_STATES

FILE = "data/sachs.txt"
#FILE = "data/test.txt"

bayesianTree = {}
initialNodes = {}

#Used later to map the tree
#stateTransition[state] = previousStates
stateTransitions = {}

def main():
    #Something like:
    with open(FILE) as _file:
        for line in _file:
            line = line.split()
            if (len(line) == 0):
                continue
            if (len(line) == 1):
                node = Node(line[0])
                line = _file.readline().split()
                while (line[0] != 'end'):
                    node.createState(line[0], float(line[1]))
                    line = _file.readline().split()
                #endfor
                
                bayesianTree[node.name] = node
                initialNodes[node.name] = node
            #endif
            else:
                node = Node(line[0])
                if(line[0] not in stateTransitions):
                    name = line[0].upper()
                    stateTransitions[name] = []

                for _next in line[1:]:
                    stateTransitions[name].append(_next.upper())
                
                numPrevs = len(stateTransitions[name])
                bayesianTree[node.name] = node

                line = _file.readline().split()
                while (line[0] != 'end' ):
                    prevStates = tuple(line[:numPrevs])
                    probs = line[numPrevs:]
                    node.setTransition(prevStates, probs)
                    line = _file.readline().split()
                #endwhile
            #endelse
        #endfor
    #endwith

    _file.close()

    #Testing
    print("\n%i nodes detected." % (len(bayesianTree)))
    print("%i initial nodes detected: " % (len(initialNodes)), end="")
    for key, value in initialNodes.items():
        print(key, end=" ")
    print("\n")
    
    print("Bayesian tree structure: ")
    for key, value in stateTransitions.items():
        print(value, end=' -> ')
        print(key)

        for state in value:
            bayesianTree[key].previousStates.append(bayesianTree[state])

    print('\n\n')
    
    print("DEBUGGING NODE MEK:\n\n")

    print("Previous states:")
    for i in bayesianTree['MEK'].previousStates:
        print(i.name, end=' ')
    
    print('\n')

    for key, value in bayesianTree['MEK'].transitionProb.items():
        print(key, end=': ')
        print(value)

    print("\n\nEND DEBUGGING")

#endmain

if (__name__ == '__main__'):
    main()
