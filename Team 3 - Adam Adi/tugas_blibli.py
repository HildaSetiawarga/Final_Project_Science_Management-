#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


customer = pd.read_csv('customer_data.csv')
hub = pd.read_csv('hub_data.csv')
hub_2 = pd.read_csv('hub2_data.csv') 
warehouse = pd.read_csv('warehouse_data.csv')


# In[3]:


cust_id = customer['id'].values
cust_long = customer['Longitude'].values
cust_lat = customer['Latitude'].values


# In[4]:


hub_name = hub['Hub'].values
hub_long = hub['Longitude'].values
hub_lat = hub['Latitude'].values
for i in range(len(hub_name)):
    print('id: ', hub_name[i], '\t', 'longitude: ', hub_long[i], '\t', 'latitude: ', hub_lat[i])


# In[5]:


hub2_name = hub_2['Hub'].values
hub2_long = hub_2['Longitude'].values
hub2_lat = hub_2['Latitude'].values
for i in range(len(hub2_name)):
    print('id: ', hub2_name[i], '\t', 'longitude: ', hub2_long[i], '\t', 'latitude: ', hub2_lat[i])


# In[6]:


whouse_name = warehouse['Warehouse'].values
whouse_long = warehouse['Longitude'].values
whouse_lat = warehouse['Latitude'].values
for i in range(len(whouse_name)):
    print('id: ', whouse_name[i], 'longitude: ', whouse_long[i], 'latitude: ', whouse_lat[i])


# In[7]:


from scipy.spatial import distance


# In[8]:


def customer_to_hub(cust_id, cust_long, cust_lat, hub_name, hub_long, hub_lat):
    A = (cust_long, cust_lat)
    B = (hub_long, hub_lat)
    return  distance.euclidean(A, B)


# In[9]:


def customer_to_warehouse(cust_id, cust_long, cust_lat, whouse_name, whouse_long, whouse_lat):
    A = (cust_long, cust_lat)
    B = (whouse_long, whouse_lat)
    return distance.euclidean(A, B)


# In[10]:


def hub_to_hub(hub_name, hub_long, hub_lat, hub2_name, hub2_long, hub2_lat):
    A = (hub_long, hub_lat)
    B = (hub2_long, hub2_lat)
    return distance.euclidean(A, B)


# In[11]:


def hub_to_warehouse(hub_id, hub_long, hub_lat, whouse_name, whouse_long, whouse_lat):
    A = (hub_long, hub_lat)
    B = (whouse_long, whouse_lat)
    return distance.euclidean(A, B)


# In[12]:


customerHub = [[ [customer_to_hub(cust_id[j], cust_long[j], cust_lat[j], hub_name[i], hub_long[i], hub_lat[i]), hub_name[i]] for i in range(6)] for j in range(30)]
#print(customerHub)


# In[13]:


for i in range(len(customerHub)):
    customerHub[i].sort(key = lambda x : x[0])
    print('customer', i+1, customerHub[i][0])


# In[14]:


customerWhouse= [[ [customer_to_warehouse(cust_id[j], cust_long[j], cust_lat[j], whouse_name[i], whouse_long[i], whouse_lat[i]), whouse_name[i]] for i in range(4)] for j in range(30)]
#print(customerWhouse)


# In[16]:


for i in range(len(customerWhouse)):
    customerWhouse[i].sort(key = lambda x : x[0])
    #print(customerWhouse[i][0])


# In[18]:


hubToHub = [[ [hub_to_hub(hub_name[j], hub_long[j], hub_lat[j], hub2_name[i], hub2_long[i], hub2_lat[i]), hub2_name[i]] for i in range(6)] for j in range(6)]
#print(hubToHub)


# In[19]:


for i in range(len(hubToHub)):
    hubToHub[i].sort(key = lambda x : x[0])
    print(hubToHub[i][1])  


# In[22]:


hubToWhouse = [[ [hub_to_warehouse(hub_name[j], hub_long[j], hub_lat[j], whouse_name[i], whouse_long[i], whouse_lat[i]), whouse_name[i]] for i in range(4)] for j in range(6)]
#print(hubToWhouse)
#print(len(hubToWhouse))


# In[23]:


for i in range(len(hubToWhouse)):
    hubToWhouse[i].sort(key = lambda x : x[0])
    print(hubToWhouse[i][0])


# In[24]:


nearestFromCustomer = []
for i in range(30):
    if customerHub[i][0] < customerWhouse[i][0]:
        nearestFromCustomer.append(customerHub[i][0])
    else:
        nearestFromCustomer.append(customerWhouse[i][0])
        
    print('customer', i+1, '->', nearestFromCustomer[i])


