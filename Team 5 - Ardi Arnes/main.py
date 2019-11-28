import pandas as pd
import math

import Customer
import Hub
import Warehouse

df_customers = pd.read_csv("customer_data.csv")
df_hubs = pd.read_csv("hub_data.csv")
df_warehouses = pd.read_csv("warehouse_data.csv")

### Customers data
customers_id = list(df_customers["id"].values)
customers_latitude = list(df_customers["Latitude"].values)
customers_longitude = list(df_customers["Longitude"].values)

### Hubs data
hubs_name = list(df_hubs["Hub"].values + "_H")
hubs_latitude = list(df_hubs["Latitude"].values)
hubs_longitude = list(df_hubs["Longitude"].values)

### Warehouses data
warehouses_name = list(df_warehouses["Warehouse"].values + "_W")
warehouses_latitude = list(df_warehouses["Latitude"].values)
warehouses_longitude = list(df_warehouses["Longitude"].values)



class Warehouse:
    def __init__(self, name, latitude, longitude):
        self.name = name
        self.latitude = latitude
        self.longitude = longitude



class Hub:
    def __init__(self, name, latitude, longitude):
        self.name = name
        self.latitude = latitude
        self.longitude = longitude
        self.dist_to_warehouses = self.dist_to_warehouses()      # Warehouse name, distance
        self.nearest_warehouse = self.nearest_warehouse()
        self.dist_to_hubs = self.dist_to_hubs()
        self.nearest_hub = self.nearest_hub()
        self.nearest_place = self.nearest_place()
    
    def dist_to_warehouses(self):
        distances = [[warehouses_name[i], math.sqrt(pow(self.latitude - warehouses_latitude[i],2) + pow(self.longitude - warehouses_longitude[i],2))] for i in range(len(warehouses_name))]
        distances.sort(key=lambda x: x[1])
        return distances
    
    def nearest_warehouse(self):
        return self.dist_to_warehouses[0]

    def dist_to_hubs(self):
        distances = [[hubs_name[i], math.sqrt(pow(self.latitude - hubs_latitude[i],2) + pow(self.longitude - hubs_longitude[i],2))] for i in range(len(hubs_name))]
        distances.sort(key=lambda x: x[1])
        return distances

    def nearest_hub(self):
        return self.dist_to_hubs[0]
    
    def nearest_place(self):
        if self.dist_to_hubs[1][1] < self.dist_to_warehouses[0][1]:         # Why not [0][1]? Because we don't wanna compare a hub with itself.
            return self.dist_to_hubs[1]
        elif self.dist_to_hubs[1][1] > self.dist_to_warehouses[0][1]:
            return self.dist_to_warehouses[0]



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



warehouses = [Warehouse(warehouses_name[i], warehouses_latitude[i], warehouses_longitude[i]) for i in range(len(warehouses_name))]
hubs = [Hub(hubs_name[i], hubs_latitude[i], hubs_longitude[i]) for i in range(len(hubs_name))]
customers = [Customer(customers_id[i], customers_latitude[i], customers_longitude[i]) for i in range(len(customers_id))]

def getAllRoutes():
	total_travel_distance = 0

	for i in range(len(customers_id)):
		cumulative_distance = 0
		
		print("Customer no", i+1)

		for j in range(len(customers[i].route)):

			if customers[i].route[j][0] != customers[i].route[-1][0]:
				print(customers[i].route[j][0], end=" --> ")

			elif customers[i].route[j][0] == customers[i].route[-1][0]:
				print(customers[i].route[j][0])

			cumulative_distance += customers[i].route[j][1]

		total_travel_distance += cumulative_distance
		print("Cumulative distance =",cumulative_distance, "\n\n\n")

	print("Total travel distance =", total_travel_distance)


getAllRoutes()