from typing import List, Dict, Tuple
import random


def find_genre(user_songs: List[Dict[str, any]], all_songs) -> List[str]:
    """
    Function takes 2 parameters.
    :param user_songs: List of songs that user has listened to.
    :param all_songs: List of all songs
    Creates the dictionary with name of the genre as the key and number of occurrences in user_songs as value.
    Calls the function find_favourite.
    """
    genre_dict: Dict[str, int] = {}

    # loop through every song in user_songs
    for song in user_songs:
        if song['the genre of the track'] in genre_dict:
            genre_dict[song['the genre of the track']] += 1
        elif song['the genre of the track'] not in genre_dict:
            genre_dict[song['the genre of the track']] = 1

    # call the function fin_favourite that finds the most popular genre
    return find_favourite(genre_dict, all_songs)


def find_favourite(genre_dict: Dict[str, int], all_songs) -> List[str]:
    """
    Function takes 2 parameters.
    :param genre_dict: dictionary from the function find_genre
    :param all_songs: list of all songs from the dataset
    Returns the 5 songs of the favourite user genre
    """
    # converting dictionry to list of tuples
    genre_list: List[Tuple[str, int]] = [(key, val) for key, val in genre_dict.items()]
    favourite_genre_list: List[str] = []

    # sorting the list using bubblesort
    for i in range(0, len(genre_list)):
        for j in range(0, len(genre_list) - i - 1):
            if genre_list[j][1] > genre_list[j + 1][1]:
                genre_list[j], genre_list[j+1] = genre_list[j+1], genre_list[j]
    # taking the last element of the list
    favourite_genre = genre_list[-1][0]

    # searching for the songs with the same genre using linear search and adding songs to the list
    for song in all_songs:
        if song['the genre of the track'] == favourite_genre:
            favourite_genre_list.append(song['title'])

    # taking 5 random songs from the list of favourite music
    if len(favourite_genre_list) >= 5:
        final_choice: List[str] = random.sample(favourite_genre_list, 5)
    # if there arent enough songs fill the list with random songs
    else:
        final_choice: List[str] = random.sample(favourite_genre_list, len(favourite_genre_list))
        fill: int = 5 - len(favourite_genre_list)
        for i in range(fill):
            final_choice.append(random.choice(all_songs))

    return final_choice






