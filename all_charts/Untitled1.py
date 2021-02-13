
# coding: utf-8

# In[ ]:


from geopy.geocoders import Nominatim


# In[ ]:


geolocator = Nominatim(user_agent="data_lake_lab")


# In[ ]:


location = geolocator.geocode('Andorra','Antigua')
print((location.address ,location.latitude, location.longitude))


# In[ ]:


from geopy.geocoders import Nominatim


import pandas as pd
geolocator = Nominatim(user_agent="data_lake_lab")
df = pd.read_csv('/home/subir/anaconda3/notebook/corona/all_country.csv')
df=df.head()
print()
list_of_addresses = [df]
for address in list_of_addresses:
    try:
        search = geolocator.geocode(address)
    except ValueError:
        continue
    first_result = search[0]
    output =  [flocation.latitude, location.longitude]
    print (output)


# In[1]:


import pandas as pd
df = pd.DataFrame({'name': ['paris', 'berlin', 'london']})

from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="specify_your_app_name_here")

from geopy.extra.rate_limiter import RateLimiter
geocode = RateLimiter(geolocator.geocode, min_delay_seconds=1)
df['location'] = df['name'].apply(geocode)

df['point'] = df['location'].apply(lambda loc: tuple(loc.point) if loc else None)


# In[10]:


import csv
##from time import sleep

from geopy.geocoders import Nominatim
with open('/home/subir/anaconda3/notebook/corona/all_country.csv', 'r') as fp:
    with open('/home/subir/anaconda3/notebook/corona/all_country.csv', 'w',newline='') as op:
        a = csv.writer(op)
        a.writerow(["Town","District","State","Country","Address","Latitude","Longitude"])
        for line in fp.readlines():
            geolocator = Nominatim()
            Country = line.split(',')[0]
            address_new = line.split(',')[4]
            location = geolocator.geocode(address_new)
            lat=location.latitude
            lon=location.longitude
                ##time.sleep(3)
            a.writerow([town_new,district_new,state_new,country_new,address_new,lat,lon])


# In[13]:


with open('/home/subir/anaconda3/notebook/corona/all_country.csv', 'w',newline='') as op:
       a = csv.writer(op)
       a.writerow(["Country","Latitude","Longitude"])
       for line in fp.readlines():
           geolocator = Nominatim()
           town_new = line.split(',')[0]
           district_new = line.split(',')[1]
           state_new = line.split(',')[2]
           country_new = line.split(',')[3]
           address_new = line.split(',')[4]
           location = geolocator.geocode(address_new)
           ''' This will check if your given address has any latitude or longitude and if true then lat and lon will be assigned otherwise, both lat and lon will be 0. '''
           if location:
               lat=location.latitude
               lon=location.longitude
               ##time.sleep(3)
           else:
               lat = 0
               lon = 0

