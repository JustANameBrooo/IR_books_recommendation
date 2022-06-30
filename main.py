from numpy import NaN
import pandas as pd
import indexing

df = pd.read_csv(r'.\booklist.csv')
# arr = df.values
arr = df.values[:10]
# print(df.head(5))

col_names=['bookId','title','series','author','rating','description','lang','isbn','genres','characters','bookForm','edition','pages','publisher','publishDate','firstPublished','awards','numRating','ratingsByStars','likedPercent','setting','coverImg','bbeScore','bbeVotes','price']
wanted_cols = ['bookId','title','series','author','rating','description','genres','characters','setting','coverImg']

#TODO: filter out our wanted cols, create our index and save it to a file(?)
filtered_df = df[wanted_cols].head(5)
# print(filtered_df.head(5))

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