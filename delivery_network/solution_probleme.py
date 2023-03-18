class ResolutionProbleme():

    def __init__(self,filename_camion,filename_puissances,filename_routes):

        data_path = "/Users/maloevain/Desktop/ENSAE1/S2/Programmation/programmationENSAE/input/"

        with open(data_path+filename_camion, "r") as file:
            lines = file.readlines()
            #on transforme le fichier texte (qui est un tableau) en une liste de liste
            list_of_lists = [line.split() for line in lines]
            " on convertit la liste de string en une liste de int"
            tableau =[list(map(int, i)) for i in list_of_lists]

        with open(data_path+filename_puissances, "r") as file:
            lines = file.readlines()
            #on transforme le fichier texte (qui est un tableau) en une liste de liste
            list_of_lists = [line.split() for line in lines]
            " on convertit la liste de string en une liste de int"
            tableau2 =[list(map(int, i)) for i in list_of_lists]

        with open(data_path+filename_routes, "r") as file:
            lines = file.readlines()
            #on transforme le fichier texte (qui est un tableau) en une liste de liste
            list_of_lists = [line.split() for line in lines]
            " on convertit la liste de string en une liste de int"
            tableau3 =[list(map(int, i)) for i in list_of_lists]

        #on stock sous forme de liste l'ensemble des camions, des puissances minimales et des profits pour chaque trajet
        self.liste_camion=tableau[1:]
        self.liste_puissance=tableau2[1:]
        self.liste_profits=tableau3[1:][2]

        self.budget= 25*(10**9)

    def EstTrivial():
        """ fonction qui renvoie un booléen pour savoir si le problème est trivial,
        c'est-à-dire si on a assez d'argent pour acheter des camions capable de couvrir tous les trajets """
        max_power =max(self.liste_puissance)
        for i in range(len(self.liste_camion)):
            #on regarde de manière décroissante (en partant du camion le plus cher au moins cher) s'il existe une solution
            #triviale au probleme
            if self.liste_camion[-(i+1)][0]>max_power and self.liste_camion[-(i+1)][1]*len(self.liste_puissance)<self.budget:
                return True
        return false
