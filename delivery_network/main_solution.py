from solution_probleme import *


data_path = "/Users/maloevain/Desktop/ENSAE1/S2/Programmation/programmationENSAE/input/"

#On commence par formater les données
#attention le deuxieme formatage a pris environ 3min
"""
comparer_puissance_prix(data_path +"trucks.1.in",data_path+"trucks_formated.1.in")
comparer_puissance_prix(data_path +"trucks.2.in",data_path+"trucks_formated.2.in")
"""

list_filenames_routes_in=["routes.{}.in".format(i) for i in range(1,10)]
list_filenames_routes_out=["routes.{}.out".format(i) for i in range(1,10)]


"""
for i in range(0,9):
    solution= ResolutionProbleme("trucks_formated.2.in",list_filenames_routes_out[i],list_filenames_routes_in[i])

    print("pour la route ",i+1)
    print("l'utilite trouvee via l'algortihme pseudo_naif est ",solution.solution_pseudo_naive()[1]," et le poids est ",solution.solution_pseudo_naive()[2])

    print("l'utilite trouvee via l'algortihme aleatoire est ",solution.solution_aleatoire()[1]," et le poids est ",solution.solution_aleatoire()[2])
#attention brute force met beaucoup trop de temps à compiler
#print(solution.brute_force())


    print("l'utilite trouvee via l'algortihme genetique est ",solution.algorithme_genetique()[1])
"""
