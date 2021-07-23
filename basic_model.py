#The basic approach is, creating a mathematical model of a person,
#next, finding people with models similar to yours, and then what they have liked, suggestingi it should be a similar taste.
from math import sqrt

from pandas import read_csv

data = 'C:/Users/User/Desktop/song-ratings.csv'
ratings = read_csv(data,index_col=0)

#checking similar tastes through distance
#simple distance would be:
def distance(person1, person2):
    a_squared = (person1[0] - person2[0])**2
    b_squared = (person1[1] - person2[1])**2
    c = sqrt(a_squared + b_squared)
    return c
