from django.db import models

class Game(models.Model):
    """A game the user has added"""
    name = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return a string reprresentation of the model"""
        return self.name

class Player(models.Model):
    """Board game players that can loan the games."""
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    player_name = models.TextField()
    
    def __str__(self):
        return f"{self.game[:50]}..."
