
def convert(faren: float) -> float:    
    '''Converts the float parameter from degrees farenheit to celsius'''
    try: assert isinstance(faren, float)
    except: raise Exception("Float Not Provided")
    return (faren - 32) * (5/9)