# In[25]:


#customer 1
customer1 = []
if hubToHub[1][1] < hubToWhouse[1][0]:
    print('error')
else: 
    customer1.append(hubToWhouse[1][0])
#print(customer1)
print('customer1 -> ', nearestFromCustomer[0], '->', customer1)
print('total cost:',nearestFromCustomer[0][0] + customer1[0][0])


# In[26]:


#customer 2
customer2 = []
if hubToHub[3][1] < hubToWhouse[3][0]:
    customer2.append(hubToHub[3][1])
    
    if hubToHub[2][1] < hubToWhouse[2][0]:
        print('error')
    else: 
        customer2.append(hubToWhouse[2][0])
#print(customer2)
print('customer2 -> ', nearestFromCustomer[1], '->', customer2)
#print(customer2[0][0])
#print(customer2[1][0])
print('total cost:',nearestFromCustomer[1][0] + customer2[0][0] + customer2[1][0])


# In[27]:


#customer 3
customer3 = []
if hubToHub[4][1] < hubToWhouse[4][0]:
    customer3.append(hubToHub[4][1])
    
    if hubToHub[1][1] < hubToWhouse[1][0]:
        print('error')
    else: 
        customer3.append(hubToWhouse[1][0])
#print(customer2)
print('customer3 -> ', nearestFromCustomer[2], '->', customer3)
#print(customer2[0][0])
#print(customer2[1][0])
print('total cost:',nearestFromCustomer[2][0] + customer3[0][0] + customer3[1][0])


# In[28]:


#customer 4
customer4 = []
if hubToHub[0][1] < hubToWhouse[0][0]:
    customer4.append(hubToHub[0][1])
    
    if hubToHub[1][1] < hubToWhouse[1][0]:
        print('error')
    else: 
        customer4.append(hubToWhouse[1][0])
#print(customer2)
print('customer4 -> ', nearestFromCustomer[3], '->', customer4)
#print(customer2[0][0])
#print(customer2[1][0])
print('total cost:',nearestFromCustomer[3][0] + customer4[0][0] + customer4[1][0])


# In[29]:


#customer 5
customer5 = []
if hubToHub[0][1] < hubToWhouse[0][0]:
    customer5.append(hubToHub[0][1])
    
    if hubToHub[1][1] < hubToWhouse[1][0]:
        print('error')
    else: 
        customer5.append(hubToWhouse[1][0])
#print(customer2)
print('customer5 -> ', nearestFromCustomer[4], '->', customer5)
#print(customer2[0][0])
#print(customer2[1][0])
print('total cost:',nearestFromCustomer[4][0] + customer5[0][0] + customer5[1][0])


# In[30]:


#customer 6
customer6 = []
if hubToHub[0][1] < hubToWhouse[0][0]:
    customer6.append(hubToHub[0][1])
    
    if hubToHub[1][1] < hubToWhouse[1][0]:
        print('error')
    else: 
        customer6.append(hubToWhouse[1][0])
#print(customer2)
print('customer6 -> ', nearestFromCustomer[5], '->', customer6)
#print(customer2[0][0])
#print(customer2[1][0])
print('total cost:',nearestFromCustomer[5][0] + customer6[0][0] + customer6[1][0])


# In[31]:


#customer 7
customer7 = []
if hubToHub[0][1] < hubToWhouse[0][0]:
    customer7.append(hubToHub[0][1])
    
    if hubToHub[1][1] < hubToWhouse[1][0]:
        print('error')
    else: 
        customer7.append(hubToWhouse[1][0])
#print(customer2)
print('customer7 -> ', nearestFromCustomer[6], '->', customer7)
#print(customer2[0][0])
#print(customer2[1][0])
print('total cost:',nearestFromCustomer[6][0] + customer7[0][0] + customer7[1][0])


# In[32]:


#customer 8
customer8 = []
#print(customerHub[7][0])
customer8.append(customerHub[7][0])
print('customer 8 -> ', customer8, '->', hubToWhouse[1][0])


# In[33]:


#customer 9
customer9 = []
#print(customerHub[7][0])
customer9.append(customerHub[8][0])
print('customer 9 -> ', customer9, '->', hubToWhouse[1][0])


# In[34]:


#customer 10
customer10 = []
if hubToHub[0][1] < hubToWhouse[0][0]:
    customer10.append(hubToHub[0][1])
    
    if hubToHub[1][1] < hubToWhouse[1][0]:
        print('error')
    else: 
        customer10.append(hubToWhouse[1][0])
