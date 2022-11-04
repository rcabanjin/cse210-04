from game.casting.actor import Actor

class Gem(Actor):
    """
    The responsible of a Gem is to give points to the player whenever the player touches one.

    Attributes:
        _message (string): Keeps the count of the player's score
    """

    def __init__(self):
        super().__init__()
        self._message = ""

    def get_message(self):
        """Gets the player's score.
        
        Returns:
            string: The score.
        """
        return self._message

    def set_message(self, message):
        """Updated the player's score.
        
        Returns:
            string: The score.
        """
        self._message = message