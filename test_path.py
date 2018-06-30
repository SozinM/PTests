from itertools import chain
import json

class Component:

    def __init__(self, *algorithm_list):
        self.algorithm_list = algorithm_list
        self.potentialy_pathes = []
        self.algorithm_paths = {}
        for algorithm in algorithm_list:
            self.algorithm_paths.update({algorithm.__class__.__name__:{}}) #do not use dict.fromkeys

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
        potentialy_tmp_list = []
        for item in self.potentialy_pathes:
            potentialy_tmp_list.append(self.serialize_path(item))
        output = {}
        output.update(self.algorithm_paths)
        output.update({'Potential':list(set(potentialy_tmp_list))}) #remove duplications
        return output

    def check_pathes(self,source_object):
        for alghoritm in self.algorithm_list:
            queue = [source_object]
            while(queue):
                for item in queue:
                    if item == []: #pass checked or empty pathes
                        queue.remove(item)
                        continue
                    self.potentialy_pathes.append(item)
                    if isinstance(item,list): #item could be path ex: [Lemon,Orange,...]
                        shorted_item = item[-1] #we need original item onward
                    else:
                        shorted_item = item #we need original item onward
                    for callable_item in alghoritm(shorted_item):
                        if callable_item == shorted_item: #to evade recursion
                            continue
                        if isinstance(item,list):
                            self.append_to_algorithm(item,item + [callable_item], alghoritm) #item + callable item = output pathes
                            queue.append(item + [callable_item]) #add new items to queue
                        else:
                            self.append_to_algorithm([item],[item] + [callable_item], alghoritm) # item + callable item = output pathes
                            queue.append([item] + [callable_item])
                    queue.remove(item)


    def append_to_algorithm(self,path,outgoing_path,algorithm):
        '''create dict from pathes'''
        pathes = self.algorithm_paths.get(algorithm.__class__.__name__)
        if pathes == None:
            self.algorithm_paths.update({algorithm.__class__.__name__:
                                             {self.serialize_path(path) :
                                                  [self.serialize_path(outgoing_path)]}
                                         })
        else:
            existing_path = pathes.get(self.serialize_path(path))
            if existing_path == None:
                pathes.update({self.serialize_path(path):[self.serialize_path(outgoing_path)]})
            else:
                if not self.serialize_path(outgoing_path) in existing_path: #dont add duplicates
                    pathes.update({self.serialize_path(path):existing_path + [self.serialize_path(outgoing_path)]})

    def serialize_path(self,path):
        '''list to formatted string'''
        output = ''
        if isinstance(path,list):
            for item in path:
                output +='/%s'%(item.__class__.__name__)
        else:
            output +='/%s'%(path.__class__.__name__)
        return output




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
    print(json.dumps(
        C.print_pathes(Lemon()),
        indent=4
    ))



if __name__ == '__main__': main()
