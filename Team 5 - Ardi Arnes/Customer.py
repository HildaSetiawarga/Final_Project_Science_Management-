class Customer:
    def __init__(self, name, latitude, longitude):
        self.name = name
        self.latitude = latitude
        self.longitude = longitude
        self.dist_to_warehouses = self.dist_to_warehouses()      # Warehouse name, distance
        self.nearest_warehouse = self.nearest_warehouse()
        self.dist_to_hubs = self.dist_to_hubs()
        self.nearest_hub = self.nearest_hub()
        self.nearest_place = self.nearest_place()
        self.route = self.route()

    
    def dist_to_hubs(self):
        distances = [[hubs_name[i], math.sqrt(pow(self.latitude - hubs_latitude[i],2) + pow(self.longitude - hubs_longitude[i],2))] for i in range(len(hubs))]
        distances.sort(key=lambda x: x[1])
        return distances
    
    def nearest_hub(self):
        return self.dist_to_hubs[0]

    def dist_to_warehouses(self):
        distances = [[warehouses_name[i], math.sqrt(pow(self.latitude - warehouses_latitude[i],2) + pow(self.longitude - warehouses_longitude[i],2))] for i in range(len(warehouses_name))]
        distances.sort(key=lambda x: x[1])
        return distances
    
    def nearest_warehouse(self):
        return self.dist_to_warehouses[0]
    
    def nearest_place(self):
        if self.dist_to_hubs[0][1] < self.dist_to_warehouses[0][1]:
            return self.dist_to_hubs[0]
        elif self.dist_to_hubs[0][1] > self.dist_to_warehouses[0][1]:
            return self.dist_to_warehouses[0]
    
    def route(self):
        loop = True
        nodes = [[self.name, 0]]
        nodes.append(self.nearest_place)

        while loop == True:
            if nodes[-1][0][-1] == "W":
                loop = False
            elif nodes[-1][0][-1] == "H":
                for i in range(len(hubs_name)):
                    if nodes[-1][0] == hubs[i].name:
                        nodes.append(hubs[i].nearest_place)
        return nodes