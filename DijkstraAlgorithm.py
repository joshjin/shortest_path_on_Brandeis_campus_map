from Heap import Heap
from Stack import Stack
from UtilTool import UtilTool


"""
@param int idx1: the starting index
@param int idx2: the ending index
@param list e_list: a list of all edges from MapDataEdges.txt
This function takes two vertices and return the end connecting them
"""
def get_edge_from_vertices(idx1, idx2, e_list):
    for path in e_list:
        if path[3] == idx1 and path[4] == idx2:
            return path
    return None


"""
@param Graph G: the graph to set up
@param int s: the index of the starting vertex
This function sets up a adjacency list so it can be used for dijkstra algorithm
"""
def initialize_single_source(G, s):
    list_tmp = G.get_vertices()
    for tmp in list_tmp:
        v_tmp = G.get_vertex(tmp)
        v_tmp.set_dist_to_orgn(99999)
        v_tmp.set_prev(None)
    start_v = G.get_vertex(s)
    start_v.set_dist_to_orgn(0)
    start_v.set_dist_to_prev(0)
    start_v.set_prev(None)


"""
@param int u: the starting index
@param int v: the ending index
@param G adj_list: a graph structure that serves as adjacency list
This function updates distance from u to v
"""
def relax(u, v, adj_list):
    u_vertex = adj_list.get_vertex(u)
    v_vertex = adj_list.get_vertex(v)
    list_tmp = u_vertex.connected_to
    dist = list_tmp.get(v_vertex)
    if v_vertex.get_dist_to_orgn() > u_vertex.get_dist_to_orgn() + dist:
        v_vertex.set_dist_to_orgn(u_vertex.get_dist_to_orgn() + dist)
        v_vertex.set_prev(u)
        v_vertex.set_dist_to_prev(dist)


"""
@param int s: the starting index
@param int t: the ending index
@param string filename: the file name to be written to
@param Graph adj_list: a graph structure that serves as adjacency list
@param list vertex_list: a list of all vertices from MapDataVertices.txt
@param list edge_list: a list of all edges from MapDataEdges.txt
@param boolean method1: a boolean (true for walk, false for skate)
@param boolean method2: a boolean (true for distance first, false for time first)
This function takes all the parameters above and write them into a output file
"""
def write_to_output_file(s, t, filename, adj_list, vertex_list, edge_list, method1, method2):
    outPutFile = open(filename, 'w')
    final_t = t
    idx_stack = Stack()
    dist_stack = Stack()
    total_dist = 0
    total_time = 0
    while t != s:
        t_vertex = adj_list.get_vertex(t)
        prev_tmp = t_vertex.get_prev()
        dist_tmp = t_vertex.get_dist_to_prev()
        idx_stack.push(prev_tmp)
        dist_stack.push(dist_tmp)
        t = prev_tmp
    i = 1
    outPutFile.write('************* WELCOME TO THE BRANDEIS MAP *************\n')
    outPutFile.write('Enter start (return to quit): ' + str(vertex_list[s][4]) + '\n')
    outPutFile.write('Enter finish (or return to do a tour): ' + str(vertex_list[final_t][4]) + '\n')
    if method1:
        outPutFile.write('Have a skateboard (y/n - default=n)?: n\n')
    else:
        outPutFile.write('Have a skateboard (y/n - default=n)?: y\n')
    if method2:
        outPutFile.write('Minimize time (y/n - default=n)?: n\n\n')
    else:
        outPutFile.write('Minimize time (y/n - default=n)?: y\n\n')
    while idx_stack.size() > 1 or idx_stack.size() > 1:
        this_v = idx_stack.pop()
        # print(this_v)
        next_v = idx_stack.peek()
        edge = get_edge_from_vertices(this_v, next_v, edge_list)
        outPutFile.write('From: (' + str(vertex_list[this_v][1]) + ') ' + str(vertex_list[this_v][4]) + '\n')
        outPutFile.write('On: ' + str(edge[9]) + '\n')
        outPutFile.write('walk ' + str(edge[5]) + ' feet in direction ' + str(edge[6]) + ' degrees ' + str(edge[7]) + '\n')
        outPutFile.write('To: (' + str(vertex_list[next_v][1]) + ') ' + str(vertex_list[next_v][4]) +'\n')
        total_dist = total_dist + edge[5]
        time_tmp = UtilTool.calc_time(edge[5], edge[8], method1)
        outPutFile.write('(' + str(time_tmp) + ' min)\n\n')
        total_time = total_time + time_tmp
        i = i + 1
    this_v = idx_stack.pop()
    # print(this_v)
    next_v = final_t
    # print(final_t)
    edge = get_edge_from_vertices(this_v, next_v, edge_list)
    outPutFile.write('From: (' + str(vertex_list[this_v][1]) + ') ' + str(vertex_list[this_v][4]) + '\n')
    outPutFile.write('On: ' + str(edge[9]) + '\n')
    outPutFile.write('walk ' + str(edge[5]) + ' feet in direction ' + str(edge[6]) + ' degrees ' + str(edge[7]) + '\n')
    outPutFile.write('To: (' + str(vertex_list[next_v][1]) + ') ' + str(vertex_list[next_v][4]) +'\n')
    total_dist = total_dist + edge[5]
    time_tmp = UtilTool.calc_time(edge[5], edge[8], method1)
    outPutFile.write('(' + str(time_tmp) + ' min)\n\n')
    total_time = total_time + time_tmp
    outPutFile.write('legs = ' + str(i) + ', distance = ' + str(total_dist) + ', time = ' + str(total_time) + ' min.')


"""
@param Graph G: the graph to set up
@param int s: the index of the starting vertex
This function sets up a adjacency list so it can be used for dijkstra algorithm
"""
def initialize_single_source(G, s):
    list_tmp = G.get_vertices()
    for tmp in list_tmp:
        v_tmp = G.get_vertex(tmp)
        v_tmp.set_dist_to_orgn(99999)
        v_tmp.set_prev(None)
    start_v = G.get_vertex(s)
    start_v.set_dist_to_orgn(0)
    start_v.set_dist_to_prev(0)
    start_v.set_prev(None)


"""
@param int k: the starting index
@param G adj_list: a graph structure that serves as adjacency list
This function is the structure of main dijkstra algorithm
"""
def dijkstra_adja_list(adj_list, k):
    initialize_single_source(adj_list, k)
    Q = Heap(adj_list)
    Q.build_min_heap(adj_list.get_vertices())
    while Q.count > 0:
        u = Q.delete_min()
        u_vertex = adj_list.get_vertex(u)
        u_nbhd_list = u_vertex.get_connections()
        for v in u_nbhd_list:
            v_idx = v.get_id()
            relax(u, v_idx, adj_list)
        Q.sort_heap()
    return adj_list


"""
@param string s_point: the starting index in label form
@param list v_list: a list of all vertices from MapDataVertices.txt
This function returns the index of a vertex by its label
"""
def get_index_from_label(v_list, s_point):
    for vertex in v_list:
        if vertex[1] == s_point:
            return vertex[0]
    return None

