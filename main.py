from pathlib import Path
from typing import List, Dict
import csv
import random
from task1 import program_1
from task2 import find_genre
from task3 import week_3


class User:
    """
    Class user.
    This class represents every user in the system.
    """
    def __init__(self, user_songs: List[Dict[str, any]], number: int) -> None:
        """
        Class initializer.
        Has one atribute:
            :atr user_songs: list of songs listened by user
            :atr number: user number
        """
        self.user_songs = user_songs
        self.number = number


# opening the file using DictReader
file = csv.DictReader(open('spotify_dataset.csv', 'r'))
all_songs: List[Dict[str, any]] = []
    
# looping through the file and cleaning the dictionary values
for dictionary in file:
    for key in dictionary:
        try:
            dictionary[key] = int(dictionary[key])
        except:
            pass
    all_songs.append(dictionary)


all_len = len(all_songs)
list_of_users = []

# Creating 100 users. Each user has 20 random songs
for i in range(1, 101):
    random_songs = random.sample(all_songs, 20)
    new_user: User = User(random_songs, i)
    list_of_users.append(new_user)

dict_of_playlist: Dict[int, List[Dict[str, any]]] = {}

for i in range(1, 101):
    dict_of_playlist[i] = random.sample(all_songs, 50)



output_file_name = input('What will be the name of your output file? ')

path = Path(__file__).parent / f'../SpotifyAlgorithm/{output_file_name}.txt'

# writing to the file
with open(path, 'w', encoding='utf-8') as out_file:
    # write the title of the file
    out_file.write("Discover Weekly\n\n")
    out_file.write("Week 1\n")
    for user in list_of_users:
        out_file.write(f'User: {user.number}')
        task_1_result = program_1(dict_of_playlist, user.user_songs)
        out_file.write(f'{str(task_1_result)}\n')
    out_file.write("\n")

    out_file.write("Week 2\n")
    # loop through the users and call the tasks
    for user in list_of_users:
        out_file.write(f'User: {user.number}')
        task_2_result = find_genre(user.user_songs, all_songs)
        out_file.write(f'{str(task_2_result)}\n')

    out_file.write("\n")
    out_file.write("Week 3\n")
    for user in list_of_users:
        out_file.write(f'User: {user.number}')
        task_3_result = week_3(all_songs, user.user_songs)
        out_file.write(f'{str(task_3_result)}\n')


    #task_2_results = find_genre(user.user_songs, all_songs)
    #task_3_results = week_3(all_songs, user.user_songs)
    #print(task_1_result)

# here call three tasks

