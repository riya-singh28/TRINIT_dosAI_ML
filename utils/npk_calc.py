from random import randrange

"""
N (max = 140) 0 min
L < 21
21 < M < 84.25
H > 84.25

P (max = 145) 5 min
L < 28
28 < M < 68
H > 68

K (max = 205) 5 min
L < 20
20 < M < 49
H > 49

BASED 25 PERCENTILE AND 75 PERCENTILE OF AVAILABLE DATA
"""

# [(L range), (M range), (H range)]
range_dict = {"N":[(0,21),(21,84.25),(84.25, 140)],
              "P":[(5,28),(28,68),(68, 145)],
              "K":[(5,20),(20,49),(49, 205)]}

def N_value(in_range):
    if in_range == 'L':
        return randrange(start=range_dict["N"][0][0], stop=range_dict["N"][0][1])
    elif in_range == 'M':
        return randrange(start=range_dict["N"][1][0], stop=range_dict["N"][1][1])
    elif in_range == 'H':
        return randrange(start=range_dict["N"][2][0], stop=range_dict["N"][2][1])
    else:
        return 0

def P_value(in_range):
    if in_range == 'L':
        return randrange(start=range_dict["P"][0][0], stop=range_dict["P"][0][1])
    elif in_range == 'M':
        return randrange(start=range_dict["P"][1][0], stop=range_dict["P"][1][1])
    elif in_range == 'H':
        return randrange(start=range_dict["P"][2][0], stop=range_dict["P"][2][1])
    else:
        return 0

def K_value(in_range):
    if in_range == 'L':
        return randrange(start=range_dict["K"][0][0], stop=range_dict["K"][0][1])
    elif in_range == 'M':
        return randrange(start=range_dict["K"][1][0], stop=range_dict["K"][1][1])
    elif in_range == 'H':
        return randrange(start=range_dict["K"][2][0], stop=range_dict["K"][2][1])
    else:
        return 0