#print(customer2)
print('customer10 -> ', nearestFromCustomer[9], '->', customer10)
#print(customer2[0][0])
#print(customer2[1][0])
print('total cost:',nearestFromCustomer[9][0] + customer10[0][0] + customer10[1][0])


# In[35]:


#customer 11
customer11 = []
if hubToHub[2][1] < hubToWhouse[2][0]:
    print('error')
else: 
    customer11.append(hubToWhouse[2][0])
#print(customer1)
print('customer11 -> ', nearestFromCustomer[10], '->', customer11)
print('total cost:',nearestFromCustomer[10][0] + customer11[0][0])


# In[36]:


#customer 12
customer12 = []
if hubToHub[1][1] < hubToWhouse[1][0]:
    print('error')
else: 
    customer12.append(hubToWhouse[1][0])
#print(customer1)
print('customer12 -> ', nearestFromCustomer[11], '->', customer12)
print('total cost:',nearestFromCustomer[11][0] + customer12[0][0])


# In[37]:


#customer 13
customer13 = []
if hubToHub[1][1] < hubToWhouse[1][0]:
    print('error')
else: 
    customer13.append(hubToWhouse[1][0])
#print(customer1)
print('customer13 -> ', nearestFromCustomer[12], '->', customer13)
print('total cost:',nearestFromCustomer[12][0] + customer13[0][0])


# In[38]:


#customer 14
customer14 = []
if hubToHub[0][1] < hubToWhouse[0][0]:
    customer14.append(hubToHub[0][1])
    
    if hubToHub[1][1] < hubToWhouse[1][0]:
        print('error')
    else: 
        customer14.append(hubToWhouse[1][0])
#print(customer2)
print('customer14 -> ', nearestFromCustomer[13], '->', customer14)
#print(customer2[0][0])
#print(customer2[1][0])
print('total cost:',nearestFromCustomer[13][0] + customer14[0][0] + customer14[1][0])


# In[39]:


#customer 15
customer15 = []
if hubToHub[1][1] < hubToWhouse[1][0]:
    print('error')
else: 
    customer15.append(hubToWhouse[1][0])
#print(customer1)
print('customer15 -> ', nearestFromCustomer[14], '->', customer15)
print('total cost:',nearestFromCustomer[14][0] + customer15[0][0])


# In[40]:


#customer 16
customer16 = []
if hubToHub[1][1] < hubToWhouse[1][0]:
    print('error')
else: 
    customer16.append(hubToWhouse[1][0])
#print(customer1)
print('customer16 -> ', nearestFromCustomer[15], '->', customer16)
print('total cost:',nearestFromCustomer[15][0] + customer16[0][0])


# In[41]:


#customer 17
customer17 = []
if hubToHub[1][1] < hubToWhouse[1][0]:
    print('error')
else: 
    customer17.append(hubToWhouse[1][0])
#print(customer1)
print('customer17 -> ', nearestFromCustomer[16], '->', customer17)
print('total cost:',nearestFromCustomer[16][0] + customer17[0][0])


# In[42]:


#customer 18
customer18 = []
if hubToHub[0][1] < hubToWhouse[0][0]:
    customer18.append(hubToHub[0][1])
    
    if hubToHub[1][1] < hubToWhouse[1][0]:
        print('error')
    else: 
        customer18.append(hubToWhouse[1][0])
#print(customer2)
print('customer18 -> ', customerHub[17][0], '->', customer18)
#print(customer2[0][0])
#print(customer2[1][0])
print('total cost:', customerHub[17][0][0] + customer18[0][0] + customer18[1][0])


# In[43]:


#customer 19
customer19 = []
if hubToHub[0][1] < hubToWhouse[0][0]:
    customer19.append(hubToHub[0][1])
    
    if hubToHub[1][1] < hubToWhouse[1][0]:
        print('error')
    else: 
        customer19.append(hubToWhouse[1][0])
#print(customer2)
print('customer19 -> ', nearestFromCustomer[18], '->', customer19)
#print(customer2[0][0])
#print(customer2[1][0])
print('total cost:',nearestFromCustomer[18][0] + customer19[0][0] + customer19[1][0])


# In[44]:


#customer 20
customer20 = []
if hubToHub[0][1] < hubToWhouse[0][0]:
    customer20.append(hubToHub[0][1])
    
    if hubToHub[1][1] < hubToWhouse[1][0]:
        print('error')
    else: 
        customer20.append(hubToWhouse[1][0])
#print(customer2)
print('customer20 -> ', nearestFromCustomer[19], '->', customer20)
#print(customer2[0][0])
#print(customer2[1][0])
print('total cost:',nearestFromCustomer[19][0] + customer20[0][0] + customer20[1][0])


# In[45]:


