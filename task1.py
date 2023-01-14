from typing import List, Dict
import random


def program_1(all_playlists : Dict[int, List[Dict[str, any]]], user_songs : list) -> any:
    '''This function searches for playlist that fits certain requirements in respect to which songs the user have lisened 
    to in the dictionary of 100 playlists'''

    chosen_playlist = -1

    for playlist in all_playlists: #linear search performed on the distionary of playlists
        counter_is = 0
        counter_not = 0

        for song in user_songs:
            if song in all_playlists[playlist]:
                counter_is +=1
            else:
                
                counter_not +=1

        if counter_is >= 3 and counter_not >=3:
            chosen_playlist = playlist
            break

    if chosen_playlist == -1:
        return 'Playlist not found'
    else:
        recommended: List[str] = []
        for x in all_playlists[chosen_playlist]:
            recommended.append(x['title'])

        return random.sample(recommended, 5)


    

