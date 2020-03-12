import math

def ndistance(a, b):
    """Returns the distance between two n-dimensional vectors"""
    total = 0
    for i in range(len(a)):
        diff = b[i] - a[i]
        total += diff **2
    return math.sqrt(total)

def findnearest(vecs, centroids):
    """Returns the nearest vector among a list of n-dimensional vectors"""
    
    vecs= [list(v[1]) for v in vecs]
    centroids = [list(c[1]) for c in centroids]
    clusters = [[] for c in centroids]
    for j,v in enumerate(vecs):
        closestDist = float("inf")
        closestIndex = 0
        for i,c in enumerate(centroids):
            dist = ndistance(v,c)
            if dist < closestDist : 
                closestDist = dist
                closestIndex = i
                
        clusters[closestIndex].append((j,v))
    clusters = [x for x in clusters if x != []]
    return clusters

def avgvecs(veclist):
    """Returns the avarage vector of a list of n-dimensional vectors"""
    
    veclist = [v[1] for v in veclist]
    trans = map(list, zip(*veclist))
    avgvec = []
    for i in range(len(trans)):
        avgvec.append( sum(trans[i]) / len(trans[i]))
    return (-1,avgvec)