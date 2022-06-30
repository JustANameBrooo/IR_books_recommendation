import pandas as pd

df = pd.read_csv(r'.\booklist.csv')
# arr = df.values
arr = df.values[:10]

col_names=['bookId','title','series','author','rating','desc','lang','isbn','genres','characters','bookForm','edition','pages','publisher','publishDate','firstPublished','awards','numRating','ratingsByStars','likedPercent','setting','coverImg','bbeScore','bbeVotes','price']
wanted_cols = ['bookId','title','series','author','rating','desc','genres','characters','setting','coverImg']

#TODO: filter out our wanted cols, create our index and save it to a file(?)
#create diff files for diff methods (vsm,posindex,okapibm25?...)

#later on: create interface for this proj

print(arr)