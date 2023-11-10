"""
    In rock, paper, scissors gaming rules:
        - a rock defeats a scissor
        - a paper defeats a rock
        - a scissor defeats a paper
"""

def winner(player, computer):
    """ 
        This function determines the winner of the game. The game is a win or loss based on his/her input and provided one of the three rules mentioned above is True.      
    """
    if (player == 'r' and computer == 's') or (player == 'p' and computer == 'r') or (player == 's' and computer == 'p'):
        return True  # player is the winner.
