#!/usr/bin/env python
# coding: utf-8

# In[32]:


#KMeans Clustering in Customer Segmentation
import pandas as pd
import csv
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans


# In[11]:


#list the files in the input directory
import os
print(os.listdir("C:/Users/Rabbi Amin/Desktop/DS/pythonDS/K-means"))


# In[15]:


#Import the dataset

dataset = pd.read_csv('C:/Users/Rabbi Amin/Desktop/DS/pythonDS/K-means/Mall_Customers.csv')
print(dataset)
dataset.head(15)


# In[16]:


#total rows and colums in the dataset
dataset.shape


# In[17]:


# there are no missing values as all the columns has 200 entries properly
dataset.info()


# In[18]:


#Missing values computation
dataset.isnull().sum()


# In[38]:


### Feature sleection for the model
#Considering only 2 features (Annual income and Spending Score) and no Label available
X= dataset.iloc[:, [3]].values
Y = dataset.iloc[:,[4]].values


# In[39]:


plt.scatter(X,Y)
plt.show()


# In[47]:


#zip the data as a list in two way first one is
data = list(zip(X,Y))
print(data)

#another way is
Z = dataset.iloc[:, [3,4]].values
print(Z)

wcss=[]
for i in range(1,11):
    kmeans = KMeans(n_clusters= i, init='k-means++', random_state=0)
    kmeans.fit(Z)
    wcss.append(kmeans.inertia_)


# In[48]:


#Visualizing the ELBOW method to get the optimal value of K 
plt.plot(range(1,11), wcss)
plt.title('The Elbow Method')
plt.xlabel('no of clusters')
plt.ylabel('wcss')
plt.show()


# In[49]:


#If you zoom out this curve then you will see that last elbow comes at k=5
#no matter what range we select ex- (1,21) also i will see the same behaviour but if we chose higher range it is little difficult to visualize the ELBOW
#that is why we usually prefer range (1,11)
##Finally we got that k=5

#Model Build
kmeansmodel = KMeans(n_clusters= 5, init='k-means++', random_state=0)
y_kmeans= kmeansmodel.fit_predict(X)

#For unsupervised learning we use "fit_predict()" wherein for supervised learning we use "fit_tranform()"
#y_kmeans is the final model . Now how and where we will deploy this model in production is depends on what tool we are using.
#This use case is very common and it is used in BFS industry(credit card) and retail for customer segmenattion.


# In[51]:


#Visualizing all the clusters 

plt.scatter(Z[y_kmeans == 0, 0], Z[y_kmeans == 0, 1], s = 100, c = 'red', label = 'Cluster 1')
plt.scatter(Z[y_kmeans == 1, 0], Z[y_kmeans == 1, 1], s = 100, c = 'blue', label = 'Cluster 2')
plt.scatter(Z[y_kmeans == 2, 0], Z[y_kmeans == 2, 1], s = 100, c = 'green', label = 'Cluster 3')
plt.scatter(Z[y_kmeans == 3, 0], Z[y_kmeans == 3, 1], s = 100, c = 'cyan', label = 'Cluster 4')
plt.scatter(Z[y_kmeans == 4, 0], Z[y_kmeans == 4, 1], s = 100, c = 'magenta', label = 'Cluster 5')
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s = 300, c = 'yellow', label = 'Centroids')
plt.title('Clusters of customers')
plt.xlabel('Annual Income (k$)')
plt.ylabel('Spending Score (1-100)')
plt.legend()
plt.show()


# In[ ]:




