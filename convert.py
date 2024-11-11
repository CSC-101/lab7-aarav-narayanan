from typing import Optional

#Purpose is toi convert a string into a float and avoid a ValueError
#Input is the string "abc"
#Output is the float or None depending on if it is an integer example above is None
def str_to_float(x:str)->Optional[float]:
    try: #Test out the string being converted to a float
        return float(x)
    except ValueError: #What to do if previous code has an exception and in this case it returns None
        return None