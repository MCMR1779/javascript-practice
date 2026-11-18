"""Functions for implementing the rules of the classic arcade game Pac-Man."""


def eat_ghost(power_activated, touching_ghost):
    return power_activated and touching_ghost

def score(power_pellet, touching_dots):

    return power_pellet or touching_dots

def lose(power_activated, touching_ghost):
   return not power_activated and touching_ghost
    
def win(has_eaten_all_dots, power_activated, touching_ghost):  
    return has_eaten_all_dots and not (not power_activated and touching_ghost)
  