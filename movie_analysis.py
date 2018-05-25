#importing libraries
import numpy as np
import pandas as pd


#importing datasets
movie_column = ['movie_id', 'title', 'genres']
movies = pd.read_csv('movies.dat', sep = '::', names = movie_column, usecols=range(3), engine='python')

rating_column = ['user_id', 'movie_id', 'rating', 'timestamp']
ratings = pd.read_csv('ratings.dat', sep = '::', names = rating_column, usecols=range(4), engine='python')

user_column = ['user_id', 'gender', 'age', 'occupation', 'zip']
users = pd.read_csv('users.dat', sep='::', names=user_column,  usecols=range(5), engine = 'python')


#merging data as per requirements
movie_ratings = pd.merge(movies, ratings)
overall_data = pd.merge(movie_ratings, users) #merging user with the movie_rating


#Top ten most viewed movies with their movies Name (Ascending or Descending order)
movie_count = pd.DataFrame(overall_data.groupby(['movie_id', 'title']).size())
movie_count['count'] = movie_count
del movie_count[0]
movie_count = movie_count.sort_values('count', ascending = False)
movie_count.head(10).to_csv('top_ten_most_viewed_movies.csv')


#Top twenty rated movies (Condition: The movie should be rated/viewed by at least 40 users) 
movie_stats = overall_data.groupby('title').agg({'rating': [np.size, np.mean]})
atleast_40 = movie_stats['rating']['size'] >= 40
movie_stats[atleast_40].sort_values([('rating', 'mean')], ascending=False)[:20].to_csv('top_twenty_most_rated_movies_byatleast_fortyuser.csv')


# genres ranked by Average Rating, for each profession and age group. The age groups to be considered are: 18-35, 36-50 and 50+.
labels = ['18-35', '36-50', '50+']
overall_data['Age group'] = pd.cut(overall_data.age, range(18, 81, 18), right=False, labels=labels)
overall_data[['age', 'Age group']]

genre_stats = pd.DataFrame(overall_data.groupby(['occupation', 'Age group', 'genres', 'rating']).size())
genre_stats['count'] = genre_stats
del genre_stats[0]

genre_stats.reset_index(level = ['occupation', 'Age group', 'genres', 'rating'], inplace = True)
genre_stats.rating = genre_stats.rating.astype(str)
genre_stats123 = pd.pivot_table(genre_stats, values='genres', index = ['occupation', 'Age group'], columns='count', aggfunc = 'max')

stats = genre_stats123[[1, 2, 3, 4, 5]]
stats.sort_index(axis = 1, ascending = False, inplace = True)
stats.rename(columns = {1:'Rank5', 2:'Rank 4', 3:'Rank3', 4:'Rank 2', 5:'Rank 1'}, inplace = True)
stats.reset_index(level = ['occupation', 'Age group'], inplace = True)

stats['occupation'][0] = 'other'
stats['occupation'][1] = 'other'
stats['occupation'][2] = 'other'
stats['occupation'][3] = 'academic/educator'
stats['occupation'][4] = 'academic/educator'
stats['occupation'][5] = 'academic/educator'
stats['occupation'][6] = 'artist'
stats['occupation'][7] = 'artist'
stats['occupation'][8] = 'artist'
stats['occupation'][9] = 'clerical/admin'
stats['occupation'][10] = 'clerical/admin'
stats['occupation'][11] = 'clerical/admin'
stats['occupation'][12] = 'college/grad student'
stats['occupation'][13] = 'college/grad student'
stats['occupation'][14] = 'college/grad student'
stats['occupation'][15] = 'customer service'
stats['occupation'][16] = 'customer service'
stats['occupation'][17] = 'customer service'
stats['occupation'][18] = 'doctor/health care'
stats['occupation'][19] = 'doctor/health care'
stats['occupation'][20] = 'doctor/health care'
stats['occupation'][21] = 'executive/managerial'
stats['occupation'][22] = 'executive/managerial'
stats['occupation'][23] = 'executive/managerial'
stats['occupation'][24] = 'farmer'
stats['occupation'][25] = 'farmer'
stats['occupation'][26] = 'farmer'
stats['occupation'][27] = 'homemaker'
stats['occupation'][28] = 'homemaker'
stats['occupation'][29] = 'homemaker'
stats['occupation'][30] = 'K-12 student'
stats['occupation'][31] = 'K-12 student'
stats['occupation'][32] = 'K-12 student'
stats['occupation'][33] = 'lawyer'
stats['occupation'][34] = 'lawyer'
stats['occupation'][35] = 'lawyer'
stats['occupation'][36] = 'programmer'
stats['occupation'][37] = 'programmer'
stats['occupation'][38] = 'programmer'
stats['occupation'][39] = 'retired'
stats['occupation'][40] = 'retired'
stats['occupation'][41] = 'retired'
stats['occupation'][42] = 'sales/marketing'
stats['occupation'][43] = 'sales/marketing'
stats['occupation'][44] = 'sales/marketing'
stats['occupation'][45] = 'scientist'
stats['occupation'][46] = 'scientist'
stats['occupation'][47] = 'scientist'
stats['occupation'][48] = 'self-employed'
stats['occupation'][49] = 'self-employed'
stats['occupation'][50] = 'self-employed'
stats['occupation'][51] = 'technician/engineer'
stats['occupation'][52] = 'technician/engineer'
stats['occupation'][53] = 'technician/engineer'
stats['occupation'][54] = 'tradesman/craftsman'
stats['occupation'][55] = 'tradesman/craftsman'
stats['occupation'][56] = 'tradesman/craftsman'
stats['occupation'][57] = 'unemployed'
stats['occupation'][58] = 'unemployed'
stats['occupation'][59] = 'unemployed'
stats['occupation'][60] = 'writer'
stats['occupation'][61] = 'writer'
stats['occupation'][62] = 'writer'

stats.to_csv('ranking_according_to_occupation_and_agegroup.csv')

print("Success")
