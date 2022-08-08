import numpy as np
import pandas as pd
from ast import literal_eval
from math import log2

df = pd.read_csv(r'.\small_eval.csv', index_col=False)
df['recommended'] = df['recommended'].apply(literal_eval)

def precisionatk(r,k=20): # precision is relevant&retrieved/retrieved
    assert k >= 1
    r = np.asarray(r)[:k] != 0
    if r.size != k:
        raise ValueError('Relevance score length < k')
    return np.mean(r)

def average_precision(r):
    totalp=0.0
    count = 0.0
    for i in range(len(r)):
        if r[i] == 1:
            totalp+=precisionatk(r,i+1)
            count+=1.0
    if count==0.0: return 0.0
    avg_p = totalp/count
    return avg_p

def mean_average_precision(rs):
    totalp = 0.0
    for r in rs:
        totalp+= average_precision(r)
    m_avg_p = totalp/len(rs)

    return m_avg_p

def dcg_at_k(r, k, method=0):
    dcg = 0.0
    for i in range(k):
        if i==0:
            dcg += r[i]
        elif i>=len(r):
            return dcg
        elif r[i] != 0:
            dcg += r[i]/log2(i+1)

    return dcg

def ndcg_at_k(r, k=20, method=0):
    if len(r) ==1:
        return r[0]
    sorted_r = sorted(r,reverse=True)
    # print(sorted_r)
    ndcg = []
    for i in range(len(sorted_r)):
        dcg = dcg_at_k(r,i+1)
        idcg= dcg_at_k(sorted_r,i+1)
        if (idcg ==0):
            return 0
        ndcg.append(dcg/idcg)
    # print(ndcg)
    
    return ndcg[k-1]

