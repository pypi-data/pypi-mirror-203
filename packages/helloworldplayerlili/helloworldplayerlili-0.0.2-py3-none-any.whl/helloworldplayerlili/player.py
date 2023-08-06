"""
Module that includes music player class
"""

class Player:
    """
    This class creates a music player
    """

    def play(self, song: str) -> int:
        """
        Plays song received as param

        Parameters:
        song (str): song path in str format

        Returns:
        int: returns 1 if song is played successfully. Else, 0.
        """
        print(f"Playing song '{song}'")
        return 1


    def stop(self):
        """Stop this song right away!"""
        print('Stop!')
