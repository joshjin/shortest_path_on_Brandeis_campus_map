import numpy
from Graph import Graph


class UtilTool:

    # read vertices from MapDataVertices
    @staticmethod
    def read_from_vertex(file_name):
        edge_file = open(file_name, 'r')
        index = []
        lable = []
        x = []
        y = []
        name = []
        for line in edge_file:
            if "//" in line:
                pass
            elif len(line) > 5:
                segments = line.split()
                index.append(int(segments[0]))
                lable.append(segments[1])
                x.append(int(segments[2]))
                y.append(int(segments[3]))
                name_list = segments[4::1]
                name.append(" ".join(name_list))
                v_list = numpy.rec.fromarrays((index, lable, x, y, name), names=('#', 'lable', 'x', 'y', 'name'))
        edge_file.close()
        # print(v_list)
        return v_list

    # read edges from MapDataEdges
    @staticmethod
    def read_from_edge(file_name):
        # Edge format is: # label1 label2 v1 v2 length, angle, direction (C) name
        edge_file = open(file_name, 'r')
        index = []
        label1 = []
        label2 = []
        v1 = []
        v2 = []
        length = []
        angle = []
        direction = []
        C = []
        name = []
        for line in edge_file:
            if "//" in line:
                pass
            elif len(line) > 8:
                segments = line.split()
                index.append(int(segments[0]))
                label1.append(segments[1])
                label2.append(segments[2])
                v1.append(int(segments[3]))
                v2.append(int(segments[4]))
                length.append(int(segments[5]))
                angle.append(int(segments[6]))
                direction.append(segments[7])
                C.append(segments[8])
                name_list = segments[9::1]
                name.append(" ".join(name_list))
                e_list = numpy.rec.fromarrays((index, label1, label2, v1, v2, length, angle, direction, C, name), \
                                              names=(
                                              '#', 'label1', 'label2', 'v1', 'v2', 'length', 'angle', 'direction', 'C',
                                              'name'))
        edge_file.close()
        # print(e_list)
        return e_list


    @staticmethod
    def calc_time(length, key, method1):
        if method1:
            tmp = length / 272
            if key == '(F)' or key == '(f)':
                pass
            elif key == '(U)' or key == '(u)':
                tmp = tmp / 0.9
            elif key == '(D)' or key == '(d)':
                tmp = tmp / 1.1
            elif key == '(s)':
                tmp = tmp / 0.5
            elif key == '(t)':
                tmp = tmp / 0.9
            elif key == '(b)':
                pass
            else:
                pass
        else:
            tmp = float(length) / 272
            if key == '(F)':
                tmp = tmp / 2.0
            elif key == '(U)':
                tmp = tmp / 1.1
            elif key == '(D)':
                tmp = tmp / 5.0
            else:
                tmp = tmp / 2.0
        return tmp

    # make adjacency list using graph and vertex
    @staticmethod
    def make_adjacency_list(vertex_list_tmp, edge_list_tmp, flag1, flag2):
        g = Graph()
        for vertex in vertex_list_tmp:
            g.add_vertex(vertex[0])
        if flag1 == 'walk':
            if flag2 == 'no':
                for edge in edge_list_tmp:
                    g.add_edge(edge[3], edge[4], edge[5])
            elif flag2 == 'yes':
                for edge in edge_list_tmp:
                    tmp = float(edge[5]) / 272
                    if edge[8] == '(F)' or edge[8] == '(f)':
                        g.add_edge(edge[3], edge[4], tmp)
                    elif edge[8] == '(U)' or edge[8] == '(u)':
                        tmp = tmp / 0.9
                        g.add_edge(edge[3], edge[4], tmp)
                    elif edge[8] == '(D)' or edge[8] == '(d)':
                        tmp = tmp / 1.1
                        g.add_edge(edge[3], edge[4], tmp)
                    elif edge[8] == '(s)':
                        tmp = tmp / 0.5
                        g.add_edge(edge[3], edge[4], tmp)
                    elif edge[8] == '(t)':
                        tmp = tmp / 0.9
                        g.add_edge(edge[3], edge[4], tmp)
                    elif edge[8] == '(b)':
                        g.add_edge(edge[3], edge[4], tmp)
                    else:
                        g.add_edge(edge[3], edge[4], tmp)
        elif flag1 == 'skate':
            if flag2 == 'no':
                for edge in edge_list_tmp:
                    if edge[8] == '(x)' or edge[8] == '(F)' or edge[8] == '(U)' or edge[8] == '(D)':
                        g.add_edge(edge[3], edge[4], edge[5])
            elif flag2 == 'yes':
                for edge in edge_list_tmp:
                    tmp = float(edge[5]) / 272
                    if edge[8] == '(F)':
                        tmp = tmp / 2.0
                        g.add_edge(edge[3], edge[4], tmp)
                    elif edge[8] == '(U)':
                        tmp = tmp / 1.1
                        g.add_edge(edge[3], edge[4], tmp)
                    elif edge[8] == '(D)':
                        tmp = tmp / 5.0
                        g.add_edge(edge[3], edge[4], tmp)
                    else:
                        tmp = tmp / 2.0
                        g.add_edge(edge[3], edge[4], tmp)
        else:
            print('false options')
        return g
