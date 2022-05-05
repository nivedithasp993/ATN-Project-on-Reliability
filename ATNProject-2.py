
import networkx as netx
from graph_tools import *
import random
import math
import numpy as np
import copy
import matplotlib.pyplot as pyt



Iterate = []
CurrentState = []
Newstate = []
baseProbability = 0.05
master_LinkProabilityvalue = []

# Generating graph with 5 nodes and 10 edges
g = Graph()
g = Graph(directed=False)
g.add_vertex(5)
for a in range(0, 5):
    for b in range(a+1, 5):
        g.add_edge(a, b)
        

def createTheGraph(linkProbabilities,reliabilities):
    
    fig = pyt.figure()
    ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])

    pyt.rcParams["figure.figsize"] = [7.00, 3.50]
    pyt.rcParams["figure.autolayout"] = True
    
    ax.set_title("Link probabilities(p) VS Network Reliability(R)")

    ax.set_xlabel("Link Probabilities")

    ax.set_ylabel("Network reliability")
    
    tick1 = [0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5, 0.55, 0.6, 0.65, 0.7, 0.75, 0.8, 0.85, 0.9, 0.95, 1]
    
    tick2 = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]
    
    ax.set_xticks(tick1)
    
    ax.set_yticks(tick2)

    ax.plot(linkProbabilities, reliabilities, color="green")

    pyt.show()
    
    
def createTheGraph1(kvalue,reliabilities):
    
    fig = pyt.figure()
    ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])

    pyt.rcParams["figure.figsize"] = [7.00, 3.50]
    pyt.rcParams["figure.autolayout"] = False

    pyt.plot(kvalue, reliabilities,color="red")
    
    pyt.title("K Value VS Overall Network Reliability(R)")

    pyt.xlabel("K Value")

    pyt.ylabel("Overall Network Reliability")
    
    tick1 = kvalue
    
    pyt.xticks(tick1)
    
    pyt.yticks(np.arange(0.8, 1.2, 0.1))

    pyt.show()



# Calculating probability of individual states

def LinkProability1(Itr):

    itr_list = list(Itr)
    Student_id = []
    Student_id = "2021474685"
    temp = []

    for j in range(0, 10):

        if itr_list[j] == '1':
            
            temp.append(pow(baseProbability, ((int(Student_id[j]) / 3.0))))
        else:
            temp.append(1-(pow(baseProbability, ((int(Student_id[j]) / 3.0)))))

    
    res = 1
    for item in temp:
        res *= item

    return res



# Generating 1024 link states

def NetworkProbility():

    for i in range(0, 1024):
        CurrentState.append(format(i, "010b"))



# Checking if link states are up/down by node traversing

def updownstatecheck():

    global baseProbability
    statelist = ['AB', 'AC', 'AD', 'AE', 'BC', 'BD', 'BE', 'CD', 'CE', 'DE']   #Assigning values to edges

    cnt = 0
    master_LinkProabilityvalue = []
    for j in range(0, 20):
        
        batch_LinkProabilityvalue = []

        for ptr in range(0, 1024):

            Adjmatrix = [[0]*5 for _ in range(5)]        #Creating the adjacency matrix to store the connected edges
            
            Iterate = CurrentState[ptr]
            
            list2 = []
            list2 = [char for char in Iterate]
            
            new_list = list(zip(statelist, list2))
            
            output_list = [item for item in new_list if item[1] == '1']
            
            for itm1 in output_list:
                r = 0
                c = 0

                for idx in range(len(itm1[0])):         

                    if itm1[0][idx] == 'A':

                        if idx == 0:
                            r = 0
                        else:
                            c = 0

                    if itm1[0][idx] == 'B':

                        if idx == 0:
                            r = 1
                        else:
                            c = 1

                    if itm1[0][idx] == 'C':

                        if idx == 0:
                            r = 2
                        else:
                            c = 2

                    if itm1[0][idx] == 'D':

                        if idx == 0:
                            r = 3
                        else:
                            c = 3

                    if itm1[0][idx] == 'E':

                        if idx == 0:
                            r = 4
                        else:
                            c = 4

                Adjmatrix[r][c] = 1
                Adjmatrix[c][r] = 1
           
            if BFS(Adjmatrix):
                
                batch_LinkProabilityvalue.append(LinkProability1(Iterate))

        master_LinkProabilityvalue.append(sum(batch_LinkProabilityvalue))

        print('The Network Reliability with probability {} is {}' .format(round(baseProbability, 3), master_LinkProabilityvalue[j]))
        
        baseProbability += 0.05
        
    base_list = np.linspace(0.05,1.0,20)
    createTheGraph(base_list,master_LinkProabilityvalue)


