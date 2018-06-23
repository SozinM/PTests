
class GraphDestination():
    def __str__(self):
        string = ''
        for item in self.reachable_edges:
            string += '%d\n'%(item)
        return string

    def __init__(self,dictionary,initial_edge):
        self.graph = dictionary.copy()
        self.initial_edge = initial_edge
        self.checked_edges = set()
        self.reachable_edges = set()
        self.reachable_edges.add(initial_edge)
        self.check_reachable_edges(initial_edge)

    def check_reachable_edges(self,edge):  #TODO remove recursion
        if not isinstance(edge,int):
            return
        self.checked_edges.add(edge)
        set_of_edges = self.graph.get(edge)
        if set_of_edges == None:  #Edge is not declared
            return
        set_of_edges = set(set_of_edges)
        self.reachable_edges.update(set_of_edges)
        for item in set_of_edges:
            if item not in self.checked_edges:
                self.check_reachable_edges(item)  #TODO remove recursion

def main():
    data = {
        1: [2, 3],
        2: [3, 4],
        4: [1]
    }
    Graph = GraphDestination(data,1)
    print Graph

if __name__ == '__main__' : main()

