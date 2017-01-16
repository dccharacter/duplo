from itertools import combinations
from random import shuffle

class Pair:
    def __init__(self, element1, element2):
        self.el1 = element1
        self.el2 = element2

    def __repr__(self):
        return "Pair({}, {})".format(self.el1, self.el2)

    def __eq__(self, pair2):
        if self.el1 == pair2[0] and self.el2 == pair2[1]:
            return True
        if self.el1 == pair2[1] and self.el2 == pair2[0]:
            return True
        return False

    def __ne__(self, pair2):
        return not self.__eq__(pair2)

    def __getitem__(self, key):
        if key == self.el2:
            return self.el1
        if key == self.el1:
            return self.el2
        raise ValueError("This pair doesn't have that value")

nJoints = 4 #must be EVEN
runs = 1
loopDetector = 10
idxs = 'abcdefghijklm'





while True:
    pos = idxs[0]+'1'
    tj = {}
    
    nodes = [] #all nodes

    ##create joints transition table
    for jt in range(nJoints):
        tj[idxs[jt]+'1'] = idxs[jt]+'3'
        tj[idxs[jt]+'2'] = idxs[jt]+'3'
        tj[idxs[jt]+'3'] = idxs[jt]+'1'
        nodes.extend((idxs[jt]+'1', idxs[jt]+'2', idxs[jt]+'3'))

    shuffle(nodes)

    nodeCount = {}
    for n in nodes:
        nodeCount[n] = 0

    ## create rail transition table (connect tracks)
    rj = {}
    while nodes:
        rj[nodes.pop()] = nodes.pop()

    ##test case
    ##rj = {}; rj['a1'] = 'a3'; rj['a2'] = 'b2'; rj['b1'] = 'b3'

    #add reverse:
    for key in rj.keys():
        rj[rj[key]] = key

    #print "pos\trail trans\tjoint trans\ta3\tb3"
    #print "-------------------------------------------------------\n"
    #print "Testing config: ", rj, "\n"


            

    railTr = None
    jointTr = pos
    seen = set()
    run = 1


    while True:
        pos = jointTr
        nodeCount[pos] += 1
        railTr = rj[pos]
        nodeCount[railTr] += 1
        jointTr = tj[railTr]
        if railTr[1] in ['1','2']: ##turn switch
            if tj[railTr[0]+'3'] is not railTr:
                tj[railTr[0]+'3'] = railTr
                ##print 'Switch! ', railTr
            else:
                ##loopDetector -= 1
                ##if not loopDetector:
                pass
        if max(nodeCount.values()) > 50 and min(nodeCount.values()) < 3:
            #print '\nNodes: ', nodeCount, "\n"
            #print "Loop detected, abort"
            break
                
        sol = "{}\t{}\t{}\t{}\t{}".format(pos, railTr, jointTr, tj['a3'], tj['b3'])
        #if sol in seen:
        if max(nodeCount.values()) > 70:
            print 'Nodes: ', nodeCount
            if run < runs:
                print "Iteration complete!"
                run += 1
                seen = set()
            else:
                print "-------------------------------------------------------\n"
                print "Simulation complete!"
                print '\nNodes: ', nodeCount, "\n"
                print "Solution: ", rj
                halt
        else:
            #print sol
            seen.add(sol)
                

        