def BFS(Adjmatrix):

    flag = False
    visited = [False for i in range(5)]
    Visitednode = []
    countVisited = 0

    for src in range(len(Adjmatrix)):
        
        for idx in range(5):

            if (not(visited[idx]) and Adjmatrix[src][idx] == 1 and (idx not in Visitednode)):

                Visitednode.append(idx)
                countVisited += 1
                visited[idx] = True
                

    # Verification and returning the decision

    if (countVisited == 5):    #Checking if the graph is connected or not
        
        flag = True        

    return flag


def updownstatecheckagain(Newstate):
    
    global baseProbability
    statelist = ['AB', 'AC', 'AD', 'AE', 'BC', 'BD', 'BE', 'CD', 'CE', 'DE']
    cnt = 0
    batch_LinkProabilityvalue = []
    master_LinkProabilityvalue = []


    for ptr in range(0, 1024):
        Adjmatrix = [[0]*5 for _ in range(5)]
        Iterate = Newstate[ptr]
        list2 = []
        list2 = [char for char in Iterate]
        new_list = list(zip(statelist, list2))
        output_list = [item for item in new_list if item[1] == '1']
        
        for itm1 in output_list:
            r = 0
            c = 0
            for idx in range(len(itm1[0])):
                if itm1[0][idx] == 'A':
                    if idx == 0:
                        r = 0
                    else:
                        c = 0
                if itm1[0][idx] == 'B':
                    if idx == 0:
                        r = 1
                    else:
                        c = 1
                if itm1[0][idx] == 'C':
                    if idx == 0:
                        r = 2
                    else:
                        c = 2
                if itm1[0][idx] == 'D':
                    if idx == 0:
                        r = 3
                    else:
                        c = 3
                if itm1[0][idx] == 'E':
                    if idx == 0:
                        r = 4
                    else:
                        c = 4

            Adjmatrix[r][c] = 1
            Adjmatrix[c][r] = 1
        
        if BFS(Adjmatrix):
            
            itr_list = list(Iterate)
            Student_id = []
            Student_id = "2021474685"
            temp = []
            baseProb = 0.9
            #p += 1
            
            for j in range(0, 10):

                if itr_list[j] == '1':
        
                    temp.append(pow(baseProb, ((int(Student_id[j]) / 3.0))))
                else:
                    temp.append(1-(pow(baseProb, ((int(Student_id[j]) / 3.0)))))    
            
            res = 1
            for item in temp:
                res *= item

            batch_LinkProabilityvalue.append(res)
    
    return sum(batch_LinkProabilityvalue)
 
        

# Function to flip the states based on k value and calculate the reliability
   
def part2_linkreliability():
    
    k=1
    avg_value_prob_list = []
    
    for i in range(0,20):
        var=[]
        backup = []
        backup=copy.deepcopy(CurrentState)      
        master_LinkProabilityvalue = []
        for a in range(0,4): 
            Averagevalue=0   
            var=random.sample(backup,k)
                
            for j in range(0,len(var)):
                
                str1 =''
                for p in range(0,10):             # flipping the states
                    
                    if var[j][p]=='1':
                        str1+='0'
                        
                    else:
                        str1+='1'
                
                x=backup.index(var[j])
                var[j] = str1        
                backup[x]=str1   
                        
            master_LinkProabilityvalue.append(updownstatecheckagain(backup))
        
        
        Averagevalue=np.mean(master_LinkProabilityvalue)    #averaging the reliability of multiple k states
        if Averagevalue > 1.0:
            Averagevalue = 1.0
        avg_value_prob_list.append(Averagevalue)
        print("The Network reliability when k={} is {}".format(k,Averagevalue))    
        k+=1
        
    kvalue=list(range(1, 21))
    createTheGraph1(kvalue,avg_value_prob_list)
        


                               
if __name__ == "__main__":
    NetworkProbility()

    updownstatecheck()

    part2_linkreliability()

