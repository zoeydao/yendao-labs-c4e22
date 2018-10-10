from pymongo import MongoClient

uri = "mongodb://admin:admin@ds021182.mlab.com:21182/c4e"

#Connect to database
client = MongoClient(uri)
db = client.get_default_database()

#Collection
customers = db['customers'] #insert_one (C), find (R)

customers_list = customers.find()

#Count number of customers by ref group
from collections import Counter
customer_ref = []

for p in customers_list:
    customer_ref.append(p["ref"])

customer_groups = Counter(customer_ref)

#Pie chart
import matplotlib.pyplot as plt

#Prepare data:
sizes = customer_groups.values()
#Prepare labels:
groups = customer_groups.keys()

#Draw pie chart
plt.pie(sizes, labels=groups, autopct='%1.1f%%',startangle=90)
plt.axis('equal')
plt.title('Number of customers by groups of reference')
plt.show()