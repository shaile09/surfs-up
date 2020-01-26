# Surfs-up

In this module, we spent time with SQLite, SQLAlchemy, and Flask to build our knowledge of SQL database structures and quering methods. In addition, we explained the structures, interactions, and types of data of a provided dataset, differentiated between SQLite and PostgreSQL databases, used SQLAlchemy to connect to and query a SQLite database, used statistics to analyze data and design a Flask application using data. We began by importing our dependencies and used SQLAlchemy to help us easily connect to our database where we stored the weather data. Using SQLAlchemy, we created a function to set up the ablility to query a SQLite database, used SQLAlchemy automap to create a base class for an automap schema in SQLAlchemy. 

For our analysis, we calculated the date one year from Auguest 23, 3017, and found the amount of precipitation score.Then we saved our results in a DataFrame to help us analyze our data more quickly, printed the data with/without index, and plotted the data. Lastly, using the describe() method we were able to generate the summary of statitics (mean, variance, standard deviation, min, max, percentiles and count. Using the SQLite, we were able to find the number of stations and determined the most active stations. In addiion, using the session.query() we found the low, high, and average temperatues. With this information, we plotted the tempretures with the highest number of observation. Looking at the polt we can infer that a vast majority of the observations were over 67 degrees. If you count up the bins to the right of 67 degrees, you will get about 325 days where it was over 67 degrees when the temperature was observed.

Picture 

# Challenge 
In this challenge, we found a key aspects of Oahu's seasonal weather data. The investors want to ensure we have hit all of the key points before opening the surf shop. Coming from the mainland, the variable weather can be in the summer and winter and our investors want to ensure that there are enough customers between seasons to sustain the business throughout the year. The goal of this challenge is to determine the key statistical data about the month of June and December, compare the findings between the month of June and December.

We began this challenge by adding our dependents (from sqlalchemy import extract). We used the session.query to find the date, preciptation, and tempreture for June and December. We then created a DataFrame and printed the index for June and December.

For June, the average tempreture was 74.94, std was 3.25, min was 64 and max was 85. The mean precipitation was 0.13, std was 0.335, min was 0 and max was 4.43. 

For December, the average tempreture was 71.04, std was 3.74, min was 56 and max was 83. The mean precipitation was 0.21, std was 0.54, min was 0 and max was 6.42. 
