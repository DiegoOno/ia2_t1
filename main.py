from node import Node, N_STATES, POSSIBLE_STATES

FILE = "data/sachs.txt"
INPUT = "data/input.txt"
#FILE = "data/test.txt"

bayesianTree = {}
initialNodes = {}
#endingNodes = {}

import itertools

#Used later to map the tree
#stateTransition[node] = previousNode
nodeTransitions = {}

nodesNames = []
notEndingNodes = []

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
                nodesNames.append(node.name)

                while (line[0] != 'end'):
                    node.createState(line[0], float(line[1]))
                    line = _file.readline().split()
                #endfor
                
                bayesianTree[node.name] = node
                initialNodes[node.name] = node
            #endif
            else:
                node = Node(line[0])
                nodesNames.append(node.name)
                if(line[0] not in nodeTransitions):
                    name = line[0].upper()
                    nodeTransitions[name] = []

                for _next in line[1:]:
                    _next = _next.upper()
                    nodeTransitions[name].append(_next)
                    if (_next not in notEndingNodes):
                        notEndingNodes.append(_next)
                
                numPrevs = len(nodeTransitions[name])
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

    endingNodes = [i for i in nodesNames if i not in notEndingNodes]

    print("%i ending nodes detected: " % (len(endingNodes)), end="")
    for n in endingNodes:
        print(n, end=" ")
    print("\n")

    print("Bayesian tree structure: ")
    for key, value in nodeTransitions.items():
        print(value, end=' -> ')
        print(key)

        for node in value:
            bayesianTree[key].previousNodes.append(bayesianTree[node])

    print('\n')

    '''
    print("DEBUGGING NODE MEK:\n\n")

    print("Previous states:")
    for i in bayesianTree['MEK'].previousNodes:
        print(i.name, end=' ')
    
    print('\n')

    for key, value in bayesianTree['MEK'].transitionProb.items():
        print(key, end=': ')
        print(value)

    print("\n\nEND DEBUGGING")
    '''

    try:
        _input = open(INPUT)
    except IOError:
        print("Couldn't read the file.'")
        exit()

    knowledgeBase = {}

    for line in _input:
        line = line.split()

        nodeName = line[0].upper()
        nodeState = line[1].upper()

        if (nodeName not in knowledgeBase):
            knowledgeBase[nodeName] = nodeState

    jointProb = 1.0
    nodesLeft = endingNodes
    addedNodes = []

    while (True):
        for key, value in bayesianTree.items():
            index = 0
            if (value.name in initialNodes):
                if (key in knowledgeBase):
                    print("P(" + value.name + ")" + '[' + knowledgeBase[value.name] + '] = ', end='')
                    print(value.getStateProb(knowledgeBase[value.name]))
                else:
                    for state, prob in value.stateProb.items():
                        print("P(" + value.name + ")" + '[' + state + '] = ', end='')
                        print(prob)
                    print()
            
            else:
                states = []
                for prevNode in value.previousNodes:
                    if (prevNode.name in knowledgeBase):
                        states.append([knowledgeBase[prevNode.name]])
                    else:
                        states.append(['LOW', 'AVG', 'HIGH'])

                permutations = []
                if (len(states) > 0):
                    permutations = itertools.product(*states)
                
                if (value.name in knowledgeBase):
                    print("P(" + value.name + ")" + '[' + knowledgeBase[value.name] + '] ', end='')

                    for p in permutations:
                        for j in range(len(p)):
                            print(' | ' + value.previousNodes[j].name + '[' + p[j] + ']', end='')

                        print(' = ', end='')
                        prob = value.transitionProb[tuple([x for x in p])]
                        if (knowledgeBase[value.name] == 'LOW'):
                            print(prob[0])
                        elif (knowledgeBase[value.name] == 'AVG'):
                            print(prob[1])
                        elif (knowledgeBase[value.name] == 'HIGH'):
                            print(prob[2])
                        else:
                            print("Should not be here. Check the code\n")
                            exit()
                else:
                    for state in POSSIBLE_STATES:
                        if (len(states) > 0):
                            permutations = itertools.product(*states)

                        print("P(" + value.name + ")" + '[' + state + '] ', end='')

                        for p in permutations:
                            for j in range(len(p)):
                                print(' | ' + value.previousNodes[j].name + '[' + p[j] + ']', end='')

                            print(' = ', end='')
                            prob = value.transitionProb[tuple([x for x in p])]

                            if (state == 'LOW'):
                                print(prob[0])
                            elif (state == 'AVG'):
                                print(prob[1])
                            elif (state == 'HIGH'):
                                print(prob[2])
                            else:
                                print("Should not be here. Check the code\n")
                                exit()
                        print()
        input()
    '''
    while(len(nodesLeft) != 0):
        currNode = bayesianTree[nodesLeft[0]]
        del nodesLeft[0]

        if (len(currNode.previousNodes) == 0):
            currNodeState = inputs[currNode.name]
            jointProb *= currNode.stateProb[currNodeState]
            continue

        prevState = []
        for node in currNode.previousNodes:
            prevState.append(inputs[node.name])
            if (node.name not in addedNodes):
                nodesLeft.append(node.name)
                addedNodes.append(node.name)

        prevState = tuple(prevState)
        statesProbs = currNode.transitionProb[prevState]

        #hardcoded lol
        currProb = -1.0
        if (inputs[currNode.name] == 'LOW'):
            jointProb *= statesProbs[0]
            currProb = statesProbs[0]
        elif (inputs[currNode.name] == 'AVG'):
            jointProb *= statesProbs[1]
            currProb = statesProbs[1]
        elif (inputs[currNode.name] == 'HIGH'):
            jointProb *= statesProbs[2]
            currProb = statesProbs[2]
        else:
            print("Shouldn't be here. Check the code.\n'")
            exit()

        print("P(" + currNode.name + ")" + '[' + inputs[node.name] + ']', end='')
        for node in currNode.previousNodes:
            print(' | ' + node.name + '[' + inputs[node.name] + ']', end='')
        print(' = %f\n' % (currProb))

    print("\nFinal probability: ", end=' ')
    print(jointProb*100)
    '''    

#endmain

if (__name__ == '__main__'):
    main()
