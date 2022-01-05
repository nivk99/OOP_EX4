from typing import List

from matplotlib.cbook import Stack

from src.graph import GraphInterface
from src.graph.DiGraph import DiGraph
from src.graph.GraphAlgoInterface import GraphAlgoInterface
from queue import PriorityQueue

from src.graph.Node_Data import Node_Data


class GraphAlgo(GraphAlgoInterface):
    """
In this class you can find methods that work on the graph. In this class you can see a number of different algorithms that help this class.
    """

    def __init__(self, diGraph: GraphInterface = DiGraph()):
        """
           constructor
        :param diGraph: GraphInterface
        """
        self._diGraph = diGraph

    def get_graph(self) -> GraphInterface:
        """
        :return: This method returns the underlying graph of which this class works
        """
        return self._diGraph


    def shortest_path1(self, id1: int, id2: int) -> float:
        arr={}
        for v in self._diGraph.get_all_v().keys():
            arr[v]=float('inf')
        arr[id1]=0
        for v in self._diGraph.get_all_v().keys():
            for e in self._diGraph.all_out_edges_of_node(v).keys():
                arr[e]=min(arr[e],arr[v]+self._diGraph.all_out_edges_of_node(v)[e])
        return arr[id2]


    def shortest_path(self, id1: int, id2: int) -> (float, list):
        """
        * This method computes the the shortest path between src to dest - as an ordered List of nodes:
        * src--> n1-->n2-->...dest
        * if no such path --> returns null;
        *  src - start node
        *  dest - end (target) node
        * Method uses Dijkstra's algorithm The explanation of the algorithm can be seen on
        * https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm
        :param id1:src  - start node
        :param id2:dest - end (target) nod
        :return: list
        """
        if self._diGraph.v_size() == 0 or self._diGraph.e_size() == 0 or id1 not in self._diGraph.get_all_v().keys() or id2 not in self._diGraph.get_all_v().keys():
            return float('inf'), []
        if id1 == id2:
            return 0, id1
        ans = []
        min_heap = PriorityQueue()
        src_node: Node_Data = self._diGraph.get_all_v()[id1]
        dest_node: Node_Data = self._diGraph.get_all_v()[id2]
        for n in self._diGraph.get_all_v().values():
            n.setWeight(float('inf'))
            n.setTag(0)

        src_node.setWeight(0)
        min_heap.put(src_node.getKey())
        while not min_heap.empty():
            node_pq: Node_Data = self._diGraph.get_all_v()[min_heap.get()]
            for v in self._diGraph.all_out_edges_of_node(node_pq.getKey()).keys():
                node_dest: Node_Data = self._diGraph.get_all_v()[v]
                weight: float = node_pq.getWeight() + self._diGraph.all_out_edges_of_node(node_pq.getKey())[v]
                if float(node_dest.getWeight()) > float(weight):
                    node_dest._node_weight = weight
                    node_dest._node_tag = node_pq.getKey()
                    min_heap.put(node_dest.getKey())

        st = Stack()
        st.push(dest_node)
        sum: float = 0
        while dest_node is not src_node:
            dest = dest_node
            dest_node = self._diGraph.get_all_v()[dest_node.getTag()]
            st.push(dest_node)
            try:
                sum += self._diGraph.all_out_edges_of_node(dest_node.getKey())[dest.getKey()]
            except Exception:
                return float('inf'), []

        while not st.empty():
            ans.append(st.forward().getKey())
            st.remove(st.forward())

        return sum, ans

    def TSP(self, node_lst: List[int]) -> (List[int], float):
        """
        * This method Computes a list of consecutive nodes which go over all the nodes in cities.
        *  the sum of the weights of all the consecutive (pairs) of nodes (directed) is the "cost" of the solution .
         * The function checks for each vertex where it is best to go. This is a greedy method
        :param node_lst: list  key nods
        :return: list nods and sum
        """
        ans = []
        arr = []
        for v in node_lst:
            temp = []
            temp.append(v)
            ans.append(temp)

        for i in range(len(node_lst)):
            list_cities = [k for k in node_lst]
            id = list_cities[i]
            list_cities.remove(id)
            total: float = 0
            for j1 in range(len(list_cities)):
                sort: float = float('inf')
                kay: int = list_cities[0]
                remov = kay
                for j2 in list_cities:
                    w: float = float(self.shortest_path(id, j2)[0])
                    if sort > w:
                        sort = w
                        remov = j2
                ans[i].append(remov)
                total += sort
                id = remov
                if remov not in list_cities:
                    break
                list_cities.remove(remov)
            k = node_lst[i]
            g = self._diGraph.get_all_v()[k]
            g.setInfo(total)
            arr.append(g)

        ind = 0
        w = float('inf')
        j = -1
        for k1 in arr:
            j += 1
            t = float(k1.getInfo())
            if w > t:
                w = t
                ind = j

        return ans[ind], w






