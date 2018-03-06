import DijkstraAlgorithm
import PrimAlgorithm
from UtilTool import UtilTool

# main method
if __name__ == '__main__':
    # read data from the raw text files
    vertex_list = UtilTool.read_from_vertex('Raw_Data/MapDataVertices.txt')
    edge_list = UtilTool.read_from_edge('Raw_Data/MapDataEdges.txt')
    # adjacency_matrix = make_adjacency_matrix(edge_list)                           # with adja matrix
    # write_to_file('testfile.txt', adjacency_matrix)                               # with adja matrix
    # get start vertex label and end vertex label
    start_point = str(input('Enter the starting source vertex using label\n'))
    end_point = str(input('Enter the ending source vertex using label\n(enter \'tour\' for a graph tour)\n'))
    # get travel method from user
    travel_method = str(input('Enter method of travel\n'))
    # get time method from user
    time_method = str(input('Do you want to minimize time? (yes or no)\n'))
    # dijkstra_adja_matrix(adjacency_matrix, k)                                     # without adjacency list & heap
    # run dijkstra since a end vertex is specified
    if end_point != 'tour':
        # get vertex index from label
        start_point_int = DijkstraAlgorithm.get_index_from_label(vertex_list, start_point)
        end_point_int = DijkstraAlgorithm.get_index_from_label(vertex_list, end_point)
        # make adjacency list in a graph form using different parameters
        graph_1 = UtilTool.make_adjacency_list(vertex_list, edge_list, travel_method, time_method)
        # run the dijkstra algorithm
        calc_list_1 = DijkstraAlgorithm.dijkstra_adja_list(graph_1, start_point_int)
        # output everything
        if travel_method == 'walk':
            if time_method == 'no':
                DijkstraAlgorithm.write_to_output_file(start_point_int, end_point_int, 'out_put_dijkstra.txt', calc_list_1, vertex_list, edge_list, True, True)
            else:
                DijkstraAlgorithm.write_to_output_file(start_point_int, end_point_int, 'out_put_dijkstra.txt', calc_list_1, vertex_list, edge_list, True, False)
        else:
            if time_method == 'no':
                DijkstraAlgorithm.write_to_output_file(start_point_int, end_point_int, 'out_put_dijkstra.txt', calc_list_1, vertex_list, edge_list, False, True)
            else:
                DijkstraAlgorithm.write_to_output_file(start_point_int, end_point_int, 'out_put_dijkstra.txt', calc_list_1, vertex_list, edge_list, False, False)
    else:
        start_point_int = PrimAlgorithm.get_index_from_label(vertex_list, start_point)
        graph_2 = UtilTool.make_adjacency_list(vertex_list, edge_list, travel_method, time_method)
        # run the prim's algorithm from PrimeAlgorithm.py
        calc_list_2 = PrimAlgorithm.prim_adja_list(graph_2, start_point_int)
        # run DFS in different cases to find the shortest path
        if travel_method == 'walk':
            if time_method == 'no':
                PrimAlgorithm.get_tour(start_point_int, calc_list_2, 'out_put_prim.txt', vertex_list, edge_list, True, True)
            else:
                PrimAlgorithm.get_tour(start_point_int, calc_list_2, 'out_put_prim.txt', vertex_list, edge_list, True, False)
        else:
            if time_method == 'no':
                PrimAlgorithm.get_tour(start_point_int, calc_list_2, 'out_put_prim.txt', vertex_list, edge_list, False, True)
            else:
                PrimAlgorithm.get_tour(start_point_int, calc_list_2, 'out_put_prim.txt', vertex_list, edge_list, False, False)
    exit(0)
