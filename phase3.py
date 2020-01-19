import networkx as nx
import pandas as pd

from phase2 import suspects

persons = pd.read_csv("./artifice Data/people.csv" )
transactions = pd.read_csv("./artifice Data/transactions.csv" )
accounts = pd.read_csv("./artifice Data/accounts.csv" )

bank_graph = nx.MultiDiGraph()
sources = []
for i in range(len(persons)):
    bank_graph.add_node(persons.iloc[i][2] , first_name = persons.iloc[i][0] ,
                          name = persons.iloc[i][1] , birth_day = persons.iloc[i][3] ,
                          city = persons.iloc[i][4] , work = persons.iloc[i][5])
    if (persons.iloc[i][5] == "قاچاقچی"):
        sources.append(persons.iloc[i][2])
    
#print(sources)
#print(bank_graph.node[90792622874])
for i in range(len(accounts)):
    bank_graph.add_node(accounts.iloc[i][3] , owner = accounts.iloc[i][0] ,
                        bank_name = accounts.iloc[i][1] ,sheba = accounts.iloc[i][2])
    bank_graph.add_edge(accounts.iloc[i][0] , accounts.iloc[i][3],  is_account_edge = True , fuckin_attrib = 123)
    bank_graph.add_edge(accounts.iloc[i][3] , accounts.iloc[i][0],  is_account_edge = True , fuckin_attrib = 123)
    


#print(bank_graph[76465777888][137312][0])
    
for i in range(len(transactions)):
    bank_graph.add_edge(transactions.iloc[i][0],transactions.iloc[i][1],
                        transaction_id = transactions.iloc[i][2] ,
                        date = transactions.iloc[i][3] , amount = transactions.iloc[i][4]
                        ,is_account_edge = False)

#print (bank_graph.edges)
suspects_list = list(suspects)
delety = set([])
#print(nx.has_path(bank_graph ,96102478622,15242752173))
#print (suspects)
print(len(suspects))
#print(nx.shortest_path(bank_graph,76465777888,9655617003))

for j in range(len(sources)):
    for i in range(len(suspects_list)):    
        if (nx.has_path(bank_graph , sources[j] , suspects_list[i])):
            delety.add(suspects_list[i])
'''
for j in range (len(sources)):
    for i in range(len(suspects_list)):
        print(nx.has_path(bank_graph , sources[j] , suspects_list[i]))
'''
'''
for i in delety :
    suspects.remove(i)
'''
print("len delety is : ")
print(delety)
print(len(delety))
    
