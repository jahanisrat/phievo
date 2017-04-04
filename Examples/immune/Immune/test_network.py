#from run_evolution import *
from classes_eds2 import * 
from mutation import * 
from interaction_pMHC import * 
from phievo.Networks.deriv2 import *
from initialization_pMHC import *
import random 

seed=int(random.random()*100000) 
g=random.Random(seed) 

# initializing the network.
L=Mutable_Network(g) 
L.activator_required=0 

# the ligand (the pMHC on the antigen presenting cell)
parameters=[['Ligand']]
parameters.append(['Input',0])
Lig=L.new_Species(parameters)


# the receptor (on the T cell)
parameters=[['Receptor']]
R = L.new_Species(parameters)


# the complex generated: it is a kinase that is phosphorylable and with the label pMHC to indicate it is in the cascade.
parameters=[['Kinase']]
parameters.append(['Phosphorylable'])
parameters.append(['Phospho',0])
parameters.append(['pMHC'])
#parameters.append(['Output',0])

# the first binding of the receptor and ligand generating the complex.
[Binding, C] = L.new_KPR_Binding(Lig,R,1,parameters)
L.write_id()
unbinbing = L.new_KPR_Unbinding(Lig,R,C)

# a kinase 
parameters=[['Kinase']]
parameters.append(['Phosphorylable'])
parameters.append(['Phospho',0])
K = L.new_Species(parameters)


# a phosphatase
parameters=[['Phosphatase']]
parameters.append(['Phosphorylable'])
parameters.append(['Phospho',0])
P = L.new_Species(parameters)

# rounds of phosphorylation and dephosphorylation. note that the new_Simple_Phosphorylation
# function recognizes automatically an element in the cascade and adds the 
# interaction KPR_Unbinding to it. 
[C_p,phospho] = L.new_Simple_Phosphorylation(K,C,0.1)
dephospho = L.new_Simple_Dephosphorylation(P,C_p,C,0.2)
[C_pp,phospho] = L.new_Simple_Phosphorylation(K,C_p,0.1)
dephospho = L.new_Simple_Dephosphorylation(P,C_pp,C_p,0.2)
[C_ppp,phospho] = L.new_Simple_Phosphorylation(K,C_pp,0.1)
dephospho = L.new_Simple_Dephosphorylation(P,C_ppp,C_pp,0.2)
[C_pppp,phospho] = L.new_Simple_Phosphorylation(K,C_ppp,0.1)
dephospho = L.new_Simple_Dephosphorylation(P,C_pppp,C_ppp,0.2)
#L.write_id()
C_pppp.add_type(['Output',0])


L.write_id()


#L.random_Simple_Phosphorylation()
#L.random_Simple_Phosphorylation()
#L.random_Simple_Dephosphorylation()
#L.random_Simple_Phosphorylation()
#L.random_Simple_Dephosphorylation()
#L.random_Simple_Phosphorylation()
#L.write_id()






gr = draw_Network(L.graph)
gr.write_jpg('test_KPR_cascade_rand_Phospho.jpg')
# print open(cfile['header']).read()
#pgm = compute_program(L,prmt,0)
#print pgm
#print "/*The derivatives generated by the code for the test KPR cascade. */"
#print deriv2.SimplePhospho_deriv_inC(L)
#print deriv2.SimpleDephospho_deriv_inC(L)
#print deriv2.compute_KPR_Binding(L)
#print deriv2.compute_KPR_Unbinding(L)
#print compute_deriv_inC(L)