#!/usr/bin/python3
"""Alta3 Resaerch | Building functions to test"""

# the homer function expects a word to be passed to it
# if it is not given one, it assumes the default "salad"
def homer(sd="salad"):
   return f"You don't win friends with {sd}"

# the milhouse function expects a word to be passed to it
# if it is not given one, it assumes the default "milhouse"
def milhouse(mh="milhouse"):
    return f"Everything is coming up {mh}"

# the troymcclure function expects a word to be passed to it
# if it is not given one, it assumes the default 3
def troymcclure(tm=3):
    if tm > 2:
        return f"2 minus {tm} equals negative fun!"
    else:
        return None