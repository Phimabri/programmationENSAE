from graph import Graph, graph_from_file

graphe1=Graph([1,2])
graphe1.add_edge(1,2,10)


data_path = "/Users/maloevain/Desktop/ENSAE1/S2/Programmation/ensae-prog23-main/input/"
file_name1 = "network.01.in"
file_name2 = "network.04.in"
file_name3="routes.1.in"



g1 = graph_from_file(data_path + file_name1)
g2 = graph_from_file(data_path+file_name2)
print(g1)
print(g2)
print(g1.find_path(4,6))
print(g1.min_power(4,6))
print(g2.min_power(1,3))
#g2.draw_graph()

g3=graph_from_file(data_path+file_name3)
print(g3)
#print(g3.min_power_without_cc(1,3))
print(g3.get_path_with_power_without_cc(1,3,1))
