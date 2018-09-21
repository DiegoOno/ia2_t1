from node import Node

FILE = "data/sachs.bif"

def main():
    #Something like:
    BayesianTree = [] #This should be a class too ?

    node0 = Node('PKC')
    node0.createState('LOW', 0.42313152)
    node0.createState('AVG', 0.48163920)
    node0.createState('HIGH', 0.09522928)

    BayesianTree.append(node0)

    node1 = Node('Plcg')
    node1.createState('LOW', 0.81213356)
    node1.createState('AVG', 0.08337962)
    node1.createState('HIGH', 0.10448682)
    
    BayesianTree.append(node1)
    
    node2 = Node('PKA')
    node2Probabilities = {'LOW': [0.3864255, 0.3794243, 0.2341501], 'AVG': [0.06039638, 0.92264651, 0.01695712], 'HIGH': [0.01577014, 0.95873839, 0.02549147]}
    node2.setProbabilities(node2Probabilities)
    BayesianTree.append(node2)

    node3 = Node('PIP3')
    node3Probabilities = {'LOW': [0.2184310, 0.4473238, 0.3342453], 'AVG': [0.07796694, 0.21120158, 0.71083148], 'HIGH': [0.4237055, 0.4396535, 0.1366411]}
    node3.setProbabilities(node3Probabilities)
    BayesianTree.append(node3)

    node4 = Node('Raf')
    BayesianTree.append(node4)

    node5 = Node('Jnk')
    BayesianTree.append(node5)

    node6 = Node('P38')
    BayesianTree.append(node6)

    node7 = Node('PIP2')
    BayesianTree.append(node7)

    node8 = Node('Mek')
    BayesianTree.append(node8)
    
    node9 = Node('Erk')
    BayesianTree.append(node9)
    
    node10 = Node('Akt')
    BayesianTree.append(node10)
    #print(node.getStateProb('LOW'))

    print(node3.probabilities)

if (__name__ == '__main__'):
    main()
