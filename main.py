import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import math
import statistics as stats

# FUNCTIONS
def guess_centroid(list1, list2):
    plt.scatter(list1, list2)
    plt.show()
    guess = input('Input Centroid Locations: ')
    guess = eval(guess)  # if written as coordinate points gives tuple or tuple of tuples
    return list(guess)

def calc_dist(p1, p2):
    return(abs(math.sqrt( (p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)))


def assign_cluster(x_list, y_list, centroid_list = None):
    if centroid_list is None:
        centroid_list = guess_centroid(x_list, y_list)

    # MAKE CLUSTER DICT FOR ANY LENGTH
    cluster_dict = {}
    for val in range(len(centroid_list)):
        cluster_dict[val] = []

    # FIND DISTANCE AND CALCULATE WHERE EACH CENTROID IS AND ASSIGN EVERY POINT TO KEY IN DICT
    for i in range(len(x_list)):
        point = (x_list[i], y_list[i])
        dist_list = []
        for centroid in centroid_list:
            dist_list.append(calc_dist(point, centroid))
        i2 = -1
        for entry in dist_list:
            i2 += 1
            if entry == min(dist_list):
                cluster_dict[i2].append([point[0], point[1]])
    return cluster_dict


def plot_centroids(dict, centroids = None):
    for key in dict:
        x_list = []
        y_list = []
        for val in dict[key]:
            x_list.append(val[0])
            y_list.append(val[1])
        plt.scatter(x_list, y_list)
    if centroids != None:
        for point in centroids:
            print(point)
            plt.plot([point[0]], [point[1]], 'k', marker='D')
    plt.show()


def calc_centroid(dict):
    centroid_coord = []
    for key in dict:
        x_list = []
        y_list = []
        for val in dict[key]:
            x_list.append(val[0])
            y_list.append(val[1])
        centroid_coord.append([stats.mean(x_list), stats.mean(y_list)])
    return(centroid_coord)



#############################################################################
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


# (-.5, .5), (-.5, 1.5), (2, 0), (2,4), (1, 3)
def main(rep):
    cluster_dict = assign_cluster(normdist_list, normspeed_list, guess_centroid(normdist_list, normspeed_list))
    cent_coord = calc_centroid(cluster_dict)
    plot_centroids(cluster_dict, cent_coord)
    for i in range(rep):
        cluster_dict = assign_cluster(normdist_list, normspeed_list, cent_coord)
        cent_coord = calc_centroid(cluster_dict)
        plot_centroids(cluster_dict, cent_coord)

main(4)

