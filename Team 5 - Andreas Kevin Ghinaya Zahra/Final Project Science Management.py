import pandas as pd
import numpy as np
import math
from operator import itemgetter
from collections import defaultdict,deque,namedtuple


Customer = pd.read_excel (r'C:\Users\ASUS\Downloads\Dataaa.xlsx' , sheet_name='Customer')
Hub = pd.read_excel (r'C:\Users\ASUS\Downloads\Dataaa.xlsx' , sheet_name='Hubs')
Warehouse = pd.read_excel (r'C:\Users\ASUS\Downloads\Dataaa.xlsx' , sheet_name='Warehouse')

customerID = np.array(Customer.id.values)
customerLatitude = np.array(Customer.Latitude.values)
customerLongitude = np.array(Customer.Longitude.values)
hubID = np.array(Hub.Hub.values)
hubLatitude = np.array(Hub.Latitude.values)
hubLongitude = np.array(Hub.Longitude.values)
warehouseID = np.array(Warehouse.Warehouse.values)
warehouseLatitude = np.array(Warehouse.Latitude.values)
warehouseLongitude = np.array(Warehouse.Longitude.values)

def computeDist(x1,y1,x2,y2):
    return math.sqrt( ((float(x2)-float(x1))**2)+((float(y2)-float(y1))**2) )

inf = float('inf')
Edge = namedtuple('Edge', 'start, end, cost')


def make_edge(start, end, cost=1):
  return Edge(start, end, cost)

class Graph:
    def __init__(self, edges):
        wrong_edges = [i for i in edges if len(i) not in [2, 3]]
        if wrong_edges:
            raise ValueError('Wrong edges data: {}'.format(wrong_edges))

        self.edges = [make_edge(*edge) for edge in edges]

    @property
    def vertices(self):
        return set(
            sum(
                ([edge.start, edge.end] for edge in self.edges), []
            )
        )

    def get_node_pairs(self, n1, n2, both_ends=True):
        if both_ends:
            node_pairs = [[n1, n2], [n2, n1]]
        else:
            node_pairs = [[n1, n2]]
        return node_pairs

    def remove_edge(self, n1, n2, both_ends=True):
        node_pairs = self.get_node_pairs(n1, n2, both_ends)
        edges = self.edges[:]
        for edge in edges:
            if [edge.start, edge.end] in node_pairs:
                self.edges.remove(edge)

    def add_edge(self, n1, n2, cost=1, both_ends=True):
        node_pairs = self.get_node_pairs(n1, n2, both_ends)
        for edge in self.edges:
            if [edge.start, edge.end] in node_pairs:
                return ValueError('Edge {} {} already exists'.format(n1, n2))

        self.edges.append(Edge(start=n1, end=n2, cost=cost))
        if both_ends:
            self.edges.append(Edge(start=n2, end=n1, cost=cost))

    @property
    def neighbours(self):
        neighbours = {vertex: set() for vertex in self.vertices}
        for edge in self.edges:
            neighbours[edge.start].add((edge.end, edge.cost))

        return neighbours

    def dijkstra(self, source, dest):
        assert source in self.vertices, 'Such source node doesn\'t exist'
        distances = {vertex: inf for vertex in self.vertices}
        previous_vertices = {
            vertex: None for vertex in self.vertices
        }
        distances[source] = 0
        vertices = self.vertices.copy()
        

        while vertices:
            current_vertex = min(
                vertices, key=lambda vertex: distances[vertex])
            vertices.remove(current_vertex)
            if distances[current_vertex] == inf:
                break
            for neighbour, cost in self.neighbours[current_vertex]:
                alternative_route = distances[current_vertex] + cost
                if alternative_route < distances[neighbour]:
                    distances[neighbour] = alternative_route
                    previous_vertices[neighbour] = current_vertex

        path, current_vertex = deque(), dest
        while previous_vertices[current_vertex] is not None:
            path.appendleft(current_vertex)
            current_vertex = previous_vertices[current_vertex]
        if path:
            path.appendleft(current_vertex)
        
        distance_between_nodes = 0
        for index in range(1, len(path)):
            for thing in self.edges:
                if thing.start == path[index - 1] and thing.end == path[index]:
                    distance_between_nodes += thing.cost
        path2 = list(path)
        return path2, distance_between_nodes

class customer:
    def __init__(self, id, custLong, custLat, number):
        self.id = id
        self.custLong = custLong
        self.custLat = custLat
        self.nearestHub = self.nearestHub
        self.number = number
    def nearestHub(self):
        self.custToHub = list([computeDist(self.custLong, self.custLat, hubLongitude[i], hubLatitude[i]), hubID[i]] for i in range(0,len(hubID)))
        self.cTHSorted = sorted(self.custToHub, key = itemgetter(0))
        return self.cTHSorted[0]
    
