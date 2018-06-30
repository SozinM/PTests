from itertools import chain
import json

class Component:

    def __init__(self, *algorithm_list):
        self.algorithm_list = algorithm_list
        self.potentialy_pathes = []
        self.algorithm_paths = dict.fromkeys([algorithm.__class__.__name__ for algorithm in self.algorithm_list],[])

    def __call__(self, source_object):
        result = []
        queue = [source_object]
        while queue:
            result.extend(queue)
            queue = list(chain.from_iterable(
                algorithm(item)
                for item in queue
                for algorithm in self.algorithm_list
            ))
            return result

    def print_pathes(self,source_object):
        self.check_pathes(source_object)
        pass #TODO: print output

    def check_pathes(self,source_object):
        for alghoritm in self.algorithm_list:
            queue = [source_object]
            while(queue):
                for item in queue:
                    if item in self.potentialy_pathes or item == []: #pass checked or empty pathes
                        queue.remove(item)
                        continue
                    self.potentialy_pathes.append(item)
                    self.append_to_algorithm(item, alghoritm) #there is bug
                    queue.remove(item)
                    if isinstance(item,list):
                        for newitem in alghoritm(item[-1]):
                            queue.append([item]+[newitem]) #add new items to queue
                    else:
                        for newitem in alghoritm(item):
                            queue.append([item]+[newitem]) #add new items to queue


    def append_to_algorithm(self,item,algorithm): #there is unknown bug TODO: fix bug
        pathes = self.algorithm_paths.get(algorithm.__class__.__name__)
        print pathes
        if pathes == None:
            self.algorithm_paths.update({algorithm.__class__.__name__: [item]})
        else:
            self.algorithm_paths.update({algorithm.__class__.__name__: pathes.append(item)}) #bug here
        print self.algorithm_paths




class Apple:
    pass


class Orange:
    def __init__(self, number):
        self.number = number


class Lemon:
    pass


class FirstAlgorithm:
    SPECIFICATION = {
                    Orange: [Apple],
                    Lemon: [Orange, Apple]
                    }

    def __call__(self, source_object):
        if isinstance(source_object, Orange):
            return [
                    Apple()
                    for _ in range(source_object.number)
                    ]
        if isinstance(source_object, Lemon):
            return [Orange(3), Apple()]
        return []


class EmptyAlgorithm:
    SPECIFICATION = {}
    def __call__(self, source_object):
        return []

def main():

    C = Component(FirstAlgorithm(),EmptyAlgorithm())
    C.check_pathes(Lemon())
    print C.algorithm_paths


if __name__ == '__main__': main()