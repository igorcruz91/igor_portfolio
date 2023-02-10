## Project 3: Clustering FIFA 22 players

This project was designed to implement **k-means** clustering algorithm, an unsupervised machine learning technique, with all FIFA 22 players in order to find patterns in our data and analyze some results. The notebook for this project is available here.

* Dataset used can be downloaded here.
* K-Means clustering algorithm was built from scratch, and later compared with sci-kitlearn.

### Data Overview

The dataset comes with several columns, including club logo from each player, nation flag, etc. For this task I worked only with the columns listed below.

`overall` - players rating 

`potential` - potential player rating

`value_eur` - how much the player is valued in euros

`wage_eur` - how much is the player salary in euros

`age` - player age

(imagem do dtaframe)

### Data Visualization

Here are some plots of our dataset. First of all, I plotted the age distribution between all players contained in the dataset. Secondly, I plotted the players overall distribution.

(imagem distrib idade)
From the plot above we see a positive skewness, that is, the mass of the distribution is concentrated on the left.

(imagem distr. overall)
For the overall distribution, we see a gaussian curve.

