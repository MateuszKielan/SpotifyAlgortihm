from typing import List, Dict
from statistics import mean
import random

def week_3(all_songs: List[Dict[str, any]], user_songs: List[Dict[str, any]]) -> List[str]:
    """
    The function takes a list of all songs and songs already listened to by a user and 
    returns 5 songs based on the type of music a user listened to previously.
    """
    # Global variables are created - average values of features
    avg_valence: float = mean(
        [x["Valence - The higher the value, the more positive mood for the song"] for x in all_songs])
    avg_liveness: float = mean(
        [x["Liveness - The higher the value, the more likely the song is a live recording"] for x in all_songs])
    avg_speechiess: float = mean(
        [x["Speechiness - The higher the value the more spoken word the song contains"] for x in all_songs])
    avg_BPM: float = mean([x["Beats.Per.Minute -The tempo of the song"] for x in all_songs])
    avg_energy: float = mean(
        [x["Energy- The energy of a song - the higher the value, the more energtic"] for x in all_songs])
    avg_danceability: float = mean(
        [x["Danceability - The higher the value, the easier it is to dance to this song"] for x in all_songs])
    avg_popularity: float = mean(
        [x["Popularity- The higher the value the more popular the song is"] for x in all_songs])
    avg_length: float = mean([x["Length - The duration of the song"] for x in all_songs])
    avg_loudness: float = mean([x["Loudness/dB - The higher the value, the louder the song"] for x in all_songs])

    def type_det(song: Dict[str, any]) -> List[int]:
        """
        The function takes a song as input and return its types based on a few criteria.

        The types of a song are represented as list if the song is a particular type its value is 1, 0 otherwise:
        0 - Happy
        1 - Party
        2 - Calming
        3 - Lounge

        Criteria:
            1. Happy:
              - valence > average valence of all songs
                - liveness > average liveness of all songs
                - speechiess > average speechiess of all songs
            2. Party:
                - BPM >  average BPM of all songs
                - energy > average energy of all songs
                - danceability > average danceability of all songs
                - popularity > average popularity of all songs
            3. Calming:
                - danceability < average danceability of all songs
                - BPM < average BPM of all songs
                - length > average lenght of all songs
            4. Lounge:
                - speechiess < average speechiess of all songs
                - length > average lenght of all songs
                - loudness < average loudness of all songs
        """
        # Types of a song are stored in the list where each index refers to a different type (indexes explained in docstring)
        types: List[int] = [0, 0, 0, 0]

        # Creating variables that refer to particular features
        valence: int = song["Valence - The higher the value, the more positive mood for the song"]
        liveness: int = song["Liveness - The higher the value, the more likely the song is a live recording"]
        speechiess: int = song["Speechiness - The higher the value the more spoken word the song contains"]
        BPM: int = song["Beats.Per.Minute -The tempo of the song"]
        energy: int = song["Energy- The energy of a song - the higher the value, the more energtic"]
        danceability: int = song["Danceability - The higher the value, the easier it is to dance to this song"]
        popularity: int = song["Popularity- The higher the value the more popular the song is"]
        length: int = song["Length - The duration of the song"]
        loudness: int = song["Loudness/dB - The higher the value, the louder the song"]

        # If the song meets the requirements of the given type, its value in the "types" is changed to 1
        
        # Happy
        if valence > avg_valence and liveness > avg_liveness and speechiess > avg_speechiess:
            types[0] = 1

        # Party
        if BPM > avg_BPM and energy > avg_energy and danceability > avg_danceability and popularity > avg_popularity:
            types[1] = 1

        # Calming
        if danceability < avg_danceability and BPM < avg_BPM and length > avg_length:
            types[2] = 1

        # Lounge
        if speechiess < avg_speechiess and length > avg_length and loudness < avg_loudness:
            types[3] = 1

        return types
    
    # "pref_dict" will track the frequency of types among the songs already listened to by a user 

    pref_dict: Dict[int, int] = {}
        
    # Iterate over the songs already listened to by a user and add 1 to the  "pref_dict" value if a particular type was listened to by a user.

    for song in user_songs:
        if type_det(song)[0] == 1:
            pref_dict[0] = pref_dict.get(0, 0) + 1
        if type_det(song)[1] == 1:
            pref_dict[1] = pref_dict.get(1, 0) + 1
        if type_det(song)[2] == 1:
            pref_dict[2] = pref_dict.get(2, 0) + 1
        if type_det(song)[3] == 1:
            pref_dict[3] = pref_dict.get(3, 0) + 1
            
    # Create list of ascendingly sorted tuple of "pref_dict"
    pref_dict: List[tuple] = list(sorted(pref_dict.items(), key=lambda x: x[1]))
        
    # Support variables are created 
    first_list: List[Dict[str, any]] = [] # "first_list" will contain the best type songs
    second_list: List[Dict[str, any]] = [] # "second_list" will contain second best type songs
    suggestions: List[Dict[str, any]] = [] # "suggestions" will contain 5 songs to be recommended to a user
        
    # Iterate over all songs and add a song to the "first_list" if it is the same type as the most popular type
    #                            add a song to the "second_lsit" if it is the same type as second most popular type    
    for song in all_songs:
        if type_det(song)[pref_dict[-1][0]] == 1:
            first_list.append(song)
        if type_det(song)[pref_dict[-2][0]] == 1:
            second_list.append(song)
            
    # This condition checks if there was more than one type listened to 
    if len(pref_dict) > 1:     
        # If there are at least 3 songs in the "first_list" and 2 songs in the "second_list", random 3 and 2 songs respectively are added to the "suggestions"
        # If there are fewer songs than it is required it adds more from the other list
        # In the situation when both lists are too small to recommend 5 songs, random songs chosen from all songs are added
        if len(first_list) >= 3 and len(second_list) >= 2:
            suggestions = random.sample(first_list, 3) + random.sample(second_list, 2)
        elif len(first_list) >= 5 - len(second_list):
            suggestions = random.sample(second_list, len(second_list)) + random.sample(first_list, 5 - len(suggestions))
        elif len(second_list) >= 5 - len(first_list):
            suggestions = random.sample(first_list, len(first_list)) + random.sample(second_list, 5 - len(suggestions))
        else:
            suggestions = random.sample(first_list, len(first_list)) + random.sample(second_list, len(second_list))
            if len(suggestions) < 5:
                suggestions = suggestions + random.sample(all_songs, 5 - len(suggestions))
                
    # If only one type was listened to by a user, all 5 songs are chosen from the most popular playlist. 
    # If the most popular type ("first_list") does not have 5 elements, random songs are added.
    else:
        for song in all_songs:
            if type_det(song)[pref_dict[-1][0]] == 1:
                first_list.append(song)
        if len(first_list) >= 5:
            suggestions = random.sample(first_list,5)
        else:
            suggestions = random.sample(first_list, len(first_list)) + random.sample(all_songs, 5 - len(first_list))
                                                                                    
    # The list of songs (Dictionaries) is transformed into the list of songs titles    
    suggested_songs: List[str] = []
    for song in suggestions:
        suggested_songs.append(song["title"])
                                                                                     
    return suggested_songs # The function returns the list of 5 songs titles that are recommended
