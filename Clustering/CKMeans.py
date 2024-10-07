from sklearn.cluster import KMeans
from statics.Config import KM_CLUSTER_COUNT
import numpy as np



def cluster_vectors(vector_list):
    km = KMeans(n_clusters=KM_CLUSTER_COUNT, init="k-means++", n_init="auto").fit(vector_list)
    clustered = [[] for i in range(KM_CLUSTER_COUNT)]
    for j in range(len(km.labels_)):
        clustered[km.labels_[j]].append(vector_list[j])
    return clustered

def mean_of_clusters(cluster_list):
    res = []
    for i in range(len(cluster_list)):
        res.append(np.mean(cluster_list[i], 0))
    return res