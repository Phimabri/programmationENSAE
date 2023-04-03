import random


# Paramètres de l'algorithme génétique
taille_population = 100  # taille de la population
taux_mutation = 0.1  # taux de mutation
nombre_iterations = 50  # nombre d'itérations



"""fonction pour le formatage des données """

""" on va supprimer les lignes dans le fichier trucks qui sont moins avantageuses (ie prix plus cher pour performance moins bonne)"""
def comparer_puissance_prix(input_file, output_file):
    # Lecture des données dans le fichier d'entrée
    with open(input_file, 'r') as f:
        data = f.readlines()[1:] # on ignore la première ligne qui ne contient qu'un nombre

    # Conversion des données en listes de puissance et de prix
    puissance = []
    prix = []
    for line in data:
        p, px = map(int, line.split())
        puissance.append(p)
        prix.append(px)

    # Parcours des données et sélection des lignes à conserver
    indices_a_supprimer = []
    for i in range(len(puissance)):
        for j in range(i+1, len(puissance)):
            if puissance[i] <= puissance[j] and prix[i] >= prix[j]:
                indices_a_supprimer.append(i)

    # Écriture des lignes à conserver dans le fichier de sortie
    with open(output_file, 'w') as f:
        for i in range(len(puissance)):
            if i not in indices_a_supprimer:
                f.write(str(puissance[i]) + " " + str(prix[i]) + "\n")








