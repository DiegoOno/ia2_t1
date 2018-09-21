from node import Node

FILE = "data/sachs.bif"

def main():
    #Something like:
    BayesianTree = [] #This should be a class too ?

    node = Node('PKC')
    node.createState('LOW', 0.42313152)
    node.createState('AVG', 0.48163920)
    node.createState('HIGH', 0.09522928)

    BayesianTree.append(node)

    print(node.getStateProb('LOW'))

if (__name__ == '__main__'):
    main()
