from Graph import Graph
from Vertex import Vertex

# only saving the index of vertex not the dist
# get dist from adj list


class Heap:

    # init
    def __init__(self, adjacency_list):
        self.adj_list = adjacency_list
        self.array = [0]
        self.count = 0
        # self.pos = []

    def sort_heap(self):
        i = self.count / 2
        while i >= 1:
            self.heapify_down(i)
            i = i - 1

    def build_min_heap(self, list):
        for tmp in list:
            self.count = self.count + 1
            self.array.append(tmp)
        self.sort_heap()

    def insert(self, num):
        self.array.append(num)
        self.count = self.count + 1
        self.heapify_up(self.count)

    def delete_min(self):
        min_idx = self.array[1]
        self.array[1] = self.array[self.count]
        del self.array[self.count]
        self.count = self.count - 1
        if self.count >= 1:
            self.heapify_down(1)
        return min_idx

    def get_min(self):
        return self.array[1]

    def heapify_down(self, i):
        l = self.left(i)
        r = self.right(i)
        i = int(i)
        l = int(l)
        r = int(r)
        # get the vertex in i
        # print(i)
        # print(l)
        # print(r)
        i_vertex = self.get_vertex_by_idx(i)
        smallest = i
        smallest_val = i_vertex.get_dist_to_orgn()
        if l <= self.count:
            # get the vertex in l
            l_vertex = self.get_vertex_by_idx(l)
            # get/compare distance to previous node between i and l
            if l_vertex.get_dist_to_orgn() < i_vertex.get_dist_to_orgn():
                smallest = l
                smallest_val = l_vertex.get_dist_to_orgn()
        # else:
        #     smallest = i
        #     smallest_val = i_vertex.get_dist_to_prev()
        if r <= self.count:
            # get the vertex in r
            r_vertex = self.get_vertex_by_idx(r)
            # get/compare distance to previous node between largest and r
            if r_vertex.get_dist_to_orgn() < smallest_val:
                smallest = r
        if smallest != i:
            self.swap_min_heap_node(smallest, i)
            self.heapify_down(smallest)
    # end

    def heapify_up(self, i):
        if i <= 1:
            pass
        else:
            i_vertex = self.get_vertex_by_idx(i)
            parent = self.parent(i)
            parent_vertex = self.get_vertex_by_idx(parent)
            while i > 1 and i_vertex.get_dist_to_orgn() < parent_vertex.get_dist_to_orgn():
                self.swap_min_heap_node(i, parent)
                i = parent
                if i <= 1:
                    pass
                else:
                    i_vertex = parent_vertex
                    parent = self.parent(i)
                    parent_vertex = self.get_vertex_by_idx(parent)
    # end

    def get_vertex_by_idx(self, i):
        # print(i)
        i_adj_index = self.array[i]
        return self.adj_list.get_vertex(i_adj_index)

    @staticmethod
    def left(index):
        return 2 * index

    @staticmethod
    def right(index):
        return 2 * index + 1

    @staticmethod
    def parent(index):
        if index % 2 == 0:
            return index / 2
        else:
            return (index - 1) / 2

    def swap_min_heap_node(self, a, b):
        tmp = self.array[a]
        self.array[a] = self.array[b]
        self.array[b] = tmp

    def __contains__(self, item):
        if item in self.array:
            return True
        else:
            return False
