import itertools
#print "Success"
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

nJoints = 6 #must be EVEN
runs = 1
loopDetector = 10
idxs = 'abcdefghijklm'


def getTrack(nodes, seen):
    for perm in itertools.permutations(nodes):
        p = tuple(sorted(
            [tuple(sorted(perm[i:i + 2])) for i in range(0, len(perm), 2)]))
        #if p not in seen:
        #    seen.add(p)
        yield p

def getTrack2(l, seen):
    # recursion anchor, basic case:
    # when we have 2 nodes only one pair is possible
    if len(l) == 2:
        yield [tuple(l)]
    else:
        # Pair the first node with all the others
        for i in range(1, len(l)):
            # Current pair
            pair1 = [(l[0], l[i])]
            # Combine it with all pairs among the remaining nodes
            remaining = l[1:i] + l[i+1:]
            for otherPairs in getTrack2(remaining, 1):
                yield pair1 + otherPairs

def getTransition(track, pos):
    for pair in track:
        if pos in pair:
            if pos != pair[0]:
                return pair[0]
            else:
                return pair[1]

    
seenTracks = set()
itrack = 0

tj = {}
    
nodes = [] #all nodes

##create joints transition table
for jt in range(nJoints):
    tj[idxs[jt]+'1'] = idxs[jt]+'3'
    tj[idxs[jt]+'2'] = idxs[jt]+'3'
    tj[idxs[jt]+'3'] = idxs[jt]+'1'
    nodes.extend((idxs[jt]+'1', idxs[jt]+'2', idxs[jt]+'3'))

nIter = 0
for track in getTrack2(nodes, seenTracks):
    pos = idxs[0]+'1'

    print 'Iter: ', nIter, " ",
    nIter += 1

    nodeCount = {}
    for n in nodes:
        nodeCount[n] = 0

    ## create rail transition table (connect tracks)
    #####rj = {}
    #####while nodes:
    #####    rj[nodes.pop()] = nodes.pop()

    
    ##print track
    
    ##test case
    ##rj = {}; rj['a1'] = 'a3'; rj['a2'] = 'b2'; rj['b1'] = 'b3'

    #add reverse:
    ######for key in rj.keys():
    ######    rj[rj[key]] = key

    #print "pos\trail trans\tjoint trans\ta3\tb3"
    #print "-------------------------------------------------------\n"
    #print "Testing config: ", track, "\n"


            

    railTr = None
    jointTr = pos
    ##seen = set()
    run = 1

    #itrack += 1
    #if not itrack%20:
    #    print 'Iteration: ', itrack


    while True:
        pos = jointTr
        nodeCount[pos] += 1
        railTr = getTransition(track, pos)
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
        if max(nodeCount.values()) > 20 and min(nodeCount.values()) < 3:
            ##print '\nNodes: ', nodeCount, "\n"
            print "Loop"
            break
                
        sol = "{}\t{}\t{}\t{}\t{}".format(pos, railTr, jointTr, tj['a3'], tj['b3'])
        #if sol in seen:
        if max(nodeCount.values()) > 30:
            print 'Nodes: ', nodeCount
            if run < runs:
                print "Iteration complete!"
                run += 1
                #seen = set()
            else:
                print "-------------------------------------------------------\n"
                print "Simulation complete!"
                print '\nNodes: ', nodeCount, "\n"
                print "Solution: ", track
                halt
                
        #else:
            #print sol
            #seen.add(sol)
                

        
