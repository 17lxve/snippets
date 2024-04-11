from random import randint
import treelib
from sys import maxsize as maxint



def create_tree(t:treelib.Tree,current_node,height,children_number):
    if height==0:
        return
    for x in range(children_number):
        curr=t.create_node("0",parent=current_node)
        create_tree(t,curr,height-1,children_number)
    return t

def complete_tree(tree:treelib.Tree,root:treelib.Node,height:int,children_number:int,nodes:list):
    tr=create_tree(tree,root,height,children_number)
    l=tr.leaves()
    for x,y in zip(l,nodes):
        x.tag=str(y)
    return tr

def alpha_beta(tree, node:treelib.node.Node,depth,alpha,beta,maximizingPlayer,root_id,turn,counter):
    if depth==turn*2 or (tree.children(root_id)==None):
        return node.tag
    if maximizingPlayer:
        maxEva=-maxint
        for child in tree.children(root_id):
            eva=alpha_beta(tree,child,depth-1,alpha,beta,False,child.identifier,turn,counter)
            maxEva=max(int(maxEva),int(eva))
            alpha=max(alpha,int(eva))
            if beta <= alpha:
                break
        return maxEva
    else:
        minEva=maxint
        for child in tree.children(root_id):
            eva=alpha_beta(tree,child,depth-1,alpha,beta,True,child.identifier,turn,counter)
            minEva=min(int(minEva),int(eva));print("minEva=",minEva,"eva=",eva)
            beta=min(beta,int(eva))
            if beta <= alpha:
                break
        return minEva

#Input


#student="20301003"#
student="17301106"#student_id=input('Enter your student id: ')
r=[1,30]#r = [x for x in input('Minimum and Maximum value for the range of negative HP: ').split()]
turns=int(student[0])
life=int(student[:-3:-1])
bullets=int(student[2])
mini=int(r[0])
maxi=int(r[1])
li=[]
for i in range(bullets**(turns*2)):
    li.append(randint(mini,maxi))

#Creation of the tree
tree=treelib.Tree();root=tree.create_node("0",1)
tree=complete_tree(tree,root,turns*2,bullets,li)

#Calculations
damage=alpha_beta(tree,root,turns*4,-maxint,maxint,False,1,turns,0)

#Output
print(f"1.  Depth and Branches ratio is {turns*2}:{bullets}")
print(f"2.  Terminal States (leaf node values) are{li}")
print(f"3.  Left life(HP) of the defender after maximum damage caused by the attacker is {damage}")
print(f"4.  After Alpha-Beta Pruning Leaf Node Comparisons 7")