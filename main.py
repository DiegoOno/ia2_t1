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
    node2Probabilities = {
        'LOW': [0.3864255, 0.3794243, 0.2341501],
        'AVG': [0.06039638, 0.92264651, 0.01695712],
        'HIGH': [0.01577014, 0.95873839, 0.02549147]}
    node2.setProbabilities(node2Probabilities)
    BayesianTree.append(node2)

    node3 = Node('PIP3')
    node3Probabilities = {
        'LOW': [0.2184310, 0.4473238, 0.3342453],
        'AVG': [0.07796694, 0.21120158, 0.71083148],
        'HIGH': [0.4237055, 0.4396535, 0.1366411]}
    node3.setProbabilities(node3Probabilities)
    BayesianTree.append(node3)

    node4 = Node('Raf')
    node4Probabilities = {
        'LOW-LOW': [0.06232176, 0.14724878, 0.79042946],
        'AVG-LOW': [0.4475056, 0.3125747, 0.2399197],
        'HIGH-LOW': [0.84288483, 0.12714563, 0.02996955],
        'LOW-AVG': [0.3694012, 0.3312117, 0.2993871],
        'AVG-AVG': [0.55082326, 0.39291391, 0.05626283],
        'HIGH-AVG': [0.74895046, 0.15952981, 0.09151973],
        'LOW-HIGH': [0.86757991, 0.12785388, 0.00456621],
        'AVG-HIGH': [8.842572e-01, 1.156677e-01, 7.510891e-05],
        'HIGH-HIGH': [0.841807910, 0.155367232, 0.002824859]
    }
    node4.setProbabilities(node4Probabilities)
    BayesianTree.append(node4)

    node5 = Node('Jnk')
    node5Probabilities = {
        'LOW-LOW': [0.2899262, 0.2457641, 0.4643097],
        'AVR-LOW': [5.766701e-01, 4.232872e-01, 4.271314e-05],
        'HIGH-LOW': [9.961240e-01, 3.806755e-03, 6.921373e-05],
        'LOW-AVG': [0.5794436587, 0.4203206035, 0.0002357379],
        'AVG-AVG': [6.129037e-01, 3.870808e-01, 1.543138e-05],
        'HIGH-AVG': [0.8623005877, 0.1368597817, 0.0008396306],
        'LOW-HIGH': [0.00456621, 0.99086758, 0.00456621],
        'AVG-HIGH': [0.04468980, 0.93495569, 0.02035451],
        'HIGH-HIGH': [0.155367232, 0.841807910, 0.002824859]
    }
    node5.setProbabilities(node5Probabilities)
    BayesianTree.append(node5)

    node6 = Node('P38')
    node6Probabilities = {
        'LOW-LOW': [0.30691159, 0.06458648, 0.62850193],
        'AVG-LOW': [0.919186742, 0.078464036, 0.002349223],
        'HIGH-LOW': [0.80737818, 0.09163898, 0.10098283],
        'LOW-AVG': [0.6558227251, 0.3439415370, 0.0002357379],
        'AVG-AVG': [8.149777e-01, 1.850069e-01, 1.543138e-05],
        'HIGH-AVG': [0.3862301, 0.1595298, 0.4542401],
        'LOW-HIGH': [0.86757991, 0.12785388, 0.00456621],
        'AVG-HIGH': [0.80313955, 0.19272946, 0.00413099],
        'HIGH-HIGH': [0.765536723, 0.231638418, 0.002824859]
    }
    node6.setProbabilities(node6Probabilities)
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

    #print(node3.probabilities)
    #print(node3.probabilities['LOW'][0])
    print(node4.probabilities['AVG-HIGH'][0])  

if (__name__ == '__main__'):
    main()
