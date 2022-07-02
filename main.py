from numpy import NaN
import pandas as pd
import indexing
import os, glob, re, sys, random, unicodedata, collections
import re
from nltk.tokenize import sent_tokenize , word_tokenize
from nltk.corpus import stopwords

df = pd.read_csv(r'.\booklist.csv')
# arr = df.values
arr = df.values[:10]
# print(df.head(5))

col_names=['bookId','title','series','author','rating','description','lang','isbn','genres','characters','bookForm','edition','pages','publisher','publishDate','firstPublished','awards','numRating','ratingsByStars','likedPercent','setting','coverImg','bbeScore','bbeVotes','price']
wanted_cols = ['bookId','title','series','author','rating','description','genres','characters','setting','coverImg']

#TODO: filter out our wanted cols, create our index and save it to a file(?)
filtered_df = df[wanted_cols].head(5)
# print(filtered_df.head(5))

WORD_MIN_LENGTH = 2
STOP_WORDS = stopwords.words('english')

def tokenize_text(text):
    # Strip accents/punctuations
    nfkd = unicodedata.normalize('NFKD', text)
    text = u"".join([c for c in nfkd if not unicodedata.combining(c)])
    text=  re.sub('[^a-zA-Z0-9\d\'\s \\\']', '', text) 

    # tokenize, lowercase/remove newlines, remove stop words and words with less than 2 chars.
    words = text.lower().split()
    text = re.sub(re.compile('\n'),' ',text)
    words = word_tokenize(text)
    words = [word.lower() for word in words]
    words = [word for word in words if word not in STOP_WORDS and len(word) >= WORD_MIN_LENGTH]
    return words


def clean_lists(w):
    return len(w)>2

def clean_col(col):
    print(col.name)
    if (col.name in ["characters","genres","setting"]):
        col = col.str.strip("[]")
        col = col.str.split(",")

    elif(col.name in ["title","description","series"]):
        col = col.str.split()

    elif(col.name is "author"):
        col = col.str.split(",")
    
    print(col)
    return col
    

filtered_df = filtered_df.apply(clean_col)
print(filtered_df)















# for i in list(range(5)):
#     print(i)
#     print(filtered_df.iloc[i])
#     people = filtered_df.iloc[i]["characters"].split("'")
#     people = list(filter(clean_lists,people))
#     people.append(filtered_df.iloc[i]["author"])
#     print(people)

#     content= filtered_df.iloc[i]["genres"].split("'")
#     content = list(filter(clean_lists,content))
#     title = filtered_df.iloc[i]["title"].split()
#     content += title 
#     if (filtered_df.iloc[i]["series"] is not NaN):
#         series = filtered_df.iloc[i]["series"].split()
#         content += series
#     desc = filtered_df.iloc[i]["description"].split()
#     content += desc
#     setting = filtered_df.iloc[i]["setting"].split("'")
#     setting = list(filter(clean_lists,setting))
#     content += setting
#     print(content)
    


# indexing.create_pos_index(filtered_df.head(5))

#create diff files for diff methods (vsm,posindex,okapibm25?...)

#later on: create interface for this proj

# print(arr)