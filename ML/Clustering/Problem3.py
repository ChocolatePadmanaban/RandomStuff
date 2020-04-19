import numpy as np 
import pandas as pd

def Clustring(x_list,z_list):
    Cluster_dist = np.array([[np.linalg.norm(x-z, ord=1) for z in z_list] for x in x_list])
    Cluster_belong = np.argmin(Cluster_dist, axis=1)
    Clusters_dic = {i:[] for i in range(len(z_list)) }
    for i in range(len(Cluster_belong)):
        Clusters_dic[Cluster_belong[i]].append(x_list[i])
    return Clusters_dic

def KMedoids(x_list,z_list,Clusters_dic):
    for i in range(len(z_list)):
        Cluster_mem = np.array(Clusters_dic[i])
        Cost_Mat = np.array([sum([np.linalg.norm(mem1-x, ord=1) for mem1 in Cluster_mem]) for x in x_list])
        z_list[i]= x_list[np.argmin(Cost_Mat)]
    return z_list

def Kmean(x_list,z_list,Clusters_dic):
    for i in range(len(z_list)):
        Cluster_mem = np.array(Clusters_dic[i])
        z_list[i]= np.sum(Cluster_mem, axis=0)/len(Cluster_mem)
    return z_list

if __name__ == "__main__":
    x_list = np.array([[0,-6],[4,4],[0,0],[-5,2]])
    z_list = np.array([[-5,2],[0,-6]], dtype=float)
    Cluster_dic=Clustring(x_list,z_list)
    
    
    print("Cluster_dic      ", Cluster_dic)
    print(Kmean(x_list,z_list,Cluster_dic))