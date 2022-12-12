from django.shortcuts import render

def index(request):
    """The home page for Board Game."""
    return render(request, 'board_games/index.html')
    
