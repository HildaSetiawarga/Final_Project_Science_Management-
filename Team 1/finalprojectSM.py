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
#print(list_cust)


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
#print(list_hub)


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
#print(list_warehouse)


def distance (lat1, lat2, long1, long2) :
    lat1 = np.float64(lat1)
    lat2 = np.float64(lat2)
    lat =   lat1-lat2
    long1 = np.float64(long1)
    long2 = np.float64(long2)
    longi = long1 - long2
    lat = lat**2
    longi = longi**2
    #print(lat,longi)
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
        #print(distance_temp , sep='\n')
    
        distance_array.append([distance_temp, list_hub[hub][0], list_cust[customer][0]])
    
    min_hub = min(distance_array)
    distance_cust.append(min_hub)

    #print(distance_cust)

#pprint.pprint(distance_cust)
#print('\n\n')

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
        #print(distance_temp , sep='\n')
    
        distance_array.append([distance_temp, list_hub[hub][0], list_warehouse[warehouse][0]])
    
    min_hub = min(distance_array)
    distance_hub.append(min_hub)

    #print(distance_hub)

#pprint.pprint(distance_hub)
#print('\n\n')

print(distance_hub[0])

distance_total = []

# From Customer to Warehouse ..
for customer in range(len(distance_cust)) :
    #hub1 = distance_cust[customer][1]

    for hub in range(len(distance_hub)) :

        #hub2 = distance_hub[hub][1]
        if distance_cust[customer][1] == distance_hub[hub][1] :
            distance_temp = distance_cust[customer][0] + distance_hub[hub][0]
            distance_total.append([distance_temp, distance_cust[customer][2], distance_hub[hub][1], distance_hub[hub][2]])
    
#pprint.pprint(distance_total)


for customer in range(len(distance_total)) :
    print(
        '\nNo. : ', customer,
        '\nDistance : ', distance_total[customer][0],
        'Customer ID : ', distance_total[customer][1],
        'Hub : ', distance_total[customer][2],
        'Warehouse : ', distance_total[customer][3]
    )

angke = 0
cawang = 0
cakung = 0
bekasi = 0
bogor = 0
karawaci = 0

for customer in range(len(distance_total)):
    if (distance_total[customer][2]) == "Angke" :
        angke +=1
    elif (distance_total[customer][2]) == "Cawang" :
        cawang +=1
    elif (distance_total[customer][2]) == "Cakung" :
        cakung +=1
    elif (distance_total[customer][2]) == "Bekasi" :
        bekasi +=1
    elif (distance_total[customer][2]) == "Bogor Citereup" :
        bogor +=1
    elif (distance_total[customer][2]) == "Karawaci" :
        karawaci +=1

print("\n")
print("======================================================================")
print("Hub Angke have ", angke, " items")
print("Hub Cawang have ", cawang, " items")
print("Hub Cakung have ", cakung, " items")
print("Hub Bekasi have ", bekasi, " items")
print("Hub Bogor have ", bogor, " items")
print("Hub Karawaci have ", karawaci, " items")

print("Total items in hub = ", angke+cawang+cakung+bekasi+bogor+karawaci)
print("======================================================================")

warecawang = 0
warecakung = 0
wareceper = 0
warekara = 0

for customer in range(len(distance_total)):
    if (distance_total[customer][3]) == "Cawang" :
        warecawang +=1
    elif (distance_total[customer][3]) == "Cakung" :
        warecakung +=1
    elif (distance_total[customer][3]) == "Ceper" :
        wareceper +=1
    elif (distance_total[customer][3]) == "Karawaci" :
        warekara +=1

print("Warehouse Cawang have ", warecawang, " items")
print("Warehouse Cakung have ", warecakung, " items")
print("Warehouse Ceper have ", wareceper, " items")
print("Warehouse Karawaci have ", warekara, " items")
print("Total items in warehouse = ", warecakung+warecawang+wareceper+warekara)
'''
ft. ko anjer
terimakasih
'''
            





        



    




