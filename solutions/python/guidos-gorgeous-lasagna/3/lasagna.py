EXPECTED_BAKE_TIME = 40
def bake_time_remaining(time):
    """Calculate the bake time remaining.
    
    Parameters:
        time (int) : Time the lasagna has already been baking.
    
    Returns:
        int : The remaining bake time in minutes.
    """
    return EXPECTED_BAKE_TIME - time
def preparation_time_in_minutes(number_of_layers):
    """Calculate the Preparation time in minutes.
    
    Parameters:
        number_of_layers (int) : The number of layers in the lasagna.
    
    Returns:
        int : Total prepration time in minutes.
    """
    return number_of_layers*2
def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calculate the elapsed cooking time.
    
    Parameters:
        number_of_layers (int): The number of layers in the lasagna.
        elapsed_bake_time (int): Time the lasagna has already been baking in the oven.
    
    Returns:
        int : Total time for preparing and baking the lasagna.
    
    This function takes two integers representing the number of lasagna layers and the time already spent baking the lasagna. It calculates the total elapsed minutes spent cooking (preparing + baking).
    """
    return number_of_layers*2 + elapsed_bake_time