customersList = [customer(customerID[i], customerLongitude[i], customerLatitude[i], i) for i in range(0,len(customerID))]

class hub:
    def __init__(self, id, hubLong, hubLat, number):
        self.id = id
        self.hubLong = hubLong
        self.hubLat = hubLat
        self.nearestHub = self.nearestHub
        self.nearestWarehouse = self.nearestWarehouse
        self.number = number
    def nearestHub(self):
        self.hubToHub = list([computeDist(self.hubLong, self.hubLat, hubLongitude[i], hubLatitude[i]), hubID[i]] for i in range(0,len(hubID)))
        self.hTHSorted = sorted(self.hubToHub, key = itemgetter(0))
        return self.hTHSorted[1]
    def nearestWarehouse(self):
        self.hubToWarehouse = list([computeDist(self.hubLong, self.hubLat, warehouseLongitude[i], warehouseLatitude[i]), warehouseID[i]] for i in range(0,len(warehouseID)))
        self.hTWSorted = sorted(self.hubToWarehouse, key = itemgetter(0))
        return self.hTWSorted[0]
hubsList = [hub(hubID[i], hubLongitude[i], hubLatitude[i], (i+len(customerID))) for i in range(0, len(hubID))]

class warehouse:
    def __init__(self, id, wareLong, wareLat,number):
        self.id = id
        self.wareLong = wareLong
        self.wareLat = wareLat
        self.number = number
warehouseList = [warehouse(warehouseID[i], warehouseLongitude[i], warehouseLatitude[i], (i+len(customerID) +len(hubID))) for i in range(0, len(warehouseID))]

grapharray = []           

for i in range(0,len(hubID)):
    for j in range(0,len(hubID)):
        if(hubsList[i].id != hubsList[j].id):
            grapharray.append((hubsList[i].id, hubsList[j].id, computeDist(hubsList[i].hubLong,hubsList[i].hubLat,hubsList[j].hubLong,hubsList[j].hubLat)))
        else:
            pass
        
                
for j in range(0,len(hubID)):
    for k in range(0,len(warehouseID)):
        grapharray.append((hubsList[j].id, warehouseList[k].id, computeDist(hubsList[j].hubLong,hubsList[j].hubLat,warehouseList[k].wareLong,warehouseList[k].wareLat)))

graph = Graph(grapharray)
grapharr = []
for i in range(0,len(hubID)):
    for j in range(0,len(warehouseID)):
        defGraph = graph.dijkstra(hubsList[i].id,warehouseList[j].id)
        grapharr.append(defGraph)
        
graphArrSorted = sorted(grapharr, key = itemgetter(1))
dist = []
thisprint = ()
totDist = 0
#print(graphArrSorted)
for i in range (0, len(customerID)):
    print(customersList[i].id, " -> ", customersList[i].nearestHub()[1], " -> ", end = ' ')
    dist.append(customersList[i].nearestHub()[0])
    totDist += customersList[i].nearestHub()[0]
    for j in range (0, len(graphArrSorted)):
        if(customersList[i].nearestHub()[1].lower == graphArrSorted[j][0][0].lower):
            dist[i] += graphArrSorted[j][1]
            totDist += graphArrSorted[j][1]
            print(graphArrSorted[j][0][1], " with distance ", dist[i])
            break
        else:
            pass
        
print (totDist, " or " , totDist*111.699, " km.")
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    # for j in range (0,len(hubID)):
    #     kappa = False
    #     if(str.strip(customersList[i].nearestHub()[1]) == str.strip(hubsList[j].nearestWarehouse()[1])):
    #         dist[i] += hubsList[j].nearestWarehouse()[0]
    #         kappa = True
    #         thisprint1 = (hubsList[j].nearestWarehouse()[1], " with distance = ", dist[i])
    #     elif(customersList[i].nearestHub != hubsList[j].nearestWarehouse()[1]):
    #         for k in range(1, len(warehouseID)):
    #             if(hubsList[j].nearestHub()[1][0] < hubsList[j].nearestWarehouse()[0]):
    #                 if(hubsList[j].nearestHub()[k][1] == hubsList[j].nearestWarehouse()[1]):
    #                     thisprint = hubsList[j].nearestHub()[k][1]
    #             elif(hubsList[j].nearestHub()[1][0] >= hubsList[j].nearestWarehouse()[0]):
    #                 thisprint = hubsList[k].nearestWarehouse()[1]
    # if(kappa):
    #     print(thisprint1)
    # elif(kappa == False):
    #     print(thisprint)
        
            
