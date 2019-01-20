import random
import math

from copy import deepcopy

from Tree import Node

class NPuzzle(object):
    def __init__(self,board=None):
        if board!=None:
            self.board=board
        else:
            self.Randomize()

    def Randomize(self):
        r=[1,2,3,4,5,6,7,8]
        random.shuffle(r)
        r=[ [ r[0], r[1], r[2] ],
            [ r[3], r[4], r[5] ],
            [ r[6], r[7], None ] ]
        self.board=r
        
    def Display(self,board):
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] != None:
                    print(board[i][j],end=' ')
                else:
                    print(" ",end=' ')
            print("")

    def SolveBFS(self): # solve 8-puzzle with breadth-first-search
        # return a list of moves that lead to solution.
        root = Node(element=self.board)
        self.tree=root
        
        stack = [root]
        visited=[]
        
        print("\nSolving " + str(len(self.board)**2-1) + "-puzzle with breadth-first-search.\n" )
        
        # generate the solution board
        solution=[ [ (i+1+j*3) for i in range(len(self.board)) ]
                             for j in range(len(self.board)) ]
        solution[-1][-1]=None
        max_depth=25

        while stack != []:
        
            for node in stack:
                visited.append(node)
                board = node.element
                for i in range(len(board)):
                    for j in range(len(board[i])):
                        valid_moves=self.GetValidMoves(board,i,j)
                        if valid_moves != []:
                            for k in valid_moves:
                                try:
                                    if node.parent.element != deepcopy(k):
                                        c=Node(element=deepcopy(k))
                                        node.setChild(c)
                                        if c.depth==max_depth:
                                            print("Max depth reached.")
                                            return []
                                        # print(c.element)
                                        stack.append(c)

                                        # solutions to 8-puzzle, 15-puzzle, etc
                                        if k==solution:
                                            steps=[c.element]
                                            k_parent=c.parent
                                            while k_parent != None:
                                                steps.append(k_parent.element)
                                                k_parent=k_parent.parent
                                            
                                            return list(reversed(steps))
                                    else:
                                        pass
                                except AttributeError:
                                    c=Node(element=deepcopy(k))
                                    node.setChild(c)
                                    if c.depth==max_depth:
                                        print("Max depth reached.")
                                        return []
                                    # print(c.element)
                                    stack.append(c)
                                              

            for node in visited:
                if node in stack:
                    stack.remove(node)

            print(stack)

    def GetValidMoves(self,board,m,n):
        valid_moves=[]
        
        indices=[[m-1,n],
                 [m+1,n],
                 [m,n-1],
                 [m,n+1]]

        for index in indices:
            try:
                if board[index[0]][index[1]] == None and (index[0] >= 0 and index[1] >= 0):
                    new_board=deepcopy(board)
                    new_board[index[0]][index[1]]=new_board[m][n]
                    new_board[m][n]=None
                    valid_moves.append(deepcopy(new_board))
            except IndexError:
                pass

        return valid_moves

'''
n=NPuzzle([ [4, 13, 12, 10],
            [15, 9, 8, 11],
            [14, 5, 1, 6],
            [3, 2, 7, None] ])
'''

n=NPuzzle([[7,5,3],[1,6,2],[4,8,None]])
print("Board:")
n.Display(n.board)
steps=n.SolveBFS()
for i in range(len(steps)):
    print("Step "+str(i)+":")
    n.Display(steps[i])
    print("")
