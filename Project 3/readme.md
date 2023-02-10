## Project 3: Clustering FIFA 22 players

This project was designed to implement **k-means** clustering algorithm, an unsupervised machine learning technique, with all FIFA 22 players in order to find patterns in our data and analyze some results. The notebook for this project is available here.

* Dataset used can be downloaded here.
* K-Means clustering algorithm was built from scratch, and later compared with sci-kitlearn.

### Data Overview

The dataset comes with several columns, including club logo from each player, nation flag, etc. For this task I worked only with the columns or features listed below.

`overall` - players rating 

`potential` - potential player rating

`value_eur` - how much the player is valued in euros

`wage_eur` - how much is the player salary in euros

`age` - player age

![](images/data.png)

### Data Visualization

Here are some plots of our dataset. First of all, I plotted the age distribution between all players contained in the dataset. Secondly, I plotted the players overall distribution.

![](images/age.png)

From the plot above we see a positive skewness, that is, the mass of the distribution is concentrated on the left.

![](images/ovr.png)

For the overall distribution, we see a gaussian curve.

### Scaling the data

From the initial data, we see that our columns have lots of different orders of magnitude and I would like to treat each column
equally. For this purpose, I scalled the columns to have values between 1-10, with 10 being the maximun value for each column and 1 beign the minimum value for each column.

![](images/data_scaled.png)

### K-Means algorithm implementation

Now that the data is scaled, I implemented the k-means algorithm. First I generated a random centroid. The centroid is the data point that is in the center of the cluster. For this project I choosed three centroids. Here is a table containing the centroids features values.

![](images/centroids.png)

Now, with respect to each centroid the euclidean distance between every data point was calculated. For each data point, it was assigned cluster labels (0, 1 or 2) according to the minimum distance to the centroids. The centroids are updated based on who is on the cluster, by calculating the geometric mean of each feature.

In order to plot the clusters, I used the PCA (Principal Component Analysis) to help visualize them, since our features dimension is 5. I used 100 iterations for the centroid update. The algorithm stops if the number of iterations reach the choosed value (100) or if the centroids converge and stop updating. Here is the clustering plot of the data.

![](images/clustering.png)

From the plot above, we see that it took 33 iterations to converge.
