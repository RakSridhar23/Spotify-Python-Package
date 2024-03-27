import pytest
import os
from dotenv import load_dotenv 
from src.Pytify.albums import get_artist_albums
from src.Pytify.client import get_artist_id, authenticate



class Tests:
    def test_result_format(self):
        artist = "wallows" 
        albums = get_artist_albums(artist)

        # Check if the function returns a list
        assert isinstance(albums, list)

        if not albums:
            # if no albums, return empty list
            assert albums == []
            print("No albums found for the artist.")
        else:
            # else check the format of albums
            for album in albums:
                assert isinstance(album, str)
                assert len(album) > 0

    def test_correct_info(self):
        # Call a successful response with albums
        artist = 'wallows'
        
        # Call the function
        albums = get_artist_albums(artist)

        # Check with correct information
        assert albums == ['Tell Me That It’s Over', 'Nothing Happens']
    
    def test_invalid_artist(self):
        # Call a response with no artists found
        artist = 'nonexist_artist_name_1234567'
        
        # Call the function
        albums = get_artist_albums(artist)
        
        # Check if album list is empty
        assert albums == []

    