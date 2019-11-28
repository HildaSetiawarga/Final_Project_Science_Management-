import pandas as pd
import pprint
import math
import numpy as np

'''
# Load the Data
hub = pd.read_csv('hub.csv')
customer = pd.read_csv('customer.csv')
warehouse = pd.read_csv('warehouse.csv')
'''

# Load Data
xls = pd.ExcelFile(r'Data copy.xlsx')
df = xls.parse('RD Data')

# Select particular frame and make it into list
df_cust = df.iloc[0:30, 0:3]
cust_id = list(df_cust['id'].values)
cust_latitude = list(df_cust['Latitude'].values)
cust_longitude = list(df_cust['Longitude'].values)


list_cust = []
for i in range(len(df_cust)) :
    list_cust.append(
        [cust_id[i], cust_latitude[i], cust_longitude[i]]
    )
total_customer = len(list_cust)

df_hub = df.iloc[0:6,7:10]
hub_hub = list(df_hub['Hub'].values)
hub_latitude = list(df_hub['Latitude.1'].values)
hub_longitude = list(df_hub['Longitude.1'].values)


list_hub = []

for i in range(len(df_hub)) :
    list_hub.append(
        [hub_hub[i], hub_latitude[i], hub_longitude[i]]
    )
total_hub= len(list_hub)

df_warehouse = df.iloc[0:4 , 11:15]
warehouse_warehouse = list(df_warehouse['Warehouse'].values)
warehouse_latitude = list(df_warehouse['Latitude.2'].values)
warehouse_longitude = list(df_warehouse['Longitude.2'].values)


list_warehouse = []

for i in range(len(df_warehouse)) :
    list_warehouse.append(
        [warehouse_warehouse[i], warehouse_latitude[i], warehouse_longitude[i]]
    )
total_warehouse = len(list_warehouse)

def distance (lat1, lat2, long1, long2) :
    lat1 = np.float64(lat1)
    lat2 = np.float64(lat2)
    lat =   lat1-lat2
    long1 = np.float64(long1)
    long2 = np.float64(long2)
    longi = long1 - long2
    lat = lat**2
    longi = longi**2
    dis = lat+longi
    distance = math.sqrt(dis)
    return distance


distance_cust = []

# From Customer to Hub
for customer in range (total_customer) :
    distance_array=[]
    min_hub=0
    for hub in range (total_hub) :
        long_cus = list_cust[customer][2]
        lat_cus = list_cust[customer][1]
        long_hub = list_hub[hub][2]
        lat_hub = list_hub[hub][1]
        distance_temp = distance(lat_cus, lat_hub, long_cus, long_hub)
        distance_array.append([distance_temp, list_hub[hub][0], list_cust[customer][0]])
    
    min_hub = min(distance_array)
    distance_cust.append(min_hub)

distance_hub = []

# From Hub to Warehouse
for hub in range (total_hub) :
    distance_array=[]
    min_hub=0
    for warehouse in range (total_warehouse) :
        long_warehouse = list_warehouse[warehouse][2]
        lat_warehouse = list_warehouse[warehouse][1]
        long_hub = list_hub[hub][2]
        lat_hub = list_hub[hub][1]
        distance_temp = distance(lat_warehouse, lat_hub, long_warehouse, long_hub)
        distance_array.append([distance_temp, list_hub[hub][0], list_warehouse[warehouse][0]])
    
    min_hub = min(distance_array)
    distance_hub.append(min_hub)

distance_hub2hub = []

# From Hub to Hub
for hub1 in range (total_hub) :
    for hub2 in range (total_hub) :
        long_hub1 = list_hub[hub1][2]
        lat_hub1 = list_hub[hub1][1]
        long_hub2 = list_hub[hub2][2]
        lat_hub2 = list_hub[hub2][1]

        distance_temp = distance(lat_hub1, lat_hub2, long_hub1, long_hub2)
        temp = [distance_temp, list_hub[hub1][0], list_hub[hub2][0]]
        distance_hub2hub.append([distance_temp, list_hub[hub1][0], list_hub[hub2][0]])

distance_h = []

for hub in range(total_hub) :
    if distance_hub[hub][1] == distance_hub[hub][2] :
        distance_h.append([[distance_hub[hub][1]], distance_hub[hub][2], distance_hub[hub][0]])
        
for hub in range (total_hub):
    for hub2 in range (len(distance_hub2hub)):
        if distance_hub[hub][1] != distance_hub[hub][2] : #nyocokin kalo hub sama warehouse beda nama

            if distance_hub[hub][1] == distance_hub2hub[hub2][1]: # nycokin start hub di list hub ke warehouse sama hub2hub
                if distance_hub[hub][2] == distance_hub2hub[hub2][2]: # nyocokin end hub sama warehouse
                    
                    for hub3 in range(total_hub) :
                        if distance_hub[hub3][2] == distance_hub2hub[hub2][2] : # nyocokin nama hub tujuan di list hub dan warehouse di list hub
                            if distance_hub[hub3][1] == distance_hub[hub3][2] : # nyocokin nama hub dan warehouse
                                distance_temp = distance_hub2hub[hub2][0] + distance_hub[hub3][0]
                                distance_h.append([[distance_hub[hub][1], distance_hub[hub][2]], distance_hub[hub3][2], distance_temp])

exist_hub=[]
for hub in  range (5):
    exist_hub.append(distance_h[hub][0][0])

for hub in range(total_hub):
    if distance_hub[hub][1] not in exist_hub:
        distance_h.append([[distance_hub[hub][1]],distance_hub[hub][2],distance_hub[hub][0]])
                

distance_total = []

#From Customer to Warehouse ..
for customer in range(len(distance_cust)) :
    for hub in range(len(distance_h)) :
        if distance_cust[customer][1] == distance_h[hub][0][0] :
            distance_temp = distance_cust[customer][0] + distance_h[hub][2]
            distance_total.append([distance_temp, distance_cust[customer][2], distance_h[hub][0], distance_h[hub][1]])

#Output
for customer in range(len(distance_total)) :
    print(
        '\nNo. : ', customer+1,
        '\nDistance : ', distance_total[customer][0],
        '\nCustomer ID : ', distance_total[customer][1],
        '\nHub : ', distance_total[customer][2],
        '\nWarehouse : ', distance_total[customer][3]
    )