class ResolutionProbleme():

    def __init__(self,filename_camion_formated,filename_puissances,filename_routes):
        """ attention il faut mettre le chemin propre à l'utilisateur en dessous """
        data_path = "/Users/maloevain/Desktop/ENSAE1/S2/Programmation/programmationENSAE/input/"

        #il faut que le fichier camion ai été formaté avant
        with open(data_path+filename_camion_formated, "r") as file:
            lines = file.readlines()
            #on transforme le fichier texte (qui est un tableau) en une liste de liste
            list_of_lists = [line.split() for line in lines]
            " on convertit la liste de string en une liste de int"
            tableau =[list(map(int, i)) for i in list_of_lists]

        with open(data_path + filename_puissances, "r") as file:
            lines = file.readlines()
            # on transforme le fichier texte (qui est un tableau) en une liste
            list_of_lists = [line.split() for line in lines]
            # on convertit la liste de string en une liste de int
            tableau2= [int(item) for sublist in list_of_lists for item in sublist]


        with open(data_path+filename_routes, "r") as file:
            lines = file.readlines()
            #on transforme le fichier texte (qui est un tableau) en une liste de liste
            list_of_lists = [line.split() for line in lines]
            " on convertit la liste de string en une liste de int"
            tableau3 =[list(map(int, i)) for i in list_of_lists]

        #on stock sous forme de liste l'ensemble des camions, des puissances minimales et des profits pour chaque trajet
        self.liste_camions=tableau
        self.liste_puissances=tableau2[1:]
        self.liste_trajets=tableau3[1:]

        self.budget= 25*(10**9)

        #on traduit le probleme des camions en probleme du sac à dos
        self.poids=[]
        self.valeurs =[]

        cpt=0

        for trajet in self.liste_trajets:

            #on ajoute à valeur le profit d'un trajet
            self.valeurs.append(trajet[1])
            #on fait ensuite une dichotomie pour trouver le prix minimal du camion à associer à ce trajet
            puissance=self.liste_puissances[cpt]
            debut_tmp=0
            fin_tmp=len(self.liste_camions)
            while debut_tmp+1!=fin_tmp:
                milieu=int((debut_tmp+fin_tmp)/2)
                if puissance <= self.liste_camions[milieu][0]:
                    fin_tmp=milieu
                else:
                    debut_tmp=milieu
            self.poids.append(self.liste_camions[milieu][1])
            cpt+=1

    def EstTrivial(self):
        """ fonction qui renvoie un booléen pour savoir si le problème est trivial,
        c'est-à-dire si on a assez d'argent pour acheter des camions capable de couvrir tous les trajets """
        max_power =max(self.liste_puissances)
        for i in range(len(self.liste_camions)):
            #on regarde de manière décroissante (en partant du camion le plus cher au moins cher) s'il existe une solution
            #triviale au probleme
            if self.liste_camions[-(i+1)][0]>max_power and self.liste_camions[-(i+1)][1]*len(self.liste_puissances)<self.budget:
                return True
        return False


    def solution_pseudo_naive(self):
        """ on va trier tous les objets en fonction de leur rapport valeur/poids et on prendra les meilleurs
        Cela ne garantit pas une solution optimale mais ça garantit une solution assez proche """
        Liste_ratio = []
        for i in range(len(self.poids)):
            #on stock le ratio des valeurs/poids et l'indice de l'objet concerne
            Liste_ratio.append((self.valeurs[i]/self.poids[i],i))
        Liste_ratio= sorted(Liste_ratio, key=lambda x:x[0],reverse=True)
        poids_total=0
        solution=[]
        cpt=0
        while poids_total<=self.budget:
            solution.append(Liste_ratio[cpt][1])
            poids_total+=self.poids[Liste_ratio[cpt][1]]
            cpt+=1
        #il faut enlever le dernier poids car sinon on dépasse le budget
        dernier_poids=solution.pop()
        return solution, poids_total-self.poids[dernier_poids]



    """************************************* Algo genetique **********************************"""

    "Nous définissons en dessous des méthodes dans le but d'implémenter l'algorithme generique pour resoudre le probleme"

    def evaluation(self,solution):
        poids_total = 0
        valeur_totale = 0
        for i in range(len(solution)):
            if solution[i] == 1: #si on prend le camion i
                poids_total += self.poids[i]
                valeur_totale += self.valeurs[i]
        if poids_total > self.budget:
            return 0
        else:
            return valeur_totale

    def algorithme_genetique(self):
        """les parametres de l'algo on ete defini au haut du fichier """


        """on choisit au hasard au debut la population"""
        population = []
        for i in range(taille_population):
            solution = []
            for i in range(len(self.poids)):
                a=random.randint(0,1)
                solution.append(a)
            population.append(solution)

        # Évaluation de la population
        evals = []
        for solution in population:
            eval = self.evaluation(solution)
            evals.append((solution, eval))

        population=evals

        for iteration in range(nombre_iterations):

            evals = sorted(population, key=lambda x: x[1], reverse=True)

            #choix des parents
            #on fait "reproduire" les solutions avec la meilleure evaluation
            parents = []
            for i in range(int(taille_population / 2)):
                parent1 = random.choice(evals[:int(taille_population / 4)])[0]
                parent2 = random.choice(evals[:int(taille_population / 4)])[0]
                parents.append((parent1, parent2))


            # Croisement
            #on mélange la génétique des deux parents pour avoir la genetique de l'enfant
            enfants = []
            for parent1, parent2 in parents:
                enfant=[]
                point_croisement = random.randint(1, len(parent1) - 1)
                for i in range(point_croisement):
                    enfant.append(parent1[i])
                for i in range(point_croisement,len(parent1)):
                    enfant.append(parent2[i])
                enfants.append(enfant)

            # Mutation
            for enfant in enfants:

                for i in range(len(enfant)):
                    if random.random() < taux_mutation:
                        enfant[i] = 1 - enfant[i]

            #on remplace les solutions moins bonnes par les solutions enfants
            nouvelle_population = []
            for i in range(int(taille_population / 2)):
                nouvelle_population.append(evals[i][0])
            for enfant in enfants:
                eval = self.evaluation(enfant)
                nouvelle_population.append((enfant, eval))
            population = nouvelle_population

            for enfant in enfants:
                 eval = self.evaluation(enfant)
                 population.append((enfant, eval))


            meilleure_solution = sorted(population, key=lambda x: x[1], reverse=True)[0]
            print(meilleure_solution)


        return meilleure_solution






















#
