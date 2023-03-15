
from heapq import *
import networkx as nx
import matplotlib.pyplot as plt


def voisin(graph,x):
    """fonction qui renvoie une liste de couple formée des voisins de x, de leur puissance et leur distance"""
    vois=[]
    for i in graph[x]:
        vois.append((i[0],i[1],i[2]))
    return vois

def dfs(graph,src,dest,visited,power=0,pere=0):
    """fonction qui fait un dfs pour trouver le chemin entre 2 neouds (src et dest)
    Cette fonction renvoie une liste de couple formé du chemin et de la puissance nécessaire pour emprunter chaque arête """
    visited.append((src,power))
    if src==dest:
        return visited
    else :
        for i in graph.graph[src]:
            if i[0]!=pere:
                result=dfs(graph,i[0],dest,visited,i[1],pere=src)
                if result !=None:
                     return result
        return None


class Graph:
    def __init__(self, nodes=[]):
        self.nodes = nodes
        self.graph = dict([(n, []) for n in nodes])
        self.nb_nodes = len(nodes)
        self.nb_edges = 0



    def __str__(self):
        """Prints the graph as a list of neighbors for each node (one per line)"""
        if not self.graph:
            output = "The graph is empty"
        else:
            output = f"The graph has {self.nb_nodes} nodes and {self.nb_edges} edges.\n"
            for source, destination in self.graph.items():
                output += f"{source}-->{destination}\n"
        return output

    def add_edge(self, node1, node2, power_min, dist=1):    #complexité en O(#voisins de node1)
        """
        Adds an edge to the graph. Graphs are not oriented, hence an edge is added to the adjacency list of both end nodes.

        Parameters:
        -----------
        node1: NodeType
            First end (node) of the edge
        node2: NodeType
            Second end (node) of the edge
        power_min: numeric (int or float)
            Minimum power on this edge
        dist: numeric (int or float), optional
            Distance between node1 and node2 on the edge. Default is 1.
        """
        if node2 not in self.graph[node1]:
            self.nb_edges +=1
            self.graph[node1].append([node2,power_min,dist])
            self.graph[node2].append([node1,power_min,dist])




    def get_path_with_power(self, src, dest, power):      #complexité en O((#V)**2)
        """regarder si src et dest sont dans la même composante connexe
        s'ils sont dans la même composante connexe cela nous garantit que l'algo s'arrête car on atteindra la destination
        (sous réserve de ne pas tourner en rond : il faudra donc enregistrer les noeuds deja visités)"""
        cc=self.connected_components()
        for i in cc:
            if src in i :
                if dest not in i:
                    return None,None
                else:

                    """ on applique ensuite une version de l'algo de Dijkstra modulo le fait qu'on ajoute le noeud seulement
                    si la puissance le permet """
                    M = set()
                    d = {src: 0}
                    p = {}
                    suivants = [(0, src)] # tas de couples (d[x],x)

                    while suivants != []:
                        dx, x = heappop(suivants)
                        vois=voisin(self.graph,x)
                        """ on regarde les voisins du noeud. Ils sont renvoyés sous la forme (x,pow,d[x]) """
                        if x in M:
                            continue

                        M.add(x)

                        for y,pow,w in vois:
                            """ on applique ici la condition de puissance minimum """
                            if pow>power :
                                continue #si la puissance n'est pas suffisante on n'explore pas ce passage
                            else:
                                if y in M:
                                    continue
                                dy = dx + w
                                if y not in d or d[y] > dy:
                                    d[y] = dy
                                    heappush(suivants, (dy, y))
                                    p[y] = x
                    path = [dest]
                    x = dest
                    if dest not in p: #s'il n'existe aucun chemin admettant une distance suffisante on renvoie une liste vide
                        return None,None
                    while x != src:
                        x = p[x]
                        path.insert(0, x)

                    return d[dest],path

        return None,None

    def get_path_with_power_without_cc(self, src, dest, power):  #complexité en O((#V)**2)
        "dans cette version on ne vérifie pas que la source et la destination appartiennent à la même composante connexe"
        "c'est utile pour la deuxieme séance"
        M = set()
        d = {src: 0}
        p = {}
        suivants = [(0, src)] # tas de couples (d[x],x)

        while suivants != []:
            dx, x = heappop(suivants)
            vois=voisin(self.graph,x)
            """ on regarde les voisins du noeud. Ils sont renvoyés sous la forme (x,d[x]) """
            if x in M:
                continue

            M.add(x)

            for y,pow,w in vois:
                """ on applique ici la condition de puissance minimum """
                if pow>power :
                    if suivants==[]:
                        continue
                    else:
                        a,b=heappop(suivants) #si la puissance n'est pas suffisante on n'explore pas ce passage
                else:
                    if y in M:
                        continue
                    dy = dx + w
                    if y not in d or d[y] > dy:
                        d[y] = dy
                        heappush(suivants, (dy, y))
                        p[y] = x

        path = [dest]
        x = dest
        if dest not in p: #s'il n'existe aucun chemin admettant une distance suffisante on renvoie une liste vide
            return None,None
        while x != src:
            x = p[x]
            path.insert(0, x)

        return d[dest], path



    def connected_components(self):    #complexité en O(#V+#E)
        """fonction qui renvoie l'ensemble des composantes connexes d'un graphe"""

        explored = [] #explored permettra de mémoriser les noeuds déjà vu
        res = [] #res permettra de stocker les différentes composantes connexes, ce sera donc une liste de liste de noeuds
        def connected(self,node,neighbors):
            if node not in neighbors: #si node n'a pas déjà été mis dans la composante connexe
                neighbors.append(node)
                to_visit = [i[0] for i in self.graph[node]] #to_visit est l'ensemble des voisins de node
                for n in to_visit:
                    if n not in neighbors:
                        connected(self,n,neighbors)
                return neighbors
            else:
                return neighbors

        for n in self.nodes:
            if n not in explored: #si n n'est pas dans explore alors il n'appartient à aucune des composantes connexes déjà traitées
                cc=connected(self,n,[])
                res.append(cc) #on ajoute à res la composante connexe de n
                explored += cc #on ajoute à explored tous les noeuds visités pendant l'appel de connected
        return res



    def connected_components_set(self):   #complexité en O(#V+#E)
        """
        The result should be a set of frozensets (one per component),
        For instance, for network01.in: {frozenset({1, 2, 3}), frozenset({4, 5, 6, 7})}
        """
        return set(map(frozenset, self.connected_components()))


    def exist_path(self,src,dest,power,visited):    #complexité en O((#V)**2)
        """ fonction qui fait un dfs et renvoie s'il existe un chemin et si oui renvoie ce chemin"""
        """ cette fonction est utlisée dans min_power"""
        visited.append(src)
        if src==dest:
            return True, visited
        else:
            for i in self.graph[src]:
                if i[0] not in visited:
                    if i[1]<=power:
                        result = self.exist_path(i[0],dest,power,visited)
                        if result[0]:
                            return result
            return False,None

    def min_power(self,src,dest):   #complexité en O(log(#V)*(#V**2))
        """on commence par stocker toutes les puissances dans une liste"""
        puissances_liste=[]
        for i in self.graph:
            for j in range(len(self.graph[i])):
                puissances_liste.append(self.graph[i][j][1])

        puissances_liste.sort()
        """on va par dichotomie tester pour une puissance choisie s'il existe un chemin"""
        path=None
        debut=0
        fin=len(puissances_liste)
        puissances_exploree=[]
        if fin%2==0:
            while debut+1!=fin:
                a=int((debut+fin)/2)
                power=puissances_liste[a]
                #puissances_exploree permet d'eviter de devoir parcourir tout le graphe à nouveau quand la puissance
                # a deja ete exploree (car il y a des doublons dans la liste des puissances)
                for i in puissances_exploree:
                    if i[0]==power:
                        if i[1]:
                            fin=a
                        else :
                            debut=a
                exist,chemin = self.exist_path(src,dest,power,[])
                if exist==True:
                    fin=a
                    path=chemin
                    puissances_exploree.append((power,True))
                else :
                    debut=a
                    puissances_exploree.append((power,False))
            return puissances_liste[a],path
        else:
            while debut+1!=fin:
                a=int((debut+fin)/2)
                power=puissances_liste[a]
                for i in puissances_exploree:
                    if i[0]==power:
                        if i[1]:
                            fin=a
                        else :
                            debut=a
                exist,chemin=self.exist_path(src,dest,power,[])
                if exist==True:
                    fin=a
                    path=chemin
                    puissances_exploree.append((power,True))

                else :
                    debut=a
                    puissances_exploree.append((power,False))

            return puissances_liste[a],path


    """ Les fonctions find path et min_power2 etaient une première approche pour min power mais la complexité
    est beaucoup trop elevee donc on a refait min power"""

    def find_path(self, src, dest, path=[],puissance=0):  #complexité en O(#V!)

        """ fonction qui renvoie l'ensemble des chemins possibles allant de src à dest (sans contrainte de puissance)
        sous forme de liste de couple (chemin,max puissance requis pour passer par ce chemin)"""
        # Ajouter le noeud de départ au chemin
        path = path + [(src,puissance)]
        # Si le noeud de départ est le même que le noeud d'arrivée, retourner le chemin et la puissance max du chemin
        if src == dest:
            max=path[0][1]
            for i,j in path:
                if j>max:
                    max=j

            return [[path,max]]
        # Si le noeud de départ n'est pas dans le graphe, retourner une liste vide
        if src not in self.graph:
            return []

        # Initialiser une liste vide pour stocker tous les chemins possibles
        possible_paths = []

        # Explorer tous les voisins du noeud de départ
        for voisin in self.graph[src]:
            # Vérifier si le voisin n'est pas déjà dans le chemin
            deja_vu=False
            for i,j in path :
                if voisin[0]==i:
                    deja_vu=True
                # Récursivement explorer le voisin et ajouter tous les chemins possibles dans la liste
            if deja_vu==False:
                new_paths = self.find_path(voisin[0], dest, path,voisin[1])
                for n_path in new_paths:
                    possible_paths.append(n_path)

        # Retourner tous les chemins possibles
        return possible_paths

    def min_power2(self, src, dest):           #complexité en O(#V!)
        """Attention cette version a une complexité trop importante"""

        """ avec la fonction find_path on va trouver tous les chemins allant de src à dest
        puis on va pour chacun de ces chemins regarder le puissance maximale nécessaire pour l'emprunter
        on prendra alors le min des puissances de tous les chemins pour connaitre la puissance minimale requise"""
        cc=self.connected_components()

        for i in cc:
            if src in i :
                if dest not in i:
                    return None,None
                else:
                    paths=self.find_path(src,dest)
                    min=paths[0][1]
                    chemin_minimal=paths[0][0]
                    for chemin in paths:
                         if chemin[1]<min:#chemin[1] est la puissance maximale requise pour le chemin
                            min=chemin[1]
                            chemin_minimal=chemin[0]
                    return [i for i,j in chemin_minimal],min



    """ Pour cette fonction nous avons utilisé le module networkx car on arrivait pas à installer graphviz """

    def draw_graph(self):
        G = nx.Graph()
        for node in self.graph:
            neighbors = self.graph[node]
            G.add_node(node)
            for neighbor in neighbors:
                G.add_edge(node, neighbor[0], weight=neighbor[1])
        pos = nx.spring_layout(G)
        nx.draw_networkx_nodes(G, pos)
        nx.draw_networkx_edges(G, pos)
        nx.draw_networkx_edge_labels(G, pos, edge_labels=nx.get_edge_attributes(G, 'weight'))
        nx.draw_networkx_labels(G, pos)
        plt.show()


    def min_power_kruskal(self,minimal_graph,src,dest): #complexité en O((#V**2)*#E
        """ cette fonction commence par trouver le chemin entre src et dest (qui est unique car c'est un arbre)
        puis on regarde la puissance minimale requise pour pouvoir emprunter ce chemin """
        chemin=dfs(minimal_graph,src,dest,[])
        #dfs renvoie une liste de chemin et de puissances pour emprunter chaque arête
        max=chemin[0][1]
        List=[]
        for i in chemin:
            List.append(i[0])
            if i[1]>max:
                max=i[1]
        return max,List



