from django.db import models

class Game(models.Model):
    """A game the user has added"""
    name = models.CharField(max_lenght=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return a string reprresentation of the model"""
        return self.name