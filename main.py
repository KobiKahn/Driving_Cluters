import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import math

# FUNCTIONS
def guess_centroid(list1, list2):
    plt.scatter(list1, list2)
    plt.show()
    guess = input('Input Centroid Locations: ')
    guess = eval(guess)  # if written as coordinate points gives tuple or tuple of tuples
    return list(guess)

def calc_dist(p1, p2):
    return(abs(math.sqrt( (p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)))


def assign_cluster(centroid_list, x_list, y_list):
    cluster_dict = {0:[], 1:[], 2:[], 3:[]}
    for i in range(len(x_list)):
        point = (x_list[i], y_list[i])
        dist_list = []
        for centroid in centroid_list:
            dist_list.append(calc_dist(point, centroid))
        i2 = -1
        for entry in dist_list:
            i2 += 1
            if entry == min(dist_list):
                cluster_dict[i2] = point
    print(cluster_dict)








# Create and change column names in Dataframe
driver_df = pd.read_csv('data.txt', delim_whitespace=True)
driver_df.columns = ['id', 'dist', 'speed']

# CREATE RAW LISTS
dist_list = driver_df['dist'].values.tolist()
speed_list = driver_df['speed'].values.tolist()

# CREATE NORMAL COLUMNS
driver_df['norm dist'] = (driver_df.dist - driver_df.dist.mean())/driver_df.dist.std()
driver_df['norm speed'] = (driver_df.speed - driver_df.speed.mean())/driver_df.speed.std()

# CREATE NORMAL LISTS
normdist_list = driver_df['norm dist'].values.tolist()
normspeed_list = driver_df['norm speed'].values.tolist()

# print(normdist_list, normspeed_list)

# (-.5, .5), (-.5, 1.5), (2, 0), (2,4)
assign_cluster(guess_centroid(normdist_list, normspeed_list), normdist_list, normspeed_list)