def graph_from_file(filename):
    """
    Reads a text file and returns the graph as an object of the Graph class.

    The file should have the following format:
        The first line of the file is 'n m'
        The next m lines have 'node1 node2 power_min dist' or 'node1 node2 power_min' (if dist is missing, it will be set to 1 by default)
        The nodes (node1, node2) should be named 1..n
        All values are integers.

    Parameters:
    -----------
    filename: str
        The name of the file

    Outputs:
    -----------
    G: Graph
        An object of the class Graph with the graph from file_name.
    """

    with open(filename, "r") as file:
        lines = file.readlines()
        """ on transforme le fichier texte (qui est un tableau) en une liste de liste"""
        list_of_lists = [line.split() for line in lines]
        " on convertit la liste de string en une liste de int"
        tableau =[list(map(int, i)) for i in list_of_lists]

    g1=Graph([i for i in range(1,tableau[0][0]+1)])
    for i in range(1,len(tableau)):
        if len(tableau[i])<4:
            g1.add_edge(tableau[i][0],tableau[i][1],tableau[i][2])
        else :
            g1.add_edge(tableau[i][0],tableau[i][1],tableau[i][2],tableau[i][3])

    return g1



class UnionFind():

    def __init__(self):
        self.dico = {}

    def makeSet(self,elt):
        self.dico[elt]=elt

    def find(self,elt):
        if self.dico[elt]!=elt:
            self.dico[elt] = self.find(self.dico[elt])
        return self.dico[elt]

    def union(self,e1,e2):
        i = self.find(e1)
        j = self.find(e2)
        self.dico[i]=j
        return None



def takeThird(element):
    return element[2]


def kruskal(g):            #complexité en O((#E)*(#V))
    A = Graph(g.nodes)     #l'arbre couvrant est constitué des mêmes noeuds que g
    list = []              #on initialise la liste des arrêtes
    for node in g.nodes:
        list += [[node,g.graph[node][i][0],g.graph[node][i][1]] for i in range(len(g.graph[node]))]
    list.sort(key=takeThird)     #la liste triée contient des doublons mais ce n'est pas un problème dans notre cas
    E = UnionFind()
    for node in g.nodes:
        E.makeSet(node)
    counter = 0
    for edge in list:                     # on parcourt la liste triée des arrêtes
        if counter < g.nb_nodes-1:    #si counter = g.nb_nodes, l'arbre couvrant est terminé
            if E.find(edge[0])!=E.find(edge[1]):       #on vérifie que les deux sommets ne sont pas la même composante connexe sinon on crée un cycle
                A.add_edge(edge[0],edge[1],edge[2],dist=1)
                E.union(edge[0],edge[1])      #les deux sommets sont désormais dans la même composante connexe
                counter+=1
        else:
            break
    return A






















#
