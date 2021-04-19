##########ANUP RAJ NIROULA#######################

from anytree import Node, RenderTree, AsciiStyle,search
from anytree.exporter import DotExporter
from graphviz import Source
import copy
from recviz import recviz
import os
import pprint
goal_state=[[1,2,3],[8,0,4],[7,6,5]]

initial_state=[[2,8,3],[1,6,4],[7,0,5]]

DEPTH=5       ######DEPTH OF THE TREE#####################


def swapLeft(state):
    for i,s in enumerate(state):
        try:
            row,col=i,s.index(0)
        except:
            continue
    temp=copy.deepcopy(state)
    if(col==0):
        return []
    temp[row][col],temp[row][col-1]=temp[row][col-1],temp[row][col]
    col=col-1
    return temp

    #printState(state)

def swapRight(state):
    for i,s in enumerate(state):
        try:
            row,col=i,s.index(0)
        except:
            continue
    temp=copy.deepcopy(state)
    if(col==2):
        return []
    temp[row][col],temp[row][col+1]=temp[row][col+1],temp[row][col]
    col=col+1
    return temp

    #printState(state)

def swapUp(state):
    for i,s in enumerate(state):
        try:
            row,col=i,s.index(0)
        except:
            continue
    temp=copy.deepcopy(state)
    if(row==0):
        return[]
    temp[row][col],temp[row-1][col]=temp[row-1][col],temp[row][col]
    row=row-1
    return temp

    #printState(state)

def swapDown(state):
    for i,s in enumerate(state):
        try:
            row,col=i,s.index(0)
        except:
            continue
    temp=copy.deepcopy(state)
    if(row==2):
        return[]
    temp[row][col],temp[row+1][col]=temp[row+1][col],temp[row][col]
    row=row+1
    return temp
    #printState(state)

def depthFirstGeneration(node,root,counter):
    if node.name==[] or node.name==goal_state or (counter!=DEPTH and node.name==initial_state):
        return
    if counter==0:
        return
    node1=Node((swapLeft(node.name)),parent=root)
    node2=Node((swapRight(node.name)),parent=root)
    node3=Node((swapUp(node.name)),parent=root)
    node4=Node((swapDown(node.name)),parent=root)
    depthFirstGeneration(node1, node1, counter-1)
    depthFirstGeneration(node2, node2, counter-1)
    depthFirstGeneration(node3, node3, counter-1)
    depthFirstGeneration(node4, node4, counter-1)


def main():
    root=copy.deepcopy(initial_state)
    root=Node(root)
    depthFirstGeneration(root, root, DEPTH)
    for pre, fill, node in RenderTree(root):
        print(f"{pre}{node.name}")
        break
    DotExporter(root).to_dotfile("tree.dot")

    dot_file=open('tree.dot','r')
    file=dot_file.read()
    dot_file.close()
    s=Source(file,format='png')
    s.view()
    dot_file.close()
    goal_paths=(search.findall(root, lambda node: node.name == (goal_state)))
    pprint.pprint((goal_paths))

    

if __name__=='__main__':
    main()



















# def swapUp(state):
#     for i,s in enumerate(state):
#         try:
#             row,col=i,s.index(0)
#         except:
#             continue
#     try:
#         state[row][col],state[row-1][col]=state[row-1][col],state[row][col]
#     except:
#         return[]
#     printState(state)