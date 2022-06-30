import numpy as np
import re

idIndex = 0
contentIndex = [1,2,3,5,6,7,8]

termdoci = {}

def processrow(a):
    id=a[idIndex]
    content = a[contentIndex]
    print(content)

    for c in content:
        print(type(c))
        # if (type(c) == str):
        #     tokens = c.split()
        # else:

    # tokens = content.split()
    # for tokenidx in range(len(tokens)):
    #     token = re.sub(r'[^\w\s]','',tokens[tokenidx])
    #     if not token.isalnum():
    #         continue
    #     if token not in termdoci.keys():
    #         termdoci[token]={}
    #     if id in termdoci[token].keys():
    #         termdoci[token][id].append(tokenidx)
    #     else:
    #         termdoci[token][id]=[tokenidx]


def create_pos_index(df):
    arr = df.values
    np.apply_along_axis(processrow,1,arr)
    return termdoci

def create_inverted_index(df):

    return