#customer 21
customer21 = []
if hubToHub[0][1] < hubToWhouse[0][0]:
    customer21.append(hubToHub[0][1])
    
    if hubToHub[1][1] < hubToWhouse[1][0]:
        print('error')
    else: 
        customer21.append(hubToWhouse[1][0])
#print(customer2)
print('customer21 -> ', nearestFromCustomer[20], '->', customer21)
#print(customer2[0][0])
#print(customer2[1][0])
print('total cost:',nearestFromCustomer[20][0] + customer21[0][0] + customer21[1][0])


# In[46]:


#customer 22
customer22 = []
if hubToHub[2][1] < hubToWhouse[2][0]:
    print('error')
else: 
    customer22.append(hubToWhouse[2][0])
#print(customer1)
print('customer22 -> ', nearestFromCustomer[21], '->', customer22)
print('total cost:',nearestFromCustomer[21][0] + customer22[0][0])


# In[47]:


#customer 23
customer23 = []
if hubToHub[0][1] < hubToWhouse[0][0]:
    customer23.append(hubToHub[0][1])
    
    if hubToHub[1][1] < hubToWhouse[1][0]:
        print('error')
    else: 
        customer23.append(hubToWhouse[1][0])
#print(customer2)
print('customer23 -> ', nearestFromCustomer[22], '->', customer23)
#print(customer2[0][0])
#print(customer2[1][0])
print('total cost:',nearestFromCustomer[22][0] + customer23[0][0] + customer23[1][0])


# In[48]:


#customer 24
customer24 = []
if hubToHub[4][1] < hubToWhouse[4][0]:
    customer24.append(hubToHub[4][1])
    
    if hubToHub[1][1] < hubToWhouse[1][0]:
        print('error')
    else: 
        customer24.append(hubToWhouse[1][0])
#print(customer2)
print('customer24 -> ', nearestFromCustomer[23], '->', customer24)
#print(customer2[0][0])
#print(customer2[1][0])
print('total cost:',nearestFromCustomer[23][0] + customer24[0][0] + customer24[1][0])


# In[49]:


#customer 25
customer25 = []
if hubToHub[1][1] < hubToWhouse[1][0]:
    print('error')
else: 
    customer25.append(hubToWhouse[1][0])
#print(customer1)
print('customer25 -> ', nearestFromCustomer[24], '->', customer25)
print('total cost:',nearestFromCustomer[24][0] + customer25[0][0])


# In[50]:


#customer 26
customer26 = []
if hubToHub[1][1] < hubToWhouse[1][0]:
    print('error')
else: 
    customer26.append(hubToWhouse[1][0])
#print(customer1)
print('customer26 -> ', nearestFromCustomer[25], '->', customer26)
print('total cost:',nearestFromCustomer[25][0] + customer26[0][0])


# In[51]:


#customer 27
customer27 = []
if hubToHub[1][1] < hubToWhouse[1][0]:
    print('error')
else: 
    customer27.append(hubToWhouse[1][0])
#print(customer1)
print('customer27 -> ', nearestFromCustomer[26], '->', customer27)
print('total cost:',nearestFromCustomer[26][0] + customer27[0][0])


# In[52]:


#customer 28
customer28 = []
if hubToHub[5][1] < hubToWhouse[5][0]:
    print('error')
else: 
    customer28.append(hubToWhouse[5][0])
#print(customer1)
print('customer28 -> ', nearestFromCustomer[27], '->', customer28)
print('total cost:',nearestFromCustomer[27][0] + customer28[0][0])


# In[53]:


#customer 29
customer29 = []
if hubToHub[0][1] < hubToWhouse[0][0]:
    customer29.append(hubToHub[0][1])
    
    if hubToHub[1][1] < hubToWhouse[1][0]:
        print('error')
    else: 
        customer29.append(hubToWhouse[1][0])
#print(customer2)
print('customer29 -> ', customerHub[28][0], '->', customer29)
#print(customer2[0][0])
#print(customer2[1][0])
print('total cost:', customerHub[28][0][0] + customer29[0][0] + customer29[1][0])


# In[54]:


#customer 30
customer30 = []
if hubToHub[0][1] < hubToWhouse[0][0]:
    customer30.append(hubToHub[0][1])
    
    if hubToHub[1][1] < hubToWhouse[1][0]:
        print('error')
    else: 
        customer30.append(hubToWhouse[1][0])
#print(customer2)
print('customer30 -> ', customerHub[29][0], '->', customer30)
#print(customer2[0][0])
#print(customer2[1][0])
print('total cost:', customerHub[29][0][0] + customer30[0][0] + customer30[1][0])

