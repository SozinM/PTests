
class GraphDestination():
    def __str__(self):
        string = ''
        for item in self.reachable_edges:
            string += '%d\n'%(item)
        return string

    def __init__(self,dictionary,initial_edge):
        self.graph = dictionary.copy()
        self.checked_edges = set()
        self.reachable_edges = set()
        self.check_reachable_edges(initial_edge)

    def check_reachable_edges(self,edge):
        if not isinstance(edge,int): #check there is edge
            return
        queue = [edge]
        while(queue):
            for item in queue:
                if item in self.checked_edges:
                    queue.remove(item)
                    continue
                queue.remove(item)
                self.checked_edges.add(item)
                self.reachable_edges.add(item)
                set_of_edges = self.graph.get(item)
                if set_of_edges == None:  #Edge is not declared
                    continue
                queue.extend(set_of_edges)
        print self
        #return self.checked_edges




def main():
    data = {
        1: [2, 3],
        2: [3, 4],
        4: [1],
    }
    GraphDestination(data,1)

if __name__ == '__main__' : main()

