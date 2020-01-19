#TODO: this file should be renamed to phase 2 ...
import datetime
import networkx as nx
import pandas as pd

persons = pd.read_csv("./artifice Data/people.csv" )
assets = pd.read_csv("./artifice Data/ownerships.csv" )
homes = pd.read_csv("./artifice Data/homes.csv" )
cars = pd.read_csv("./artifice Data/cars.csv" )
rels = pd.read_csv("./artifice Data/relationships.csv" )


family_graph = nx.DiGraph()
asset_graph = nx.DiGraph()

#loading persons
for i in range(len(persons)):
    family_graph.add_node(persons.iloc[i][2] , first_name = persons.iloc[i][0] ,
                          name = persons.iloc[i][1] , birth_day = persons.iloc[i][3] ,
                          city = persons.iloc[i][4] , work = persons.iloc[i][5])
    asset_graph.add_node(persons.iloc[i][2] , first_name = persons.iloc[i][0] ,
                          name = persons.iloc[i][1] , birth_day = persons.iloc[i][3] ,
                          city = persons.iloc[i][4] , work = persons.iloc[i][5])
    
for i in range(len(homes)):
    asset_graph.add_node(homes.iloc[i][2] , owner = homes.iloc[i][0],
                         price = homes.iloc[i][1] , size = homes.iloc[i][3],
                         address = homes.iloc[i][4])

for i in range(len(cars)):
    asset_graph.add_node(cars.iloc[i][0] , owner = cars.iloc[i][1] , model = cars.iloc[i][2] ,
                         color = cars.iloc[i][3])
#a function to determine the 2 year deadline    
test=dict(asset_graph.nodes.data())
print (test)    
l=[]
for i in range(len(assets)):
    l.append(int(str(assets.iloc[i][3][0:10]).translate({ord('-'): None})))    
a=(datetime.datetime.now())
a=str(a)
a=a[0:10]
a=int(a.translate({ord('-'): None}))
for i in range(len(l)):
    if a-l[i]<20000:
        l[i]=True
    else:l[i]=False
assets["Suspect"]=l    
#end of that bloody function for deadline
for i in range(len(assets)):#TODO : manipulate the bloody date of ownerships
    asset_graph.add_edge(assets.iloc[i][0] , assets.iloc[i][1] , ownership_id = assets.iloc[i][2],
                         date = assets.iloc[i][3] , amount = assets.iloc[i][4] , Suspect = assets.iloc[i][5])

test1 =dict(asset_graph.nodes.data())
print (test)   
    
for i in range(len(rels)):
    family_graph.add_edge(rels.iloc[i][0] , rels.iloc[i][1] , relation = rels.iloc[i][2] ,
                          date = rels.iloc[i][3])

#listofguys = nx.neighbors(family_graph , 47708709952)
#print(list(family_graph.nodes))
#print(family_graph[70232533224][36191272611]['relation'])    #consider testing
#print(family_graph[84320556439][87474057898]['relation'] != "SIBLING")  # test for the filter algorithm

suspects = set([])

test2 =dict(asset_graph.nodes.data())
print (test)   
    

for i in family_graph:
    # functionality for chekcing the families ...
    neighbours_list = list(filter(lambda x : family_graph[i][x]['relation'] != "SIBLING" # consider checking for the company of that bloody person
                             ,list(family_graph.neighbors(i))))
    for j in neighbours_list:
        props = list(asset_graph.neighbors(j))#lists the assets of person 'j'
        for k in props:
            if(asset_graph[j][k]['Suspect']==True):#check if in this assets there is sth bought in 2 years
                suspects.add(i)
                suspects.add(j)
                break #consider testing the break on fuckin python ...
            
#print (suspects)
                
            
    