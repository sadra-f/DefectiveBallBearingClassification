from scipy.spatial import distance



def dist(vec1, vec2):
    return distance.euclidean(vec1, vec2)


def cosine_sim(vec1, vec2):
    return 1 - distance.cosine(vec1, vec2)


def normalize(lst):
    min = min(lst)
    max = max(lst)
    for i in range(lst):
        lst[i] = ((lst[i] - min)/(max - min))
    return lst