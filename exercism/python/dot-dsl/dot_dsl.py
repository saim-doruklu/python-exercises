from typing import List

NODE, EDGE, ATTR = range(3)


class Node:
    def __init__(self, name, attrs):
        self.name = name
        self.attrs = attrs

    def __eq__(self, other):
        return self.name == other.name and self.attrs == other.attrs


class Edge:
    def __init__(self, src, dst, attrs):
        self.src = src
        self.dst = dst
        self.attrs = attrs

    def __eq__(self, other):
        return (self.src == other.src and
                self.dst == other.dst and
                self.attrs == other.attrs)


def extract_with_type(iterator, type, details):
    try:
        next_item = next(iterator)
    except StopIteration:
        print(details+" is missing")
        raise TypeError(details+" is missing")

    if not isinstance(next_item, type):
        print(details+" has wrong type")
        raise ValueError(details+" has wrong type")
    return next_item


class Graph:
    def __init__(self, data: List[tuple] = None):
        self.nodes = []
        self.edges = []
        self.attrs = {}
        if data is not None:
            if not isinstance(data, list):
                raise TypeError("Bad input format")
            for item in data:
                if len(item) == 0:
                    raise TypeError("Bad input format")
                type = item[0]
                iterator = iter(item)
                next(iterator)
                if type == NODE:
                    name = extract_with_type(iterator, str, str(['NODE']+list(item[1:]))+' : name')
                    attrs = extract_with_type(iterator, dict, str(['NODE']+list(item[1:]))+' : attrs')
                    self.nodes.append(Node(name, attrs))
                elif type == ATTR:
                    key = extract_with_type(iterator, str, str(['ATTR']+list(item[1:]))+' : key')
                    val = extract_with_type(iterator, str, str(['ATTR']+list(item[1:]))+' : value')
                    self.attrs[key] = val
                elif type == EDGE:
                    src = extract_with_type(iterator, str, str(['EDGE']+list(item[1:]))+' : src')
                    dst = extract_with_type(iterator, str, str(['EDGE']+list(item[1:]))+' : dst')
                    attrs = extract_with_type(iterator, dict, str(['EDGE']+list(item[1:]))+' : attrs')
                    self.edges.append(Edge(src, dst, attrs))
                else:
                    raise ValueError("Unknown type")
