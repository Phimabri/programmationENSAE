
from heapq import *
import networkx as nx
import matplotlib.pyplot as plt


def voisin(graph,x):
    """fonction qui renvoie une liste de couple formée des voisins de x et leur distance"""
    vois=[]
    for i in graph[x]:
        if len(i)<3:
            vois.append((i[0],1))
        else:
            vois.append((i[0],i[2]))
    return vois



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

    def add_edge(self, node1, node2, power_min, dist=1):
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




    def get_path_with_power(self, src, dest, power):
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
                        """ on regarde les voisins du noeud. Ils sont renvoyés sous la forme (x,d[x]) """
                        if x in M:
                            continue

                        M.add(x)

                        for y,w in vois:
                            """ on applique ici la condition de puissance minimum """
                            if w>power :
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

        return None,None

    def get_path_with_power_without_cc(self, src, dest, power):
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

            for y,w in vois:
                """ on applique ici la condition de puissance minimum """
                if w>power :
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



    def connected_components(self):
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



    def connected_components_set(self):
        """
        The result should be a set of frozensets (one per component),
        For instance, for network01.in: {frozenset({1, 2, 3}), frozenset({4, 5, 6, 7})}
        """
        return set(map(frozenset, self.connected_components()))





    def find_path(self, src, dest, path=[],puissance=0):

        """ fonction utile pour calculer min_power plus tard"""

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

    def min_power(self, src, dest):
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

    def min_power_without_cc(self,src,dest):
        "fonction qui renvoie min power sans vérifier que source et dest soient dans la même cc"
        paths=self.find_path(src,dest)
        min=paths[0][1]
        chemin_minimal=paths[0][0]
        for chemin in paths:
             if chemin[1]<min:#chemin[1] est la puissance maximale requise pour le chemin
                min=chemin[1]
                chemin_minimal=chemin[0]
        return [i for i,j in chemin_minimal],min


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
