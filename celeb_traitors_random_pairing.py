import pandas as pd
from random import shuffle

# read a list of the celebrity traitors into a dataframe
traitors_df = pd.read_csv(r'C:\Data\Andrew\celeb_traitors\celeb_traitors.csv')

# extract the traitor name as a list
names = traitors_df['traitor'].tolist()
# shuffle the names so order is random
shuffle(names)

# create a list of friends ['Andy', 'Catherine', 'Elodie'...] that matches length of traitors (19)
friends = ['Elodie', 'Abi', 'Jess', 'Charlie', 'Theo', 'Sue', 'Evie', 'G', 'Phil', 'Louise', 'Alfie', 'Tom', 'Daisy', 'Hetty', 'Wilfred', 'Chris', 'Emma', 'Zoe', 'Iris'] # place holder just numbers at present
print(len(friends))
# shuffle the friends so order is random
shuffle(friends)

# create the pairings with zip
pairings = zip(friends, names)
# iterate over zip object as its a generator (could be converted to list)
for pair in pairings:
    print(pair)