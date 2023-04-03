from solution_probleme import *


data_path = "/Users/maloevain/Desktop/ENSAE1/S2/Programmation/programmationENSAE/input/"

#On commence par formater les données
#attention le deuxieme formatage a pris environ 3min
"""
comparer_puissance_prix(data_path +"trucks.1.in",data_path+"trucks_formated.1.in")
comparer_puissance_prix(data_path +"trucks.2.in",data_path+"trucks_formated.2.in")
"""

solution= ResolutionProbleme("trucks_formated.1.in","routes.4.out","routes.4.in")

print(solution.algorithme_genetique())
