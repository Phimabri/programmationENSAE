
from heapq import *

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
        on suppose qu'ils sont dans la même composante connexe (ce qui nous garantit qu'on arrive à dest)"""
        M = set()
        d = {src: 0}
        p = {}
        suivants = [(0, src)] #Â tas de couples (d[x],x)

        while suivants != []:
            dx, x = heappop(suivants)
            vois=voisin(self.graph,x)
            if x in M:
                continue

            M.add(x)

            for y,w in vois:
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
            return 0,[]
        while x != src:
            x = p[x]
            path.insert(0, x)

        return d[dest], path



    def path_rec(self,src,dest,power,path,visited_nodes):
        for nodes in self.graph[src]:
            node=nodes[0]
            if node == dest and nodes[1]<power :
                return path
            elif nodes[1]<power and node not in visited_nodes:
                visited_nodes.append(node)
                path.append(node)
                path_rec(self,node,power,path,visited_nodes)
        return []


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

    def min_power(self, src, dest):
        """regarder si src et dest sont dans la même composante connexe
        on suppose qu'ils sont dans la même composante connexe (ce qui nous garantit qu'on arrive à dest)"""
        M = set()
        d = {src:0 }
        p = {}
        suivants = [(0, src)] #tas de couples (d[x],x)

        while suivants != []:
            dx, x = heappop(suivants)
            vois=[(i[0],i[1]) for i in self.graph[src]]
            if x in M:
                continue

            M.add(x)

            for y,w in vois:
                if y in M:
                    continue
                dy = max(dx,w)
                if y not in d or d[y] > dy:
                    d[y] = dy
                    heappush(suivants, (dy, y))
                    p[y] = x
        print(d)



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
