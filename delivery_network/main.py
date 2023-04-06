from graph import *
from time import *
import sys

sys.setrecursionlimit(10**6)





data_path = "/Users/maloevain/Desktop/ENSAE1/S2/Programmation/programmationENSAE/input/"
file_name1 = "network.00.in"
file_name2 = "network.1.in"


list_filenames_routes=["routes.{}.in".format(i) for i in range(1,11)]
list_filenames_network=["network.{}.in".format(i) for i in range(1,11)]

"""
g=graph_from_file(data_path+file_name2)
g_kruskal=kruskal(g)
kruskal_dict=dfs(g_kruskal,1)
g_kruskal.draw_graph()
print(g.min_power_kruskal(kruskal_dict,6,11))"""

""" ************************** Seance 2 ****************************************"""

""" *********************************** Question 10 *******************************************"""


"on va tester pour un certain nombre de trajets le temps que ca prend pour calculer la puissance minimale"

""" Je mets le programme en dessous en commentaire car il prend du temps à tourner


for i in range(0,5):
    g3=graph_from_file(data_path+list_filenames_network[i])
    with open(data_path+list_filenames_routes[i], "r") as file:
        lines = file.readlines()
        #on transforme le fichier texte (qui est un tableau) en une liste de liste
        list_of_lists = [line.split() for line in lines]
        " on convertit la liste de string en une liste de int"
        tableau =[list(map(int, i)) for i in list_of_lists]

    trajet1=tableau[57]
    #trajet2=tableau[2]

    src1=trajet1[0]
    dest1=trajet1[1]

    #src2=trajet2[0]
    #dest2=trajet2[1]

    t1_start = perf_counter()

    print(g3.min_power(src1,dest1))
    #print(g3.min_power(src2,dest2))


    t1_stop=perf_counter()
    print("il a fallu ", t1_stop-t1_start ," secondes pour trouver un trajet minimale  pour la route ",i+1)
    print("sachant qu'il y a ", tableau[0][0]," trajets, il faudrait ", tableau[0][0]*(t1_stop-t1_start)/(60*60*24)," jours pour tous les trajets")
"""
""" network1 environ 1.331409722221677e-07  jours pour tous les trajets
    network2 environ 723 jours pour tous les trajets (620secondes pour un trajet)
    network3 environ 231 jours pour tous les trajets (50 secondes pour un trajet)
    network4 environ 228 jours pour tous les trajets (48 secondes pour un trajet)
    network5 environ 580 jours pour tous les trajets (501 secondes pour un trajet)


    je n'ai pas fait tourner l'algo pour les autres trajets car ca va prendre le même ordre de grandeur niveau temps
"""



""" *********************************** Question 15 *******************************************"""


"""
for i in range(0,9):
    g=graph_from_file(data_path+list_filenames_network[i])
    with open(data_path+list_filenames_routes[i], "r") as file:
        lines = file.readlines()
        #on transforme le fichier texte (qui est un tableau) en une liste de liste
        list_of_lists = [line.split() for line in lines]
        " on convertit la liste de string en une liste de int"
        tableau =[list(map(int, i)) for i in list_of_lists]

    trajet1=tableau[57]
    #trajet2=tableau[2]

    src1=trajet1[0]
    dest1=trajet1[1]

    #on crée le sous arbre couvrant relatif au graphe
    g_kruskal=kruskal(g)


    t1_start = perf_counter()
    g.min_power_kruskal_1(g_kruskal,src1,dest1)
    #print(g3.min_power(src2,dest2))
    t1_stop=perf_counter()

    print("il a fallu ", t1_stop-t1_start ," secondes pour trouver un trajet minimale  pour la route ",i+1)
    print("sachant qu'il y a ", tableau[0][0]," trajets, il faudrait ", tableau[0][0]*(t1_stop-t1_start)/(60*60)," heures pour tous les trajets")

"""
"""il a fallu  4.415999999896059e-06  secondes pour trouver un trajet minimale  pour la route  1
sachant qu'il y a  140  trajets, il faudrait  1.7173333332929116e-07  heures pour tous les trajets


il a fallu  0.06750245800000032  secondes pour trouver un trajet minimale  pour la route  2
sachant qu'il y a  100000  trajets, il faudrait  1.8750682777777867  heures pour tous les trajets


il a fallu  0.07851487500000065  secondes pour trouver un trajet minimale  pour la route  3
sachant qu'il y a  500000  trajets, il faudrait  10.90484375000009  heures pour tous les trajets


il a fallu  0.10050150000000002  secondes pour trouver un trajet minimale  pour la route  4
sachant qu'il y a  500000  trajets, il faudrait  13.958541666666669  heures pour tous les trajets


il a fallu  0.18222079099999888  secondes pour trouver un trajet minimale  pour la route  5
sachant qu'il y a  100000  trajets, il faudrait  5.0616886388888584  heures pour tous les trajets


il a fallu  0.25425075000000064  secondes pour trouver un trajet minimale  pour la route  6
sachant qu'il y a  500000  trajets, il faudrait  35.31260416666676  heures pour tous les trajets


il a fallu  0.2467205419999985  secondes pour trouver un trajet minimale  pour la route  7
sachant qu'il y a  500000  trajets, il faudrait  34.266741944444234  heures pour tous les trajets


il a fallu  0.29718862500000043  secondes pour trouver un trajet minimale  pour la route  8
sachant qu'il y a  500000  trajets, il faudrait  41.276197916666725  heures pour tous les trajets


il a fallu  0.22283108399999918  secondes pour trouver un trajet minimale  pour la route  9
sachant qu'il y a  500000  trajets, il faudrait  30.948761666666552  heures pour tous les trajets
"""


""" En dessous on va écrire dans un fichier routes.i.out la puissance minimale pour chaque trajet"""


""" on ne fait que pour les 1000 premiers trajets car sinon ca peut durer des heures"""






"""

En dessous, on utilise la version optimisee de min_power avec kruskal (deuxieme version de min_power_kruskal),
On arrive à calculer l'ensemble des puissances minimales pour tous les fichiers routes en moins de 15min

"""
"""
for j in range(9):
    g=graph_from_file(data_path+list_filenames_network[j])
    with open(data_path+list_filenames_routes[j], "r") as file:
        lines = file.readlines()
        #on transforme le fichier texte (qui est un tableau) en une liste de liste
        list_of_lists = [line.split() for line in lines]
        " on convertit la liste de string en une liste de int"
        tableau =[list(map(int, i)) for i in list_of_lists]

    List_puissances =[str(i) for i in tableau[0]]
    t1_start = perf_counter()

    g_kruskal=kruskal(g)
    kruskal_dict=dfs(g_kruskal,1)

    for i in range(1,len(tableau)):

        src=tableau[i][0]
        dest=tableau[i][1]
        pow,chemin=g.min_power_kruskal_2(kruskal_dict,src,dest)
        List_puissances.append(pow)
    t1_stop = perf_counter()


    #with open(data_path + "routes.{}.out".format(j+1),"w") as file:
    #    for i in range(0,len(List_puissances)):
    #        file.write(str(List_puissances[i])+" \n ")


    print("il a fallu ", t1_stop-t1_start ," secondes pour trouver toutes les puissances minimales pour la route ",i+1)
"""

""" Toutes les puissances minimales pour tous les trajets de tous les fichiers routes ont été calculés
en moins de 5min"""






#
